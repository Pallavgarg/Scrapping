import cv2
from PIL import Image
import numpy as np
img = Image.open(r'C:\Users\ADMIN\Desktop\pic.png').convert('L')
np_img = np.array(img)
np_img = ~np_img
new_im = Image.fromarray(np_img)
new_im.save("test.png")
np_img[np_img > 0] = 1
print(bytearray(np_img))
