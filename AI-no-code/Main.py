from tkinter import *
from tkinter import Tk, Button
from PIL import Image,ImageTk
from c_image import Window
from NLP import NLPWindow

class App(Tk):
   
    def __init__(self):

        super().__init__()

        self.geometry("800x500+500+200") # window dimension
        self.title("AI no code")

        bg = PhotoImage(file = 'Icons/font.png') 
        backgraund = Label( self, image = bg )
        backgraund.place(x = 0, y = 0) 
        
        backgraund.image = bg
        backgraund.pack(side = "bottom", fill = "both", expand = "yes")

        self.img = Image.open('Icons/IMAGE-ICON.png')
        self.img =  self.img.resize((100, 88), Image.ANTIALIAS) # Resize (Height, Width)
        self.img = ImageTk.PhotoImage( self.img)
        #self.flag_image = PhotoImage(file="Icons/IMAGE-ICON.png", width=100, height=100)
        
        button = Button( self,image= self.img,text="Image", width=100 , height=100,compound="top", command=self.open_window).place(x=220, y=200)
 
        self.img2 = Image.open('Icons/NLP-ICON.png')
        self.img2 = self.img2.resize((100,85), Image.ANTIALIAS) # Resize (Height, Width)
        self.img2 = ImageTk.PhotoImage(self.img2)
      
        Button(self, text="NLP",image=self.img2, width=100, height=100, compound="top", command= self.open_windowNLP).place(x=420, y=200)

        menubar = Menu(self)
        self.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="CLose")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cute")
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Paste")

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help")
        helpmenu.add_separator()
        helpmenu.add_command(label="about...")

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
            # place a button on the root window
       
    def open_window(self):
        window = Window(self)
        window.grab_set()
        #self.withdraw()

    def open_windowNLP(self):
        window = NLPWindow(self)
        window.grab_set()
        #self.withdraw()
     

 
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
    app = App()
    app.mainloop()
   #window1()