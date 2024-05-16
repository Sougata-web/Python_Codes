import qrcode
features= qrcode.QRCode(version=1, box_size=40,border=5)

features.add_data('https://www.youtube.com/c/GeeksforGeeksVideos')
features.make(fit=True)
generate_image=features.make_image(fill_color="red",back_color="white")
generate_image.save('iamge1.png')