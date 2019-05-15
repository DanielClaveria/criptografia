import time
from Crypto.Hash import MD5
from Crypto.Hash import SHA256, SHA512

charRange = range(65,165) #Retorna un rango de números en un arreglo
searchHashMD5 = "187ef4436122d1cc2f40dc2b92f0eba0" #>"ab" es hash de la "clave", "ab en este caso"
startTime = time.clock()

def check(type, text_check):
    if type == 'MD5':
        h = MD5.new()
        h.update(text_check.strip().encode())
        print ("Probando MD5: {0} = {1}".format(text_check,h.hexdigest()))
        if (searchHashMD5 == h.hexdigest()):
            return True
    elif type == 'SHA256':
        h = SHA256.new()
        h.update(text_check.encode())
        print ("Probando SHA256: {0} = {1}".format(text_check,h.hexdigest()))
        #if (searchHashSHA1 == h.hexdigest()):
        #    return True
    elif type == 'SHA512':
        h = SHA512.new()
        h.update(text_check.encode())
        print ("Probando SHA512: {0} = {1}".format(text_check,h.hexdigest()))
        #if (searchHashSHA1 == h.hexdigest()):
        #    return True
    return False

# Caso base:
# -SI ancho a buscar > limite => Termina. (devuelve None)
# Caso Recursivo:
# -Para cada caracter posible
#     -SI Comprueba nuevaBase (base + caracter) == true => termina (devuelve nuevaBase)
#     -SI NO => Combina(nuevaBase, ancho + 1)
def combineChars(hashtype,base, width, maxLenght):
    if width > maxLenght:
        return
    for char in charRange:
        newBase = base + chr(char)
        if check(hashtype, newBase):
            print ("Encontrado: {0}".format(newBase))
            print ("tiempo: {0}".format(time.clock() - startTime))
            exit()
        else:
            combineChars(hashtype, newBase, width + 1, maxLenght)


combineChars('MD5','', 1, 3)

#for char in charRange:
#    print(chr(char))
