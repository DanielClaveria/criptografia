import Crypto
from Crypto.PublicKey import RSA 
from Crypto.Hash import SHA256 
from Crypto.Signature import PKCS1_v1_5

random = Crypto.Random.new().read
llaveprivada = RSA.generate(1024, random) #Las llaves siempre son en formato binario, luego se debe traducir a otro formato

print('Llave Privada: \n {0} \n'.format(llaveprivada.exportKey("PEM")))

llavepublica = llaveprivada.publickey()

print('Llave Pública: \n {0} \n'.format(llavepublica.exportKey('PEM')))

mensaje = "Este es el mensaje a FIRMAR"
mensaje = mensaje.encode()

print('\n MENSAJE A FIRMAR: \n {0} \n'.format(mensaje))

firmador = PKCS1_v1_5.new(llaveprivada)

recurso_a_firmar = mensaje

sha = SHA256.new()
sha.update(recurso_a_firmar)

firma = firmador.sign(sha)

print ("Esta es la Firma resultante: \n{0}".format(firma))


#PASO 2 VERIFICACIÓN DE FIRMA
print("VERIFICACIÓN DE FIRMA:\n")
firmador = PKCS1_v1_5.new(llavepublica)

sha = SHA256.new()
sha.update(recurso_a_firmar)

resultado = firmador.verify(sha,firma)
print('RESULTADO ES: {0}'.format(resultado))

