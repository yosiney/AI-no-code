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
    Button(window1, text="NLP", image=img2, width=100, height=100, compound="top", command=window3).place(x=400, y=200)

    menubar = Menu(window1)
    window1.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_command(label="CLose")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window1.quit)

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

    # Finally application loop
    window1.mainloop()

def window2():
    global window2
    window2 = Toplevel(window1) # create a next window from window1
    window2.geometry("800x500")
    window2.title("AI no code")

    Button(window2, text="Back to main", width=10, command=back_window).place(x=0, rely=0)

    img3 = Image.open('Icon1.png')
    img3 = img3.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img3 = ImageTk.PhotoImage(img3)
    Button(window2, text=" Image classification",image=img3, width=198, height=30, compound="left", command=back_window).place(x=30, y=50)

    img4 = Image.open('Icon2.png')
    img4 = img4.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img4 = ImageTk.PhotoImage(img4)
    Button(window2, text=" Image Segmentation", image=img4, width=198, height=30, compound="left", command=back_window).place(x=260, y=50)

    img5 = Image.open('Icon3.png')
    img5 = img5.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img5 = ImageTk.PhotoImage(img5)
    Button(window2, text=" Zero-shot Image Classification", image=img5, width=198, height=30, compound="left", command=back_window).place(x=30, y=100)

    img6 = Image.open('Icon4.png')
    img6 = img6.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img6 = ImageTk.PhotoImage(img6)
    Button(window2, text=" Image-to-image", image=img6, width=198, height=30, compound="left", command=back_window).place(x=30, y=150)

    img7 = Image.open('Icon5.png')
    img7 = img7.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img7 = ImageTk.PhotoImage(img7)
    Button(window2, text=" Unconditional Image Generation", image=img7, width=198, height=30, compound="left", command=back_window).place(x=30, y=190)
    
    img8 = Image.open('Icon6.png')
    img8 = img8.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img8 = ImageTk.PhotoImage(img8)
    Button(window2, text=" OBject Detection", image=img8, width=198, height=30, compound="left", command=back_window).place(x=30, y=230)

    img9 = Image.open('Icon7.png')
    img9 = img9.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img9 = ImageTk.PhotoImage(img9)
    Button(window2, text=" Video Classification", image=img9, width=198, height=30, compound="left", command=back_window).place(x=260, y=230)
    
    if(window2):
        window1.withdraw()

    window2.mainloop()

def window3():
    global window3
    window3 = Toplevel(window1) # create a next window from window1
    window3.geometry("800x500")
    window3.title("AI no code")

    Button(window3, text="Back to main", width=10, command=back_window2).place(x=0, rely=0)

    img10 = Image.open('Icon1.png')
    img10 = img10.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img10 = ImageTk.PhotoImage(img10)
    Button(window3, text=" Traslation",image=img10, width=198, height=30, compound="left", command=back_window).place(x=30, y=50)

    img11 = Image.open('Icon7.png')
    img11 = img11.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img11 = ImageTk.PhotoImage(img11)
    Button(window3, text=" Fill-Mask", image=img11, width=198, height=30, compound="left", command=back_window).place(x=250, y=50)

    img12 = Image.open('Icon2.png')
    img12 = img12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img12 = ImageTk.PhotoImage(img12)
    Button(window3, text=" Token Classification", image=img12, width=198, height=30, compound="left", command=back_window).place(x=30, y=100)

    img13 = Image.open('Icon7.png')
    img13 = img13.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img13 = ImageTk.PhotoImage(img13)
    Button(window3, text=" Sentence Similarity", image=img13, width=198, height=30, compound="left", command=back_window).place(x=250, y=100)

    img14 = Image.open('Icon3.png')
    img14 = img14.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img14 = ImageTk.PhotoImage(img14)
    Button(window3, text=" Question Answering", image=img14, width=198, height=30, compound="left", command=back_window).place(x=30, y=150)

    img15 = Image.open('Icon3.png')
    img15 = img15.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img15 = ImageTk.PhotoImage(img15)
    Button(window3, text=" Summarization", image=img15, width=198, height=30, compound="left", command=back_window).place(x=250, y=150)

    img16 = Image.open('Icon4.png')
    img16 = img16.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img16 = ImageTk.PhotoImage(img16)
    Button(window3, text=" Zero-Shot-Classification", image=img16, width=198, height=30, compound="left", command=back_window).place(x=30, y=200)

    img17 = Image.open('Icon5.png')
    img17 = img17.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img17 = ImageTk.PhotoImage(img17)
    Button(window3, text=" Text Classification", image=img17, width=198, height=30, compound="left", command=back_window).place(x=30, y=250)

    img18 = Image.open('Icon2.png')
    img18 = img18.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img18 = ImageTk.PhotoImage(img18)
    Button(window3, text=" Text2Text Generation", image=img18, width=198, height=30, compound="left", command=back_window).place(x=250, y=250)

    img19 = Image.open('Icon5.png')
    img19 = img19.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img19 = ImageTk.PhotoImage(img19)
    Button(window3, text=" Text Generation", image=img19, width=198, height=30, compound="left", command=back_window).place(x=30, y=300)

    img20 = Image.open('Icon5.png')
    img20 = img20.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img20 = ImageTk.PhotoImage(img20)
    Button(window3, text=" Conversational", image=img20, width=198, height=30, compound="left", command=back_window).place(x=250, y=300)

    img21 = Image.open('Icon6.png')
    img21 = img21.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img21 = ImageTk.PhotoImage(img21)
    Button(window3, text=" Table Question Answering", image=img21, width=198, height=30, compound="left", command=back_window).place(x=30, y=350)


    if(window3):
        window1.withdraw()

    window3.mainloop()

def back_window2():
    window1.iconify()
    window1.deiconify()
    window3.destroy()

def back_window():
    window1.iconify()
    window1.deiconify()
    window2.destroy()

window1()