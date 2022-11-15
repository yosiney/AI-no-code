from tkinter import *
from tkinter import Tk, Button
from PIL import Image,ImageTk

def window1():
    global window1
    window1 = Tk() # create window
    window1.geometry("800x500+500+200") # window dimension
    window1.title("AI no code")

    bg = PhotoImage(file = 'Icons/font.png') 
    backgraund = Label( window1, image = bg )
    backgraund.place(x = 0, y = 0) 

    img = Image.open('Icons/IMAGE-ICON.png')
    img = img.resize((100, 88), Image.ANTIALIAS) # Resize (Height, Width)
    img = ImageTk.PhotoImage(img)
    Button(window1, text="Image",image=img, width=100, height=100, compound="top", command=window2).place(x=220, y=200)

    img2 = Image.open('Icons/NLP-ICON.png')
    img2 = img2.resize((100,85), Image.ANTIALIAS) # Resize (Height, Width)
    img2 = ImageTk.PhotoImage(img2)
    Button(window1, text="NLP", image=img2, width=100, height=100, compound="top", command=window3).place(x=420, y=200)

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
#---------------------------------------------------------------------------------
def window2():
    global window2
    window2 = Toplevel(window1) # create a next window from window1
    window2.geometry("800x500+500+200")
    window2.title("AI no code")

    Button(window2, text="Back to main", width=10, command=back_window).place(x=0, rely=0)

    img3 = Image.open('Icons/Icon1.png')
    img3 = img3.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img3 = ImageTk.PhotoImage(img3)
    Button(window2, text=" Image classification",image=img3, width=198, height=30, compound="left", command=raiz).place(x=30, y=50)

    img4 = Image.open('Icons/Icon2.png')
    img4 = img4.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img4 = ImageTk.PhotoImage(img4)
    Button(window2, text=" Image Segmentation", image=img4, width=198, height=30, compound="left", command=raiz).place(x=260, y=50)

    img5 = Image.open('Icons/Icon3.png')
    img5 = img5.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img5 = ImageTk.PhotoImage(img5)
    Button(window2, text=" Zero-shot Image Classification", image=img5, width=198, height=30, compound="left", command=raiz).place(x=30, y=100)

    img6 = Image.open('Icons/Icon4.png')
    img6 = img6.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img6 = ImageTk.PhotoImage(img6)
    Button(window2, text=" Image-to-image", image=img6, width=198, height=30, compound="left", command=back_window).place(x=30, y=150)

    img7 = Image.open('Icons/Icon5.png')
    img7 = img7.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img7 = ImageTk.PhotoImage(img7)
    Button(window2, text=" Unconditional Image Generation", image=img7, width=198, height=30, compound="left", command=back_window).place(x=30, y=190)
    
    img8 = Image.open('Icons/Icon6.png')
    img8 = img8.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img8 = ImageTk.PhotoImage(img8)
    Button(window2, text=" OBject Detection", image=img8, width=198, height=30, compound="left", command=back_window).place(x=30, y=230)

    img9 = Image.open('Icons/Icon7.png')
    img9 = img9.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img9 = ImageTk.PhotoImage(img9)
    Button(window2, text=" Video Classification", image=img9, width=198, height=30, compound="left", command=back_window).place(x=260, y=230)
    
    if(window2):
        window1.withdraw()

    window2.mainloop()
#------------------------------------------------------------------------------------------------------------------
def window3():
    global window3
    window3 = Toplevel(window1) # create a next window from window1
    window3.geometry("800x500+500+200")
    window3.title("AI no code")

    Button(window3, text="Back to main", width=10, command=back_window2).place(x=0, rely=0)

    img10 = Image.open('Icons/Icon1.png')
    img10 = img10.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img10 = ImageTk.PhotoImage(img10)
    Button(window3, text=" Traslation",image=img10, width=198, height=30, compound="left", command=raiz).place(x=30, y=50)

    img11 = Image.open('Icons/Icon7.png')
    img11 = img11.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img11 = ImageTk.PhotoImage(img11)
    Button(window3, text=" Fill-Mask", image=img11, width=198, height=30, compound="left", command=back_window2).place(x=250, y=50)

    img12 = Image.open('Icons/Icon2.png')
    img12 = img12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img12 = ImageTk.PhotoImage(img12)
    Button(window3, text=" Token Classification", image=img12, width=198, height=30, compound="left", command=back_window2).place(x=30, y=100)

    img13 = Image.open('Icons/Icon7.png')
    img13 = img13.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img13 = ImageTk.PhotoImage(img13)
    Button(window3, text=" Sentence Similarity", image=img13, width=198, height=30, compound="left", command=back_window2).place(x=250, y=100)

    img14 = Image.open('Icons/Icon4.png')
    img14 = img14.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img14 = ImageTk.PhotoImage(img14)
    Button(window3, text=" Question Answering", image=img14, width=198, height=30, compound="left", command=back_window2).place(x=30, y=150)

    img15 = Image.open('Icons/Icon3.png')
    img15 = img15.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img15 = ImageTk.PhotoImage(img15)
    Button(window3, text=" Summarization", image=img15, width=198, height=30, compound="left", command=back_window2).place(x=250, y=150)

    img16 = Image.open('Icons/Icon4.png')
    img16 = img16.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img16 = ImageTk.PhotoImage(img16)
    Button(window3, text=" Zero-Shot-Classification", image=img16, width=198, height=30, compound="left", command=back_window2).place(x=30, y=200)

    img17 = Image.open('Icons/Icon1.png')
    img17 = img17.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img17 = ImageTk.PhotoImage(img17)
    Button(window3, text=" Text Classification", image=img17, width=198, height=30, compound="left", command=back_window2).place(x=30, y=250)

    img18 = Image.open('Icons/Icon6.png')
    img18 = img18.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img18 = ImageTk.PhotoImage(img18)
    Button(window3, text=" Text2Text Generation", image=img18, width=198, height=30, compound="left", command=back_window2).place(x=250, y=250)

    img19 = Image.open('Icons/Icon5.png')
    img19 = img19.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img19 = ImageTk.PhotoImage(img19)
    Button(window3, text=" Text Generation", image=img19, width=198, height=30, compound="left", command=back_window2).place(x=30, y=300)

    img20 = Image.open('Icons/Icon1.png')
    img20 = img20.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img20 = ImageTk.PhotoImage(img20)
    Button(window3, text=" Conversational", image=img20, width=198, height=30, compound="left", command=back_window2).place(x=250, y=300)

    img21 = Image.open('Icons/Icon1.png')
    img21 = img21.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img21 = ImageTk.PhotoImage(img21)
    Button(window3, text=" Table Question Answering", image=img21, width=198, height=30, compound="left", command=back_window2).place(x=30, y=350)


    if(window3):
        window1.withdraw()

    window3.mainloop()

#------------------------------------------------------------------------------------



def raiz():

    global raiz
    raiz = Toplevel(window2) # create a next window from window2
    raiz.geometry("1300x500+500+200")
    
    Button(raiz, text="Back to Image", width=12, command=back_window3).place(x=0, rely=0)

    def Delete_or_show():
     if b.place_info() != {}:
            b.place_forget()
     else:
        b.place(x=380, y=60)

    img00 = Image.open('Icons/Icon00.png')
    img00 = img00.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img00 = ImageTk.PhotoImage(img00)
    l = Button(raiz, text="microsoft/beit-base-patch16-224-pt22k-ft22k", image=img00, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    b = Label(raiz, text=" BEiT (base-sized model, fine-tuned on ImageNet-22k)  \n \n Beit model pre-trained a self-supervised fashion on ImageNet-22k -also \n called ImageNet-22k (14 million images, 21,841 classes) at revolution 224x224, \n and fine-tuned on the same desaset at resolution 224x224. it was introduced in the \n paper BEIT: BERT PRE-Training of image Transformers by Hangbo bao, li dong \n and Furu Wei and first relased in this repository. \n \n Disclamer: The team releasing BeiT did not write a model card for this \n model so this model card has been written by the Hugging  Face team")
    b.config(bg="white") #Change backgraund color
    b.config(font=('arial', 11)) #Change type and size of font
    b.config(justify=LEFT)
    b.config(fg="gray") #Change text color
    b.place_forget()

    def Delete_or_show():
     if a.place_info() != {}:
            a.place_forget()
     else:
        a.place(x=380, y=60)

    img01 = Image.open('Icons/Icon01.png')
    img01 = img01.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img01 = ImageTk.PhotoImage(img01)
    le = Button(raiz, text="google/vit-base-patch16-224", image=img01, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=110)
    a = Label(raiz, text=" Vision Transformer (base-sized model) \n \n Vision Transformer (ViT) model pre-trained on ImageNet-21k \n (14 million images, 21,843 classes) at resolution 224x224, and fine-tuned \n on ImageNet 2012 (1 million images, 1,000 classes) at resolution 384x384. It was introduced in the paper \n An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale by Dosovitskiy et al. \n and first released in this repository. However, the weights were converted from the timm repository \n by Ross Wightman, who already converted the weights from JAX to PyTorch. Credits go to him.")
    a.config(bg="white") #Change backgraund color
    a.config(font=('arial', 11)) #Change type and size of font
    a.config(justify=LEFT)
    a.config(fg="gray") #Change text color
    a.place_forget()
    
    def Delete_or_show():
     if c.place_info() != {}:
            c.place_forget()
     else:
        c.place(x=380, y=60)

    img02 = Image.open('Icons/Icon01.png')
    img02 = img02.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img02 = ImageTk.PhotoImage(img02)
    q = Button(raiz, text="google/vit-base-patch16-384", image=img02, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=160)
    c = Label(raiz, text=" Vision Transformer (base-sized model) \n \n Vision Transformer (ViT) model pre-trained on ImageNet-21k (14 million images, 21,843 classes) \n at resolution 224x224, and fine-tuned on ImageNet 2012 (1 million images, 1,000 classes) at resolution 384x384. \n It was introduced in the paper An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale by \n Dosovitskiy et al. and first released in this repository. However, the weights were converted from the timm repository \n by Ross Wightman, who already converted the weights from JAX to PyTorch. Credits go to him.")
    c.config(bg="white") #Change backgraund color
    c.config(font=('arial', 11)) #Change type and size of font
    c.config(justify=LEFT)
    c.config(fg="gray") #Change text color
    c.place_forget()
    

    def Delete_or_show():
     if d.place_info() != {}:
            d.place_forget()
     else:
        d.place(x=380, y=60)

    img03 = Image.open('Icons/Icon00.png')
    img03 = img03.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img03 = ImageTk.PhotoImage(img03)
    t = Button(raiz, text="microsoft/swin-large-patch4-window12-384-in22k", image=img03, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=210)
    d = Label(raiz, text=" Swin Transformer (large-sized model) \n \n Swin Transformer model pre-trained on ImageNet-21k (14 million images, 21,841 classes) at resolution 384x384. \n It was introduced in the paper Swin Transformer: Hierarchical Vision \n Transformer using Shifted Windows by Liu et al. and first released in this repository. \n \n Disclaimer: The team releasing Swin Transformer did not write \n a model card for this model so this model card has been written by the Hugging Face team.")
    d.config(bg="white") #Change backgraund color
    d.config(font=('arial', 11)) #Change type and size of font
    d.config(justify=LEFT)
    d.config(fg="gray") #Change text color
    d.place_forget()


    def Delete_or_show():
     if e.place_info() != {}:
            e.place_forget()
     else:
        e.place(x=380, y=60)

    img04 = Image.open('Icons/Icon00.png')
    img04 = img04.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img04 = ImageTk.PhotoImage(img04)
    r = Button(raiz, text="microsoft/resnet-50", image=img04, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=260)
    e = Label(raiz, text=" ResNet-50 v1.5 \n \n ResNet model pre-trained on ImageNet-1k at resolution 224x224. \n It was introduced in the paper Deep Residual Learning for Image Recognition by He et al. \n \n Disclaimer: The team releasing ResNet did not write a model card for this model \n so this model card has been written by the Hugging Face team.")
    e.config(bg="white") #Change backgraund color
    e.config(font=('arial', 11)) #Change type and size of font
    e.config(justify=LEFT)
    e.config(fg="gray") #Change text color
    e.place_forget()
    

    if(raiz):
        window2.withdraw()
    

    raiz.mainloop()

def back_window3():
    window2.iconify()
    window2.deiconify()
    raiz.destroy()

def back_window2():
    window1.iconify()
    window1.deiconify()
    window3.destroy()

def back_window():
    window1.iconify()
    window1.deiconify()
    window2.destroy()

window1()