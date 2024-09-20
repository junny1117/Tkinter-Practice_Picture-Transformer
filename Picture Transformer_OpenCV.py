import tkinter as tk
from tkinter import Scale, filedialog, Label, Button, Frame, HORIZONTAL, VERTICAL, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import os

filename = None
imported_image = None

def show_image():
    global filename, imported_image
    
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select image file",
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG file", "*.jpg"),
                                                     ("JPEG file", "*.jpeg"),
                                                     ("All files", "*.*")))
    if filename:
        cv_image = cv2.imread(filename)
        if cv_image is None:
            messagebox.showerror("Image Load Failed", "Failed to load image.")
        else:
            cv_img_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_img_rgb).resize((380, 320), Image.LANCZOS)
            global imported_image
            imported_image = ImageTk.PhotoImage(pil_image)
            lbl.configure(image=imported_image)
            lbl.image = imported_image

def emboss_image():
    global filename, imported_image
    if filename:
        img = cv2.imread(filename)
        filter = np.array([[-1,-1, 0],
                           [-1, 0, 1],
                           [0, 1, 1]], dtype=np.float32)
        emboss_image = cv2.filter2D(img, -1, filter, delta=128)
        emboss_image_rgb = cv2.cvtColor(emboss_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(emboss_image_rgb).resize((380, 320), Image.LANCZOS)
        # Convert Image to PhotoImage
        emboss_image_tk = ImageTk.PhotoImage(pil_image)
        lbl.configure(image=emboss_image_tk)
        lbl.image = emboss_image_tk

def blur_image():
    if filename:
        img = cv2.imread(filename)
        blur_image = cv2.blur(img, (5, 5))
        blur_image_rgb = cv2.cvtColor(blur_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(blur_image_rgb).resize((380, 320), Image.LANCZOS)
        blur_image_tk = ImageTk.PhotoImage(pil_image)
        lbl.configure(image=blur_image_tk)
        lbl.image = blur_image_tk

def sharpen_image():
    if filename:
        img = cv2.imread(filename)
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        sharpen_image = cv2.filter2D(img, -1, kernel)
        sharpen_image_rgb = cv2.cvtColor(sharpen_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(sharpen_image_rgb).resize((380, 320), Image.LANCZOS)
        sharpen_image_tk = ImageTk.PhotoImage(pil_image)
        lbl.configure(image=sharpen_image_tk)
        lbl.image = sharpen_image_tk


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
        rotated_image = Image.fromarray(rotated_image)
        rotated_image = ImageTk.PhotoImage(rotated_image)
        lbl.configure(image=rotated_image)
        lbl.image = rotated_image

def rotate180():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        rotated_image = cv2.rotate(img, cv2.ROTATE_180)
        rotated_image = cv2.resize(rotated_image, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
        rotated_image = Image.fromarray(rotated_image)
        rotated_image = ImageTk.PhotoImage(rotated_image)
        lbl.configure(image=rotated_image)
        lbl.image = rotated_image

def rotate270():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        rotated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        rotated_image = cv2.resize(rotated_image, (380, 320), interpolation=cv2.INTER_LANCZOS4)
        rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
        rotated_image = Image.fromarray(rotated_image)
        rotated_image = ImageTk.PhotoImage(rotated_image)
        lbl.configure(image=rotated_image)
        lbl.image = rotated_image

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
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(image=img_pil)
        lbl.configure(image=img_tk)
        lbl.image = img_tk

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
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(image=img_pil)
        lbl.configure(image=img_tk)
        lbl.image = img_tk

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
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(image=img_pil)
        lbl.configure(image=img_tk)
        lbl.image = img_tk

def changesize():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (475,400))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB) 
        resized_image_tk = Image.fromarray(resized_image)
        resized_image_tk = ImageTk.PhotoImage(resized_image_tk)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk      

def changesize2():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (570, 480))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)  
        resized_image_tk = Image.fromarray(resized_image)
        resized_image_tk = ImageTk.PhotoImage(resized_image_tk)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk

def changesize3():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (760,640))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB) 
        resized_image_tk = Image.fromarray(resized_image)
        resized_image_tk = ImageTk.PhotoImage(resized_image_tk)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk

def changesize4():
    global filename, lbl
    if filename and lbl:
        img = cv2.imread(filename)
        resized_image = cv2.resize(img, (190,160))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)  
        resized_image_tk = Image.fromarray(resized_image)
        resized_image_tk = ImageTk.PhotoImage(resized_image_tk)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk

window = tk.Tk()
window.title("Picture Transformer")
window.geometry("900x500+100+100")
window.configure(bg="White")


img_icon = Image.open("Tkinter-Practice_Picture-Transformer/test.png")
img_icon = img_icon.resize((70, 100), Image.LANCZOS)
photo_img = ImageTk.PhotoImage(img_icon)
window.iconphoto(False, photo_img)


tk.Label(window, image=photo_img, bg="#fff").place(x=10, y=10)
tk.Label(window, text="Picture Transformer", font="arial 25 bold", fg="yellow", bg="black").place(x=90, y=50)


selectimage = tk.Frame(window, width=400, height=400, bg="#d6dee5")
selectimage.place(x=10, y=120)
f = tk.Frame(selectimage, bg="black", width=380, height=320)
f.place(x=10, y=10)
lbl = tk.Label(f, bg="black")
lbl.place(x=0, y=0)
tk.Button(selectimage, text="Select image", width=12, height=2, font="arial 14 bold", command=show_image).place(x=10, y=340)



transformationsection = Frame(width=440, height=510, bg="white")
transformationsection.place(x=450, y=10)
Label(transformationsection, text="Filters:", font="arial 20 bold", fg="black", bg="white").place(x=10, y=10)
Button(transformationsection, text="BLUR", width=12, height=2, font="arial 14 bold", command=blur_image).place(x=10,y=50)
Button(transformationsection, text="SHARP", width=12, height=2, font="arial 14 bold", command=sharpen_image).place(x=155, y=50)
Button(transformationsection, text="EMBOSS", width=12, height=2, font="arial 14 bold", command=emboss_image).place(x=300, y=50)

tk.Button(selectimage, text="Restart", width=12, height=2, font="arial 14 bold", command=restart_image).place(x=260, y=340)

Label(transformationsection, text="Rotate image:", font="arial 20 bold", fg="black", bg="white").place(x=10, y=110)
Button(transformationsection, text="90", width=12, height=2, font="arial 14 bold", command=rotate).place(x=10,y=150)
Button(transformationsection, text="180", width=12, height=2, font="arial 14 bold", command=rotate180).place(x=155, y=150)
Button(transformationsection, text="270", width=12, height=2, font="arial 14 bold", command=rotate270).place(x=300, y=150)

Button(transformationsection, text="0.5X", width=8, height=1, font="arial 14 bold", command=changesize4).place(x=10, y=470)
Button(transformationsection, text="1.25X", width=8, height=1, font="arial 14 bold", command=changesize).place(x=115, y=470)
Button(transformationsection, text="1.5X", width=8, height=1, font="arial 14 bold", command=changesize2).place(x=220, y=470)
Button(transformationsection, text="2.0X", width=8, height=1, font="arial 14 bold", command=changesize3).place(x=325, y=470)


Label(transformationsection, text="Color change:", font="arial 20 bold", fg="black", bg="white").place(x=10, y=210)
redimage = Scale(transformationsection, from_=0, to=255, orient=VERTICAL, bg="red", length=180, command=changered)
redimage.place(x=40, y=250)
Label(transformationsection, text="RED", font="arial 12 bold", fg="red", bg="white").place(x=40, y=440)
greenimage = Scale(transformationsection, from_=0, to=255, orient=VERTICAL, bg="green", length=180, command=changegreen)
greenimage.place(x=200, y=250)
Label(transformationsection, text="GREEN", font="arial 12 bold", fg="green", bg="white").place(x=200, y=440)
blueimage = Scale(transformationsection, from_=0, to=255, orient=VERTICAL, bg="blue", length=180,  command=changeblue)
blueimage.place(x=350, y=250)
Label(transformationsection, text="BLUE", font="arial 12 bold", fg="blue", bg="white").place(x=350, y=440)

window.mainloop()
