import  qrcode
features = qrcode.qrcode(version=1,box_size=40,border=3)
features.add_data('https://www.youtube.com/c/GeeksforGeekVideos')
features.make(fit=True)
generate_image = qrcode.make_image(fill_color="black",back_color="white")
generate_image.save('image1.png')
