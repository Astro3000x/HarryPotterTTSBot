#Import the required library
from tkinter import *
from PIL import Image, ImageTk

#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("750x600")
win.title("Gallery")

#Define a Function to change to Image
def change_img():
   img2=ImageTk.PhotoImage(Image.open("paintingclosed.png"))
   label.configure(image=img2)
   label.image=img2

#Convert To PhotoImage
img1= ImageTk.PhotoImage(Image.open("paintingopen.png"))

#Create a Label widgetxs
label= Label(win,image= img1)
label.pack()

#Create a Button to handle the update Image event
button= Button(win, text= "Change", font= ('Helvetica 13 bold'),
command= change_img)
button.pack(pady=15)
win.bind("<Return>", change_img)
win.mainloop()