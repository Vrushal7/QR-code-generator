import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data("https://www.linkedin.com/in/vrushal-more-018a252b2/")
qr.make(fit=True)

img = qr.make_image(fill='green', back_color='black')
img.save("vrushal_linkedin_color.png")
