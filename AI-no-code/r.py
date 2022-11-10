from tkinter import *
from PIL import Image,ImageTk

def window1():
    global window1
    window1 = Tk() # create window
    window1.geometry("800x500") # window dimension
    window1.title("AI no code")
    img = Image.open('12.png')
    img = img.resize((100, 88), Image.ANTIALIAS) # Resize (Height, Width)
    img = ImageTk.PhotoImage(img)
    Button(window1, text="Image",image=img, width=100, height=100, compound="top", command=window2).place(x=200, y=200)

    img2 = Image.open('13.png')
    img2 = img2.resize((100,88), Image.ANTIALIAS) # Resize (Height, Width)
    img2 = ImageTk.PhotoImage(img2)
    Button(window1, text="NLP", image=img2, width=100, height=100, compound="top", command=window2).place(x=400, y=200)
    window1.mainloop()

def window2():
    global window2
    window2 = Toplevel(window1) # create a next window from window1
    window2.geometry("800x500")
    window2.title("AI no code")

    Button(window2, text="Back to main", width=13, command=back_window).place(x=0, rely=0)
    
    if(window2):
        window1.withdraw()

    window2.mainloop()

def back_window():
    window1.iconify()
    window1.deiconify()
    window2.destroy()

window1()