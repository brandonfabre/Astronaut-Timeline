from tkinter import *
import sys
from PIL import Image, ImageTk

#window = Tk()

#anvas = Canvas(window, width = 500, height = 500)

#canvas.pack()
root = Tk()
root.geometry('1000x1000')

mylabel = Label(root, text = "Hello World!")
mylabel.pack()

def buttonFunction():
    print("Hello world!")

b = Button(root, text = "Click me!", command = buttonFunction)
b.pack()

photo = Image.open("/Users/karlhickel/Documents/GitHub/MachineLearning/issPictures/1.jpg")
photo2 = Image.open("/Users/karlhickel/Documents/GitHub/MachineLearning/issPictures/2.jpg")
render = ImageTk.PhotoImage(photo)
render2 = ImageTk.PhotoImage(photo2)

img = Label(root, image=render)
img2 = Label(root, image=render2)
img.pack()
img2.pack()

img.grid(row=3, column=3)
#img2.grid(row=4,column=4)



root.mainloop()


