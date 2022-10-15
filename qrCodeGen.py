import qrcode

generate_image = qrcode.make("Raj_Randive")  # What I want to show when we scan the qr-code
generate_image.save('image1.png')