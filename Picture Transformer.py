import tkinter as tk
from tkinter import Scale, filedialog, Label, Button, Frame, HORIZONTAL, VERTICAL
from PIL import Image, ImageTk, ImageFilter
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
        img = Image.open(filename)
        img = img.resize((380, 320), Image.LANCZOS)  
        imported_image = ImageTk.PhotoImage(img)
        lbl.configure(image=imported_image)
        lbl.image = imported_image  

def apply_filter(filter_function):
    global filename, imported_image
    if filename:
        image = Image.open(filename)
        filtered_image = filter_function(image)
        filtered_image = filtered_image.resize((380, 320), Image.LANCZOS)  
        filtered_image = ImageTk.PhotoImage(filtered_image)
        lbl.configure(image=filtered_image)
        lbl.image = filtered_image

def blur_image():
    apply_filter(lambda img: img.filter(ImageFilter.BLUR))

def contour_image():
    apply_filter(lambda img: img.filter(ImageFilter.CONTOUR))

def emboss_image():
    apply_filter(lambda img: img.filter(ImageFilter.EMBOSS))

def restart_image():
    global imported_image
    if imported_image:
        lbl.configure(image=imported_image)
        lbl.image = imported_image

def rotate(_):
    global filename
    if filename:
        angle = rotateimage.get() 
        image = Image.open(filename)
        rotated_image = image.rotate(angle)
        rotated_image = rotated_image.resize((380, 320), Image.LANCZOS)  # Resize rotated image to fit the frame
        rotated_image = ImageTk.PhotoImage(rotated_image)
        lbl.configure(image=rotated_image)
        lbl.image = rotated_image



def changered(var):
    global filename
    if filename:
        image5 = Image.open(filename)
        r, g, b = image5.split()
        r = r.point(lambda i: redimage.get())
        coloredimage = Image.merge("RGB", (r, g, b))
        coloredimage = ImageTk.PhotoImage(coloredimage)
        lbl.configure(image=coloredimage, width=380, height=320)
        lbl.image = coloredimage

def changeblue(var):
    global filename
    if filename:
        image5 = Image.open(filename)
        r, g, b = image5.split()
        b = b.point(lambda i: blueimage.get())
        coloredimage = Image.merge("RGB", (r, g, b))
        coloredimage = ImageTk.PhotoImage(coloredimage)
        lbl.configure(image=coloredimage, width=380, height=320)
        lbl.image = coloredimage

def changegreen(var):
    global filename
    if filename:
        image5 = Image.open(filename)
        r, g, b = image5.split()
        g = g.point(lambda i: greenimage.get())
        coloredimage = Image.merge("RGB", (r, g, b))
        coloredimage = ImageTk.PhotoImage(coloredimage)
        lbl.configure(image=coloredimage, width=380, height=320)
        lbl.image = coloredimage

def changesize():
    global filename
    if filename:
        image = Image.open(filename)
        resized_image = image.resize((475, 400), Image.LANCZOS)
        resized_image_tk = ImageTk.PhotoImage(resized_image)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk       

def changesize2():
    global filename
    if filename:
        image = Image.open(filename)
        resized_image = image.resize((570, 480), Image.LANCZOS)
        resized_image_tk = ImageTk.PhotoImage(resized_image)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk

def changesize3():
    global filename
    if filename:
        image = Image.open(filename)
        resized_image = image.resize((760, 640), Image.LANCZOS)
        resized_image_tk = ImageTk.PhotoImage(resized_image)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk

def changesize4():
    global filename
    if filename:
        image = Image.open(filename)
        resized_image = image.resize((190, 160), Image.LANCZOS)
        resized_image_tk = ImageTk.PhotoImage(resized_image)
        lbl.configure(image=resized_image_tk, width=380, height=320)
        lbl.image = resized_image_tk

window = tk.Tk()
window.title("Picture Transformer")
window.geometry("900x500+100+100")
window.configure(bg="White")


img_icon = Image.open("test.png")
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
Button(transformationsection, text="BLUR", width=12, height=2, font="arial 14 bold", command=blur_image).place(x=10,
                                                                                                              y=50)
Button(transformationsection, text="CONTOUR", width=12, height=2, font="arial 14 bold", command=contour_image).place(x=155, y=50)
Button(transformationsection, text="EMBOSS", width=12, height=2, font="arial 14 bold", command=emboss_image).place(x=300, y=50)
tk.Button(selectimage, text="Restart", width=12, height=2, font="arial 14 bold", command=restart_image).place(x=260, y=340)
Label(transformationsection, text="Rotate image:", font="arial 20 bold", fg="black", bg="white").place(x=10, y=110)
rotateimage = Scale(transformationsection, from_=0, to=360, orient=HORIZONTAL, bg="white", length=420, command=rotate)
rotateimage.place(x=10, y=150)

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
