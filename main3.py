import qrcode as qr
from PIL import Image
code_img=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H ,box_size=10,border=5)
code_img.add_data("Paste here link to be encoded")
code_img.make(fit=True)
img=code_img.make_image(fill_color="black",back_color="red")
img.save("image_name.png")
