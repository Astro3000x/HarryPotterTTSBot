#Import the required library
from tkinter import *
from PIL import Image, ImageTk



#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("300x447")
win.title("Painting")

painting = Image.open("painting.jpg")

resized = painting.resize((300, 447), Image.ANTIALIAS)

p2 = ImageTk.PhotoImage(resized)



label= Label(win,image=p2)
label.pack()

#Create a Button to handle the update Image event

win.mainloop()