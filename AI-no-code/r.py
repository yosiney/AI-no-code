from tkinter import *
from PIL import Image,ImageTk

def ventana1():
    global ventana1
    ventana1 = Tk() # create window
    ventana1.geometry("800x500") # window dimension
    ventana1.title("AI no code")
    img = Image.open('12.png')
    img = img.resize((100, 88), Image.ANTIALIAS) # Resize (Height, Width)
    img = ImageTk.PhotoImage(img)
    Button(ventana1, text="Image",image=img, width=100, height=100, compound="top", command=ventana2).place(x=200, y=200)

    img2 = Image.open('13.png')
    img2 = img2.resize((100,88), Image.ANTIALIAS) # Resize (Height, Width)
    img2 = ImageTk.PhotoImage(img2)
    Button(ventana1, text="NLP", image=img2, width=100, height=100, compound="top", command=ventana2).place(x=400, y=200)
    ventana1.mainloop()

def ventana2():
    global ventana2
    ventana2 = Toplevel(ventana1) # create a next window from window1
    ventana2.geometry("800x500")
    ventana2.title("AI no code")

    Button(ventana2, text="Volver a principal", width=13, command=volver_ventana).place(x=0, rely=0)
    
    if(ventana2):
        ventana1.withdraw()

    ventana2.mainloop()

def volver_ventana():
    ventana1.iconify()
    ventana1.deiconify()
    ventana2.destroy()

ventana1()