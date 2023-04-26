import qrcode

data = 'https://mail.google.com/mail/u/0/#inbox'

img = qrcode.make(data)

img.save('C:/Users/Madoda/Desktop/PyTest/QR_Encode-Decoder/myQRcode.png')
