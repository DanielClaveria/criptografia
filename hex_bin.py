import binascii
import codecs
"""
HexByteConversion

Convert a byte string to it's hex representation for output or visa versa.

ByteToHex converts byte string "\xFF\xFE\x00\x01" to the string "FF FE 00 01"
HexToByte converts string "FF FE 00 01" to the byte string "\xFF\xFE\x00\x01"
"""

#-------------------------------------------------------------------------------

def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    
    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #   
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()        

    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()

#-------------------------------------------------------------------------------

def HexToByte( hexStr ):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    # The list comprehension implementation is fractionally slower in this case    
    #
    #    hexStr = ''.join( hexStr.split(" ") )
    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
    #                                   for i in range(0, len( hexStr ), 2) ] )
 
    bytes = []

    hexStr = ''.join( hexStr.split(" ") )

    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

    return ''.join( bytes )

#-------------------------------------------------------------------------------

# test data - different formats but equivalent data
hexStr1  = "68 6f 6c 61 00 00 00 00 00 00 00 00 00 00 00 00 "
hexStr2  = "686f6c61000000000000000000000000"


#print(hexStr2.decode('utf8'))
print(codecs.decode(hexStr2, "hex").decode('utf-8'))
print(bytes.fromhex(hexStr1))
#byteStr = "\xFF\xFF\xFF\x5F\x81\x21\x07\x0C\x00\x00\xFF\xFF\xFF\xFF\x5F\x81\x29\x01\x0B"


#print ("\nHex To Byte and Byte To Hex Conversion")

#print ("Test 1 - ByteToHex - Passed: {0}".format(ByteToHex( byteStr)))
#rint ("Test 2 - HexToByte - Passed: {0}".format(HexToByte( hexStr1 )))
#print ("Test 3 - HexToByte - Passed: {0}".format(HexToByte( hexStr2 )))

#print(binascii.unhexlify(hexStr1))


