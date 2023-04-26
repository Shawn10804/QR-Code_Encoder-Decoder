import qrcode

data = 'https://www.linkedin.com/in/mzwamadoda-shawn-louw-a55aa414b/'                                        #How you want your qrcode to have or display when scamned

qr = qrcode.QRCode(version=1, box_size=10, border=5)                                    #Styling the QRcode and siziing it according to built in fuctions

qr.add_data(data)                                                                       #Then you adding the data inside the QRCode

qr.make(fit=True)                                                                       #You make the data fit inside the qr code -- you can also call this process, styling of QRcode
img = qr.make_image(fill_color='yellow', black_color='red')                             #Declared a new variable img, then made a QRCode and styled it based on the colors etc
img.save('C:/Users/Madoda/Desktop/PyTest/QR_Encode-Decoder/mySecondQR-Code.png')        #when done, you need to save it, in the destination folder where you'll be able to view it