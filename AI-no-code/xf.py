from doctest import master
import tkinter
from tkinter import Label, PhotoImage, Toplevel
from PIL import Image,ImageTk

root = tkinter.Tk()  
root.title('AI no code')

def openNewWindow(): 
      
    
    
    newWindow = Toplevel(master) 
  
    
    
    newWindow.title("New Window") 
  
    
    newWindow.geometry("200x200") 
  
    
    Label(newWindow,  
          text ="This is a new window").pack() 

root.geometry('600x400+50+50')
img = Image.open('12.png')
img = img.resize((80, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
botonNuevo1 = tkinter.Button(root, image=img, text="Image", compound="top", command = openNewWindow)
botonNuevo1.place(x=400, y=200, height=100, width=80)

img2 = Image.open('12.png')
img2 = img2.resize((80, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img2 = ImageTk.PhotoImage(img2)
botonNuevo2 = tkinter.Button(root, image=img2, text="NLP", compound="top",command = openNewWindow)
botonNuevo2.place(x=200, y=200, height=100, width=80)
root.mainloop()