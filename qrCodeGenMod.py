import qrcode

features = qrcode.QRCode(version=2, box_size=30, border=1)
features.add_data('file_Path')
features.make(fit=True)  # whatever box_sizing and border we have given should be fit in that particular size only

# ****************************************************************************************************
generate_image = features.make_image(fill_color = "black", back_color = "white")
generate_image.save('image5.png')