import time
from PIL import Image
while(1):
    im = Image.open('qrcode.png')
    im.show()
    time.sleep(15)

