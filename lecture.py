from PIL import Image
from matplotlib import pyplot as plt
import time

# create figure
fig = plt.figure(figsize=(10, 7))

# setting values to rows and column variables
rows = 2
columns = 2

# reading images
im1 = Image.open('SE.png')
im2= Image.open('HCI.png')
im3 = Image.open('TOC.png')
im4 = Image.open('DBMS.png')
im5 = Image.open('Miniproject.png')
im6 = Image.open('BC.png')

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
im1.show()
plt.axis('off')
plt.title("DB")
time.sleep(60)


# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
im2.show()
plt.axis('off')
plt.title("DB/Miniproject")
time.sleep(60)

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)

# showing image
im3.show()
plt.axis('off')
plt.title("HCI")
time.sleep(60)

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)

# showing image
im4.show()
plt.axis('off')
plt.title("DB")
time.sleep(60)

im5.show()
plt.axis('off')
plt.title("SE Tutorial")
time.sleep(60)

im6.show()
plt.axis('off')
plt.title("BC")
time.sleep(60)