import qrcode

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=2)

qr.add_data('https://www.youtube.com/watch?v=l4ugfcj7qrI')

qr.make_image(fit=True,)

img=qr.make_image(fill_color="red",back_color="white")
img.save('advanced3.png')