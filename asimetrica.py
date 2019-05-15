#import hashlib
#import base64
import Crypto
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP #PKCS1_OAEP librería con algoritmos para cifrar y desifrar, simétrica y asimétrica


#PASO 1: OBTENER LLAVES PUBLICA Y PRIVADA

random = Crypto.Random.new().read
llaveprivada = RSA.generate(1024, random) #Las llaves siempre son en formato binario, luego se debe traducir a otro formato

print('Llave Privada: \n {0} \n'.format(llaveprivada.exportKey("PEM")))

llavepublica = llaveprivada.publickey()

print('Llave Pública: \n {0} \n'.format(llavepublica.exportKey('PEM')))

mensaje = "Este es el mensaje a encriptar"
mensaje = mensaje.encode()

'''
OBS: str.encode transforma string a UTF-8 (default), formato exigido por la función que encripta, si no, da error de tipo
Con parámetros es posible utilizar otros formatos como Base64.encode
'''
print('\n MENSAJE A ENCRIPTAR: \n {0} \n'.format(mensaje))

#PASO2: PROCESO DE ENCRIPTACIÓN CON LLAVE PUBLICA:
cifrador = PKCS1_OAEP.new(llavepublica) #IMPORTANTE: Instancia objeto RSA para encriptar asimétricamente

mensaje_cifrado = cifrador.encrypt(mensaje)

print('Este es el mensaje_cifrado (con llave Pública): \n {0} \n'.format(mensaje_cifrado))

#PASO 3: PROCESO DE DESENCRIPACIÓN CON LLAVE PRIVADA
cifrador = PKCS1_OAEP.new(llaveprivada)

mensaje_descifrado = cifrador.decrypt(mensaje_cifrado)

print('este es el mensaje DESCIFRADO (con llave Privada): \n {0} \n'.format(mensaje_descifrado))



#¿Funciona el mismo proceso pero invirtiendo el orden de las llaves?
#a ver...

print('¿Funciona el mismo proceso pero invirtiendo el orden de las llaves?')

cifrador = PKCS1_OAEP.new(llaveprivada) #IMPORTANTE: Instancia objeto RSA para encriptar asimétricamente

mensaje_cifrado = cifrador.encrypt(mensaje) #Recordar que mensaje está en UTF-8

print('Este es el mensaje_cifrado (con llave Privada): {0}'.format(mensaje_cifrado))

 #INICIO PROCESO DE DESENCRIPTACIÓN
cifrador = PKCS1_OAEP.new(llavepublica)

mensaje_descifrado = cifrador.decrypt(mensaje_cifrado)

print('este es el mensaje descifrado (con llave Pública): {0}'.format(mensaje_descifrado))
