import  qrtools
# import qrcode

qr=qrtools.QR()
myCode=qr.decode('advanced.png')
print(myCode)
# if(myCode.decode):
#     print(myCode.data)
#     print(myCode.data_to_string)