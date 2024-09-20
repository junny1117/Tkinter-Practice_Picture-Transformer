import numpy as np
import cv2
import os
from flask import Flask, render_template


app = Flask(__name__)

filename = None
imported_image = None

def show_image():
    global filename, imported_image
    
    img = cv2.imread(initialdir=os.getcwd(),
                                          title="Select image file",
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG file", "*.jpg"),
                                                     ("JPEG file", "*.jpeg"),
                                                     ("All files", "*.*")))

    if img is None:
        print("Image Load Failed", "Failed to load image.")


def emboss_image():
    global filename, imported_image
    if filename:
        img = cv2.imread(filename)
        filter = np.array([[-1,-1, 0],
                           [-1, 0, 1],
                           [0, 1, 1]], dtype=np.float32)
        emboss_image = cv2.filter2D(img, -1, filter, delta=128)
        emboss_image_rgb = cv2.cvtColor(emboss_image, cv2.COLOR_BGR2RGB)
  

def blur_image():
    if filename:
        img = cv2.imread(filename)
        blur_image = cv2.blur(img, (5, 5))
        blur_image_rgb = cv2.cvtColor(blur_image, cv2.COLOR_BGR2RGB)
 

def sharpen_image():
    if filename:
        img = cv2.imread(filename)
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        sharpen_image = cv2.filter2D(img, -1, kernel)
        sharpen_image_rgb = cv2.cvtColor(sharpen_image, cv2.COLOR_BGR2RGB)



def restart_image():
    global imported_image
    if imported_image:
        lbl.configure(image=imported_image)
        lbl.image = imported_image

def rotate():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        rotated_image = cv2.resize(rotated_image, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

def rotate180():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        rotated_image = cv2.rotate(img, cv2.ROTATE_180)
        rotated_image = cv2.resize(rotated_image, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

def rotate270():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        rotated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        rotated_image = cv2.resize(rotated_image, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

red_lut = np.arange(256, dtype=np.uint8)
green_lut = np.arange(256, dtype=np.uint8)
blue_lut = np.arange(256, dtype=np.uint8)

def changered(value):
    global filename, lbl, red_lut
    if filename and lbl:
        img = cv2.imread(filename)
        b, g, r = cv2.split(img)
        red_value = int(value)
        red_lut = np.array([red_value] * 256, dtype=np.uint8)
        r = cv2.LUT(r, red_lut)
        img = cv2.merge((b, g, r))
        img = cv2.resize(img, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def changegreen(value):
    global filename, lbl, green_lut
    if filename and lbl:
        img = cv2.imread(filename)
        b, g, r = cv2.split(img)
        green_value = int(value)
        green_lut = np.array([green_value] * 256, dtype=np.uint8)
        g = cv2.LUT(g, green_lut)
        img = cv2.merge((b, g, r))
        img = cv2.resize(img, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def changeblue(value):
    global filename, lbl, blue_lut
    if filename and lbl:
        img = cv2.imread(filename)
        b, g, r = cv2.split(img)
        blue_value = int(value)
        blue_lut = np.array([blue_value] * 256, dtype=np.uint8)
        b = cv2.LUT(b, blue_lut)
        img = cv2.merge((b, g, r))
        img = cv2.resize(img, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def changesize():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (475,400))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)   

def changesize2():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (570, 480))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)  


def changesize3():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (760,640))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB) 


def changesize4():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (190,160))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)  




