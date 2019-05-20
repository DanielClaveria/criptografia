import time
from Crypto.Hash import MD5
from Crypto.Hash import SHA256, SHA512

#charRange = range(32,127) #Retorna un rango de números en un arreglo
#searchHashMD5 = "187ef4436122d1cc2f40dc2b92f0eba0" #>"ab" es hash de la "clave", "ab en este caso"
startTime = time.clock()


class FuerzaBrutaHash(object):
    def __init__(self, tipo_hash, hash_a_buscar, rango):
        self.tipo_hash = tipo_hash
        self.hash_a_buscar = hash_a_buscar
        self.rango = rango

    def check(self, text_check):
        if self.tipo_hash == 'MD5':
            h = MD5.new()
            h.update(text_check.strip().encode())
            print ("Probando MD5: {0} = {1}".format(text_check,h.hexdigest()))
            if (self.hash_a_buscar == h.hexdigest()):
                return True
        elif self.tipo_hash == 'SHA256':
            h = SHA256.new()
            h.update(text_check.encode())
            print ("Probando SHA256: {0} = {1}".format(text_check,h.hexdigest()))
            if (self.hash_a_buscar == h.hexdigest()):
                return True
        elif self.tipo_hash == 'SHA512':
            h = SHA512.new()
            h.update(text_check.encode())
            print ("Probando SHA512: {0} = {1}".format(text_check,h.hexdigest()))
            if (self.hash_a_buscar == h.hexdigest()):
                return True
        return False

    def combineChars(self, base, width, maxLenght):
        if width > maxLenght:
            return
        for char in self.rango:
            newBase = base + chr(char)
            if self.check(newBase):
                print ("Encontrado: {0}".format(newBase))
                print ("tiempo: {0}".format(time.clock() - startTime))
                exit()
            else:
                self.combineChars(newBase, width + 1, maxLenght)


'''
EN este programa se amula un sistema que encuentra hash de distintos tipos
'''

print(".:CONFIGURACIÓN DE TEXTO AUTOGENERADO:.")

print ("¿Desea utilizar un prefijo para concatenar al texto aleatorio? deje en blanco su respuesta si no lo requiere")
prefijo = input("Texto prefijo: ")

print("Indique la cantidad de caracteres que requiere generar:")
maximo = int(input('largo máximo: '))

print("Caracteres a Generar:")
rango_caracteres = []
if input("¿Desea utilizar todo el código ASCII? (s/n): ") in ('si','s','SI','S','Y'):
    rango_caracteres = range(0,127)
else:

    if input("Incluir abecedario en mayúscula (s/n): ") in ('si','s','SI','S','Y'):
        rango_caracteres += range(65,90)
    if input("Incluir abecedario en minúscula (s/n): ") in ('si','s','SI','S','Y'):
        rango_caracteres += range(97,122)
    if input("Incluir números (s/n): ") in ('si','s','SI','S','Y'):
        rango_caracteres += range(48,57)
    if input("Incluir caracteres especiales (s/n): ") in ('si','s','SI','S','Y'):
        rango_caracteres += range(33,47)
        rango_caracteres += range(58,64)
        rango_caracteres += range(92,96)
    if input("Incluir espacios en blanco (s/n): ") in ('si','s','SI','S','Y'):
        rango_caracteres += range(32,33)

    excluir = ''
    excluir = input("\nIndique caracteres a excluir de la búsqueda: ")

    for i, c in enumerate(excluir):
        rango_caracteres.remove(ord(excluir[i]))


rango_final = []
for l in rango_caracteres:
    rango_final.append(chr(l))

print ("Estos son los caracteres que se utilizarán para generar las palabras aleatorias:\n{0}".format(rango_final))
input("presione enter para continuar...")

print(".:DATOS DE ENTRADA DEL HASH A BUSCAR:.\n")

print("Tipo de HASH:\n")
print("1. MD5\n2. SHA256\n3. SHA512")
tipo = input("Indique opción para Tipo de Hash: ")
in_tipo_hash = 'MD5' #Default
if tipo == '1':
    in_tipo_hash = 'MD5'
elif tipo == '2':
    in_tipo_hash = 'SHA256'
elif tipo == '3':
    in_tipo_hash = 'SHA512'

if input("¿Desea emular una búsqueda ingresando una palabra para buscar el hash por Fuerza Bruta (s/n): ") in ('si','s','SI','S','Y'):
    palabra = input("indique el texto para generar su hash de tipo {0}: ".format(in_tipo_hash))
    if in_tipo_hash == 'MD5':
        in_hash = MD5.new()
        in_hash.update(palabra.strip().encode())
        print ("en MD5: {0} = {1}".format(palabra,in_hash.hexdigest()))
    elif in_tipo_hash == 'SHA256':
        in_hash = SHA256.new()
        in_hash.update(palabra.strip().encode())
        print ("en SHA256: {0} = {1}".format(palabra,in_hash.hexdigest()))
    elif in_tipo_hash == 'SHA512':
        in_hash = SHA512.new()
        in_hash.update(palabra.strip().encode())
        print ("en SHA512: {0} = {1}".format(palabra,in_hash.hexdigest()))

    txt_hash = in_hash.hexdigest()
    input("presione enter para continuar...")
else:
    txt_hash = ''
    txt_hash = input("Pegue el texto del hash en hexadecimal: ")

objFuerzaBruta = FuerzaBrutaHash(in_tipo_hash,txt_hash,rango_caracteres)
objFuerzaBruta.combineChars(prefijo,1,maximo)
#combineChars('MD5','', 1, 3)



#for char in charRange:
#    print(chr(char))
