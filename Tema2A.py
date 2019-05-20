import time
from Crypto.Hash import MD5
from Crypto.Hash import SHA256, SHA512
from Crypto.Cipher import AES
import binascii
import codecs

charRange = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] #Retorna un rango de números en un arreglo
print(charRange)
startTime = time.clock()

def check(llave_aleatoria, mensajeoriginal_hex_text, mensajeencriptado_hex_text):
    print(llave_aleatoria)
    llave_bytes = bytes(llave_aleatoria,'utf-8')
    #print(llave_bytes)
    llave_hexadecimal = llave_bytes.hex() 
    #print(llave_hexadecimal)
    #print(str(llave_hexadecimal) + ("0" * (32-( len(str(llave_hexadecimal))) )))

    llave_hexa_string = llave_aleatoria + ("0" * (32-( len(str(llave_aleatoria))) ))
    print(llave_hexa_string)
    #llave_hexa_string = '81 17 90 39 b0 00 00 00 00 00 00 00 00 00 00 00'.replace(' ','')

    encryptor = AES.new(bytes.fromhex(llave_hexa_string))

    mensajeoriginal_text = bytes.fromhex(mensajeoriginal_hex_text)
    
    msg_enc = encryptor.encrypt(mensajeoriginal_text)

    #print(msg_enc.hex())
    #print(mensajeencriptado_hex_text)
    #mensajeencriptado_text =  bytes.fromhex(mensajeencriptado_hex_text)
    #print('mensaje enc original: ' + mensajeencriptado_text.hexdigest())

    if msg_enc.hex() == mensajeencriptado_hex_text:
        return True
    return False

def combineChars(base, width, maxLenght):
    if width > maxLenght:
        return
    for char in charRange:
        newBase = base + char
        inm1 = '68 6f 6c 61 00 00 00 00 00 00 00 00 00 00 00 00'.replace(' ','')
        inc1 = 'da b1 aa 35 4e da 79 1d 5b 1d 1f d3 17 05 ee 6c'.replace(' ','')
        if check(newBase,inm1,inc1):
            print ("Encontrado: {0}".format(newBase))

            print ("tiempo: {0}".format(time.clock() - startTime))
            exit()
        else:
            combineChars(newBase, width + 1, maxLenght)

combineChars('811790', 1, 4)
print ("Llave: {0}".format(str(bytes.fromhex('81 17 90 39 b0 00 00 00 00 00 00 00 00 00 00 00'.replace(' ','')))))
#for char in charRange:
#    print(chr(char))


'''
M1 =    '68 6f 6c 61 00 00 00 00 00 00 00 00 00 00 00 00'
bM1 = bytes.fromhex(M1)
print('mensaje Original: {0}'.format(M1))
print('mensaje Original en bytes: {0}'.format(bM1))
print('mensaje Original en texto: {0}'.format(bM1.decode()))

txtM1 = 'hola'
bytesTxtM1 = bytes(txtM1,'utf-8')
HexM1 = bytesTxtM1.hex() + '000000000000000000000000'  
print('Texto: {0}'.format(txtM1))
print('Texto Hex: {0}'.format(HexM1))
print('Texto Byte: {0}'.format(bytesTxtM1.decode()))
'''