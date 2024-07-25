import qrcode
from PIL import Image

img = qrcode.make("https://www.linkedin.com/in/vrushal-more-018a252b2/")
img.save("vrushal_linkedin.png")
print("QR code saved as 'vrushal_linkedin.png'")
img = Image.open("vrushal_linkedin.png")
img.show()