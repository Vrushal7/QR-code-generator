import qrcode

img = qrcode.make("https://www.linkedin.com/in/vrushal-more-018a252b2/")
img.save("vrushal_linkedin.png")

import qrcode.constants

