from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Madoda/Desktop/PyTest/QR_Encode-Decoder/myQRcode.png')

nowDecode = decode(img)

print(nowDecode)

#You can Decode other website QRcodes too
#Look for decoding a list of different QRcode at once or in one file. They'll be in Object format kodwa