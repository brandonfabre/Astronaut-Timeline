
import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = tkinter.Tk()
root.configure(background='#16e116')
root.title('Pop Up')
root.geometry('500x500')


photo = Image.open("/Users/karlhickel/Documents/GitHub/MachineLearning/issPictures/1.jpg")
photo2 = Image.open("/Users/karlhickel/Documents/GitHub/MachineLearning/issPictures/2.jpg")
render = ImageTk.PhotoImage(photo)
render2 = ImageTk.PhotoImage(photo2)

w = Label(root, image=render)
text = Label(root, text="Hello world!")

w2 = Label(root, image=render2)
text2 = Label(root, text="eat my ass")


w.grid(row=3, column=3)
text.grid(row=3, column=3)

w2.grid(row=3,column=4)


root.mainloop()