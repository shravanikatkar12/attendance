import time
from PIL import Image

while (True):
    im = Image.open('qrcode.png')
    time.sleep(300)
im.show()