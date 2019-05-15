import os, random, struct
from Crypto.Cipher import AES

class MyFile(object):
    """docstring for Archivo"""
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.fullPath = self.path + self.name

        print('ARCHIVO: {0}'.format(self.fullPath))
        
    def encriptarAES(self, key, out_name = None, chunksize=64*1024):
        if not(out_name):
            self.outfilename = self.path + self.name + '.enc'
        else:
            self.outfilename = self.path + out_name

        print(key)
        iv = ''.join(chr(random.randint(32, 90)) for i in range(16))
        print(iv)    
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(self.fullPath)
        print(filesize)

        with open(self.fullPath, 'rb') as infile:
            with open(self.outfilename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv.encode('utf-8'))

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))

    def desencriptarAES(self, key, out_name = None, chunksize=64*1024):
        print(key)        
        if not out_filename:
            out_filename = os.path.splitext(self.fullPath)[0]

        with open(self.fullPath, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)

miarchivo = MyFile('','candado.jpg')
miarchivo.encriptarAES('1234567890123456','candado.jpg.encDES')
print (miarchivo.name + ' ' + miarchivo.path)

