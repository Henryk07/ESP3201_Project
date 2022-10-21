import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
import pathlib
from PIL import Image
from tensorflow import keras

im = Image.open('ECG_Image_data/bw/F0.png')
# im.show(im)

with Image.open("ECG_Image_data/bw/M2101.png") as im:
    gray = im.convert("L")
    # im.show(im)
    bw = gray.point(lambda x: 0 if x < 200 else 255, 'L')
    bw.show()
    # bw.save("ECG_Image_data/bw/Q12_bw.png")
