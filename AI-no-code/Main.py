from tkinter import *
from tkinter import Tk, Button
from PIL import Image,ImageTk




#---------------------------------------Main--------------------------------------------------------------------------
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
#---------------------------------------Image------------------------------------------------------------------
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
    Button(window2, text=" Image Segmentation", image=img4, width=198, height=30, compound="left", command=image_segme).place(x=260, y=50)

    img5 = Image.open('Icons/Icon3.png')
    img5 = img5.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img5 = ImageTk.PhotoImage(img5)
    Button(window2, text=" Zero-shot Image Classification", image=img5, width=198, height=30, compound="left", command=back_window2).place(x=30, y=100)

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
#---------------------------------------NLP------------------------------------------------------------------------------
def window3():
    global window3
    window3 = Toplevel(window1) # create a next window from window1
    window3.geometry("800x500+500+200")
    window3.title("AI no code")

    Button(window3, text="Back to main", width=10, command=back_window2).place(x=0, rely=0)

    img10 = Image.open('Icons/Icon1.png')
    img10 = img10.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img10 = ImageTk.PhotoImage(img10)
    Button(window3, text=" Traslation",image=img10, width=198, height=30, compound="left", command=traslation).place(x=30, y=50)

    img11 = Image.open('Icons/Icon7.png')
    img11 = img11.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img11 = ImageTk.PhotoImage(img11)
    Button(window3, text=" Fill-Mask", image=img11, width=198, height=30, compound="left", command=fill).place(x=250, y=50)

    img12 = Image.open('Icons/Icon2.png')
    img12 = img12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img12 = ImageTk.PhotoImage(img12)
    Button(window3, text=" Token Classification", image=img12, width=198, height=30, compound="left", command=token_cla).place(x=30, y=100)

    img13 = Image.open('Icons/Icon7.png')
    img13 = img13.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img13 = ImageTk.PhotoImage(img13)
    Button(window3, text=" Sentence Similarity", image=img13, width=198, height=30, compound="left", command=sentece).place(x=250, y=100)

    img14 = Image.open('Icons/Icon4.png')
    img14 = img14.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img14 = ImageTk.PhotoImage(img14)
    Button(window3, text=" Question Answering", image=img14, width=198, height=30, compound="left", command=question).place(x=30, y=150)

    img15 = Image.open('Icons/Icon3.png')
    img15 = img15.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img15 = ImageTk.PhotoImage(img15)
    Button(window3, text=" Summarization", image=img15, width=198, height=30, compound="left", command=summarization).place(x=250, y=150)

    img16 = Image.open('Icons/Icon4.png')
    img16 = img16.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img16 = ImageTk.PhotoImage(img16)
    Button(window3, text=" Zero-Shot-Classification", image=img16, width=198, height=30, compound="left", command=zero_text).place(x=30, y=200)

    img17 = Image.open('Icons/Icon1.png')
    img17 = img17.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img17 = ImageTk.PhotoImage(img17)
    Button(window3, text=" Text Classification", image=img17, width=198, height=30, compound="left", command=text_clasif).place(x=30, y=250)

    img18 = Image.open('Icons/Icon6.png')
    img18 = img18.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img18 = ImageTk.PhotoImage(img18)
    Button(window3, text=" Text2Text Generation", image=img18, width=198, height=30, compound="left", command=back_window2).place(x=250, y=250)

    img19 = Image.open('Icons/Icon5.png')
    img19 = img19.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img19 = ImageTk.PhotoImage(img19)
    Button(window3, text=" Text Generation", image=img19, width=198, height=30, compound="left", command=text_genera).place(x=30, y=300)

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

#-----------------------------------image-----------------------------------------------
#-----------------------------image classification----------------------------------------


def raiz():

    global raiz
    raiz = Toplevel(window2) # create a next window from window2
    raiz.geometry("1300x500+500+200")
    
    Button(raiz, text="Back to Image", width=12, command=back_window3).place(x=0, rely=0)

    imgg = Image.open('Icons/1.png')
    imgg = imgg.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imgg = ImageTk.PhotoImage(imgg)
    cias = Button(raiz, text="Test", image=imgg, width=300, height=30, compound="left", command=test ).place(x=600, y=400)
    
    #-----------------------------microsoft/beit-base-patch16-224-pt22k-ft22k----------------------------------------
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



    #--------------------------------------google/vit-base-patch16-224---------------------------------------------------------------

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
    
    #--------------------------------------google/vit-base-patch16-384---------------------------------------------------------------

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
    
    #--------------------------------------microsoft/swin-large-patch4-window12-384-in22k---------------------------------------------------------------

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

    #--------------------------------------microsoft/resnet-50---------------------------------------------------------------

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



#--------------------------------image semegtation-----------------------------
#-----------------------------------image--------------------------------------

def image_segme():

    global image_segme
    image_segme = Toplevel(window2) # create a next window from window2
    image_segme.geometry("1300x600+500+200")
    
    Button(image_segme, text="Back to Image", width=12, command=segmeg_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(image_segme, text="Test", image=imggz, width=300, height=30, compound="left", command=test ).place(x=600, y=400)

    #--------------------------nvidia/segformer-b0-finetuned-ade-512-512-----------------

    def Delete_or_show():
     if pe.place_info() != {}:
            pe.place_forget() 
     else:
        pe.place(x=380, y=60)

    cr = Image.open('Icons/nvidia.png')
    cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    cr = ImageTk.PhotoImage(cr)

    l = Button(image_segme, text=" nvidia/segformer-b0-finetuned-ade-512-512", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    pe = Label(image_segme, text=" SegFormer (b0-sized) model fine-tuned on ADE20k \n \n SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper SegFormer: Simple \n and Efficient Design for Semantic Segmentation with Transformers by Xie et al. and first released in this repository. \n\nDisclaimer: The team releasing SegFormer did not write a model card for this model so \n this model card has been written by the Hugging Face team.")
    pe.config(bg="white") #Change backgraund color
    pe.config(font=('arial', 11)) #Change type and size of font
    pe.config(justify=LEFT)
    pe.config(fg="gray") #Change text color
    pe.place_forget()


    #--------------------------facebook/detr-resnet-50-panoptic-----------------

    def Delete_or_show():
     if pri.place_info() != {}:
            pri.place_forget() 
     else:
        pri.place(x=380, y=60)

    rc = Image.open('Icons/facebook.png')
    rc = rc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rc = ImageTk.PhotoImage(rc)

    l = Button(image_segme, text=" facebook/detr-resnet-50-panoptic", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    pri = Label(image_segme, text=" DETR (End-to-End Object Detection) model with ResNet-50 backbone \n\n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k annotated images). \n It was introduced in the paper End-to-End Object Detection with Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been \n written by the Hugging Face team.")
    pri.config(bg="white") #Change backgraund color
    pri.config(font=('arial', 11)) #Change type and size of font
    pri.config(justify=LEFT)
    pri.config(fg="gray") #Change text color
    pri.place_forget()

    #--------------------------facebook/maskformer-swin-tiny-ade-----------------

    def Delete_or_show():
     if gt.place_info() != {}:
            gt.place_forget() 
     else:
        gt.place(x=380, y=60)

    rcc = Image.open('Icons/facebook.png')
    rcc = rcc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rcc = ImageTk.PhotoImage(rcc)

    l = Button(image_segme, text=" facebook/maskformer-swin-tiny-ade", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    gt = Label(image_segme, text=" MaskFormer \n\n  MaskFormer model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). \n It was introduced in the paper Per-Pixel Classification is Not All You \n Need for Semantic Segmentation and first released in this repository. \n\n Disclaimer: The team releasing MaskFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
    gt.config(bg="white") #Change backgraund color
    gt.config(font=('arial', 11)) #Change type and size of font
    gt.config(justify=LEFT)
    gt.config(fg="gray") #Change text color
    gt.place_forget()
  

    #--------------------------nvidia/segformer-b1-finetuned-cityscapes-1024-1024-----------------

    def Delete_or_show():
     if gtt.place_info() != {}:
            gtt.place_forget() 
     else:
        gtt.place(x=380, y=60)

    rccl = Image.open('Icons/nvidia.png')
    rccl = rccl.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccl = ImageTk.PhotoImage(rccl)

    l = Button(image_segme, text=" nvidia/segformer-b1-finetuned-cityscapes-1024-1024", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    gtt = Label(image_segme, text=" SegFormer (b1-sized) model fine-tuned on CityScapes \n \n SegFormer model fine-tuned on CityScapes at resolution 1024x1024. It was introduced in \n the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with \n Transformers by Xie et al. and first released in this repository. \n\n Disclaimer: The team releasing SegFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
    gtt.config(bg="white") #Change backgraund color
    gtt.config(font=('arial', 11)) #Change type and size of font
    gtt.config(justify=LEFT)
    gtt.config(fg="gray") #Change text color
    gtt.place_forget()


    #--------------------------facebook/detr-resnet-101-panoptic-----------------

    def Delete_or_show():
     if gttn.place_info() != {}:
            gttn.place_forget() 
     else:
        gttn.place(x=380, y=60)

    rccln = Image.open('Icons/facebook.png')
    rccln = rccln.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccln = ImageTk.PhotoImage(rccln)

    l = Button(image_segme, text=" facebook/detr-resnet-101-panoptic", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    gttn = Label(image_segme, text=" DETR (End-to-End Object Detection) model with ResNet-101 backbone \n \n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k \n annotated images). It was introduced in the paper End-to-End Object Detection with \n Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for \n this model so this model card has been written by the Hugging Face team.")
    gttn.config(bg="white") #Change backgraund color
    gttn.config(font=('arial', 11)) #Change type and size of font
    gttn.config(justify=LEFT)
    gttn.config(fg="gray") #Change text color
    gttn.place_forget()

    if(image_segme):
        window2.withdraw()
    

    image_segme.mainloop()

    #--------------------------------image semegtation-test --------image------------------------



def test():

    global test
    test = Toplevel(window2) # create a next window from window2
    test.geometry("1300x500+500+200")
    
    Button(test, text="Back to Image", width=12, command=out_test).place(x=0, rely=0)  

    if(raiz):
        window2.withdraw()
    

    raiz.mainloop()







#---------------------------------NLP----------------------------------------------------------
#------------------------------TRASLATION---------------------------------------------------  

def traslation():

    global traslation
    traslation = Toplevel(window3) # create a next window from window2
    traslation.geometry("1300x600+500+200")
    
    Button(traslation, text="Back to Image", width=12, command=trasla_back).place(x=0, rely=0)


    #-----------------------------------t5-small----------------------------------------------

    def Delete_or_show():
     if wi.place_info() != {}:
            wi.place_forget() 
     else:
        wi.place(x=380, y=60)

    img000 = Image.open('Icons/t1.png')
    img000 = img000.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img000 = ImageTk.PhotoImage(img000)

    imgtrass = Image.open('Icons/trasla-1.png')
    imgtrass = imgtrass.resize((500, 300), Image.ANTIALIAS) # Resize (Height, Width)
    imgtrass = ImageTk.PhotoImage(imgtrass)

    l = Button(traslation, text="t5-small", image=img000, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    wi = Label(traslation, text=" Model Description \n \n The developers of the Text-To-Text Transfer Transformer (T5) write: \n \n > With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the \n input and output are always text strings, in contrast to BERT-style models that can only \n output either a class label or a span of the input. Our text-to-text framework allows us to \n use the same model, loss function, and hyperparameters on any NLP task.", image=imgtrass, compound="top")
    wi.config(bg="white") #Change backgraund color
    wi.config(font=('arial', 11)) #Change type and size of font
    wi.config(justify=LEFT)
    wi.config(fg="gray") #Change text color
    wi.place_forget()


    #-----------------------------------t5-base----------------------------------------------

    def Delete_or_show():
     if tc.place_info() != {}:
            tc.place_forget() 
     else:
        tc.place(x=380, y=60)

    img00 = Image.open('Icons/t1.png')
    img00 = img00.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img00 = ImageTk.PhotoImage(img00)

    imgtras = Image.open('Icons/trasla-1.png')
    imgtras = imgtras.resize((500, 300), Image.ANTIALIAS) # Resize (Height, Width)
    imgtras = ImageTk.PhotoImage(imgtras)

    l = Button(traslation, text="t5-base", image=img00, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    tc = Label(traslation, text=" Model Description \n \n The developers of the Text-To-Text Transfer Transformer (T5) write: \n \n > With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the \n input and output are always text strings, in contrast to BERT-style models that can only \n output either a class label or a span of the input. Our text-to-text framework allows us to \n use the same model, loss function, and hyperparameters on any NLP task.", image=imgtras, compound="top")
    tc.config(bg="white") #Change backgraund color
    tc.config(font=('arial', 11)) #Change type and size of font
    tc.config(justify=LEFT)
    tc.config(fg="gray") #Change text color
    tc.place_forget()

    #---------------------------Helsinki-NLP/opus-mt-ROMANCE-en---------------------------------------

    def Delete_or_show():
     if tcl.place_info() != {}:
            tcl.place_forget() 
     else:
        tcl.place(x=380, y=60)

    strong = Image.open('Icons/box.png')
    strong = strong.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    strong = ImageTk.PhotoImage(strong)

    l = Button(traslation, text=" Helsinki-NLP/opus-mt-ROMANCE-en", image=strong, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    tcl = Label(traslation, text= " opus-mt-ROMANCE-en \n \nsource languages: fr,fr_BE,fr_CA,fr_FR,wa,frp,oc,ca,rm,lld,fur,lij,lmo,es,\nes_AR,es_CL,es_CO,es_CR,es_DO,es_EC,es_ES,es_GT,es_HN,es_MX,es_NI,es_PA,es_PE,es_PR,es_SV,es_UY,\nes_VE,pt,pt_br,pt_BR,pt_PT,gl,lad,an,mwl,it,it_IT,co,nap,scn,vec,sc,ro,la \n\n target languages: en \n \nOPUS readme: fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR\nes_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE \nes_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la-en \n \ndataset: opus \n\n ")

    tcl.config(bg="white") #Change backgraund color
    tcl.config(font=('arial', 11)) #Change type and size of font
    tcl.config(justify=LEFT)
    tcl.config(fg="gray") #Change text color
    tcl.place_forget()
         

    #---------------------------Helsinki-NLP/opus-mt-de-en---------------------------------------

    def Delete_or_show():
     if tclo.place_info() != {}:
            tclo.place_forget() 
     else:
        tclo.place(x=380, y=60)

    strongs = Image.open('Icons/box.png')
    strongs = strongs.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    strongs = ImageTk.PhotoImage(strongs)

    l = Button(traslation, text=" Helsinki-NLP/opus-mt-de-en", image=strongs, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    tclo = Label(traslation, text= " opus-mt-de-en \n\nsource languages: de\n\ntarget languages: en\n\nOPUS readme: de-en\n\ndataset: opus\n\nmodel: transformer-align\n\npre-processing: normalization + SentencePiece\n\ndownload original weights: opus-2020-02-26.zip\n\ntest set translations: opus-2020-02-26.test.txt\n\ntest set scores: opus-2020-02-26.eval.txt")

    tclo.config(bg="white") #Change backgraund color
    tclo.config(font=('arial', 11)) #Change type and size of font
    tclo.config(justify=LEFT)
    tclo.config(fg="gray") #Change text color
    tclo.place_forget()

    #---------------------------Helsinki-NLP/opus-mt-fr-en---------------------------------------


    def Delete_or_show():
     if tcz.place_info() != {}:
            tcz.place_forget() 
     else:
        tcz.place(x=380, y=60)

    str = Image.open('Icons/box.png')
    str = str.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    str = ImageTk.PhotoImage(str)

    l = Button(traslation, text=" Helsinki-NLP/opus-mt-fr-en", image=str, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    tcz = Label(traslation, text= " opus-mt-fr-en \n\nsource languages: fr\n\ntarget languages: en\n\nOPUS readme: fr-en\n\ndataset: opus\n\nmodel: transformer-align\n\npre-processing: normalization + SentencePiece\n\ndownload original weights: opus-2020-02-26.zip\n\ntest set translations: opus-2020-02-26.test.txt\n\ntest set scores: opus-2020-02-26.eval.txt")

    tcz.config(bg="white") #Change backgraund color
    tcz.config(font=('arial', 11)) #Change type and size of font
    tcz.config(justify=LEFT)
    tcz.config(fg="gray") #Change text color
    tcz.place_forget()

    if(traslation):
        window3.withdraw()
    

    traslation.mainloop()


#-----------------------------------fill-Mask--------------------------------------------------

def fill():

    global fill
    fill = Toplevel(window3) # create a next window from window2
    fill.geometry("1300x600+500+200")
    
    Button(fill, text="Back to Image", width=12, command=fill_back).place(x=0, rely=0)


    #-----------------------------------bert-base-uncased--------------------------------------------------

    def Delete_or_show():
     if zz.place_info() != {}:
            zz.place_forget() 
     else:
        zz.place(x=380, y=60)

    zzl = Image.open('Icons/box.png')
    zzl = zzl.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zzl = ImageTk.PhotoImage(zzl)

    l = Button(fill, text=" bert-base-uncased", image=zzl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    zz = Label(fill, text= " BERT base model (uncased) \n\n Pretrained model on English language using a masked language modeling (MLM) \n objective. It was introduced in this paper and first released in this repository. This model \n is uncased: it does not make a difference between english and English. \n\n Disclaimer: The team releasing BERT did not write a model card for this model so this \n model card has been written by the Hugging Face team.")

    zz.config(bg="white") #Change backgraund color
    zz.config(font=('arial', 11)) #Change type and size of font
    zz.config(justify=LEFT)
    zz.config(fg="gray") #Change text color
    zz.place_forget()

    #-----------------------------------xlm-roberta-base-----------------------------------------------------

    def Delete_or_show():
     if zu.place_info() != {}:
            zu.place_forget() 
     else:
        zu.place(x=380, y=60)

    zul = Image.open('Icons/box.png')
    zul = zul.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zul = ImageTk.PhotoImage(zul)

    l = Button(fill, text=" xlm-roberta-base", image=zul, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    zu = Label(fill, text= " XLM-RoBERTa (base-sized model) \n\n XLM-RoBERTa model pre-trained on 2.5TB of filtered CommonCrawl data containing 100 \n languages. It was introduced in the paper Unsupervised Cross-lingual Representation \n Learning at Scale by Conneau et al. and first released in this repository. \n\n Disclaimer: The team releasing XLM-RoBERTa did not write a model card for this model \n so this model card has been written by the Hugging Face team.")

    zu.config(bg="white") #Change backgraund color
    zu.config(font=('arial', 11)) #Change type and size of font
    zu.config(justify=LEFT)
    zu.config(fg="gray") #Change text color
    zu.place_forget()

    #-----------------------------------roberta-base-----------------------------------------------------

    def Delete_or_show():
     if uu.place_info() != {}:
            uu.place_forget() 
     else:
        uu.place(x=380, y=60)

    zull = Image.open('Icons/box.png')
    zull = zull.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zull = ImageTk.PhotoImage(zull)

    l = Button(fill, text=" roberta-base", image=zull, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    uu = Label(fill, text= " XLM-RoBERTa (base-sized model) \n\n XLM-RoBERTa model pre-trained on 2.5TB of filtered CommonCrawl data containing 100 \n languages. It was introduced in the paper Unsupervised Cross-lingual Representation \n Learning at Scale by Conneau et al. and first released in this repository. \n\n Disclaimer: The team releasing XLM-RoBERTa did not write a model card for this model \n so this model card has been written by the Hugging Face team.")

    uu.config(bg="white") #Change backgraund color
    uu.config(font=('arial', 11)) #Change type and size of font
    uu.config(justify=LEFT)
    uu.config(fg="gray") #Change text color
    uu.place_forget()

    #-----------------------------------bert-base-multilingual-cased-----------------------------------------------------

    def Delete_or_show():
     if ut.place_info() != {}:
            ut.place_forget() 
     else:
        ut.place(x=380, y=60)

    zulli = Image.open('Icons/box.png')
    zulli = zulli.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zulli = ImageTk.PhotoImage(zulli)

    l = Button(fill, text=" bert-base-multilingual-cased", image=zulli, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    ut = Label(fill, text= " BERT multilingual base model (cased) \n\n Pretrained model on the top 104 languages with the largest Wikipedia using a masked \n language modeling (MLM) objective. It was introduced in this paper and first released in \n  this repository. This model is case sensitive: it makes a difference between english and English. \n\n Disclaimer: The team releasing BERT did not write a model card for this model so this \n  model card has been written by the Hugging Face team.")

    ut.config(bg="white") #Change backgraund color
    ut.config(font=('arial', 11)) #Change type and size of font
    ut.config(justify=LEFT)
    ut.config(fg="gray") #Change text color
    ut.place_forget()


    #-----------------------------------distilbert-base-uncased-----------------------------------------------------

    def Delete_or_show():
     if utt.place_info() != {}:
            utt.place_forget() 
     else:
        utt.place(x=380, y=60)

    zulliz = Image.open('Icons/box.png')
    zulliz = zulliz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zulliz = ImageTk.PhotoImage(zulliz)

    l = Button(fill, text=" distilbert-base-uncased", image=zulliz, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    utt = Label(fill, text= " DistilBERT base model (uncased) \n\n This model is a distilled version of the BERT base model. It was introduced in this paper. \n The code for the distillation process can be found here. This model is uncased: it does not  \n make a difference between english and English.")

    utt.config(bg="white") #Change backgraund color
    utt.config(font=('arial', 11)) #Change type and size of font
    utt.config(justify=LEFT)
    utt.config(fg="gray") #Change text color
    utt.place_forget()

    if(fill):
        window3.withdraw()
    
    fill.mainloop()

                                         #-------------------------------
#-----------------------------------------------Token Classification---------------------------------------------------
                                         #-------------------------------


def token_cla():

    global token_cla
    token_cla = Toplevel(window3) # create a next window from window2
    token_cla.geometry("1300x600+500+200")
    
    Button(token_cla, text="Back to Image", width=12, command=token_back).place(x=0, rely=0)

    def Delete_or_show():
     if QQ.place_info() != {}:
            QQ.place_forget() 
     else:
        QQ.place(x=440, y=60)

    zq = Image.open('Icons/box.png')
    zq = zq.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zq = ImageTk.PhotoImage(zq)

    l = Button(token_cla, text=" Jean-Baptiste/camembert-ner", image=zq, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    QQ = Label(token_cla, text= "camembert-ner: model fine-tuned from camemBERT for NER task. \n\n Introduction \n\n [camembert-ner] is a NER model that was fine-tuned from camemBERT on wikiner-fr \n dataset. Model was trained on wikiner-fr dataset (~170 634 sentences). Model was \n validated on emails/chat data and overperformed other models on this type of data \n specifically. In particular the model seems to work better on entity that don't start with \n an upper case.")

    QQ.config(bg="white") #Change backgraund color
    QQ.config(font=('arial', 11)) #Change type and size of font
    QQ.config(justify=LEFT)
    QQ.config(fg="gray") #Change text color
    QQ.place_forget()

    #---------------------------------------dslim/bert-base-NER-----------------------------------------------------
    def Delete_or_show():
     if QQq.place_info() != {}:
            QQq.place_forget() 
     else:
        QQq.place(x=440, y=60)

    zqq = Image.open('Icons/box.png')
    zqq = zqq.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zqq = ImageTk.PhotoImage(zqq)

    l = Button(token_cla, text=" dslim/bert-base-NER", image=zqq, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    QQq = Label(token_cla, text= " bert-base-NER \n\n Model description \n\n bert-base-NER is a fine-tuned BERT model that is ready to use for Named Entity \n Recognition and achieves state-of-the-art performance for the NER task. It has been \n trained to recognize four types of entities: location (LOC), organizations (ORG), person \n (PER) and Miscellaneous (MISC). \n\n Specifically, this model is a bert-base-cased model that was fine-tuned on the English \n version of the standard CoNLL-2003 Named Entity Recognition dataset. \n \n If you'd like to use a larger BERT-large model fine-tuned on the same dataset, \n a bert-large-NER version is also available.")

    QQq.config(bg="white") #Change backgraund color
    QQq.config(font=('arial', 11)) #Change type and size of font
    QQq.config(justify=LEFT)
    QQq.config(fg="gray") #Change text color
    QQq.place_forget()

    #---------------------------------------xlm-roberta-large-finetuned-conll03-english-----------------------------------------------------
    def Delete_or_show():
     if q1.place_info() != {}:
            q1.place_forget() 
     else:
        q1.place(x=440, y=60)

    z2 = Image.open('Icons/box.png')
    z2 = z2.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    z2 = ImageTk.PhotoImage(z2)

    l = Button(token_cla, text=" xlm-roberta-large-finetuned-conll03-english", image=z2, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    q1 = Label(token_cla, text= " Model Description \n\n The XLM-RoBERTa model was proposed in Unsupervised Cross-lingual Representation \n Learning at Scale by Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav \n Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke \n Zettlemoyer and Veselin Stoyanov. It is based on Facebook's RoBERTa model released in \n 2019. It is a large multi-lingual language model, trained on 2.5TB of filtered CommonCrawl data.\n  This model is XLM-RoBERTa-large fine-tuned with the conll2003 dataset in English.")

    q1.config(bg="white") #Change backgraund color
    q1.config(font=('arial', 11)) #Change type and size of font
    q1.config(justify=LEFT)
    q1.config(fg="gray") #Change text color
    q1.place_forget()


    #---------------------------------------oliverguhr/fullstop-punctuation-multilang-large-----------------------------------------------------

    def Delete_or_show():
     if qw1.place_info() != {}:
            qw1.place_forget() 
     else:
        qw1.place(x=440, y=60)

    zq2 = Image.open('Icons/box.png')
    zq2 = zq2.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zq2 = ImageTk.PhotoImage(zq2)

    l = Button(token_cla, text=" oliverguhr/fullstop-punctuation-multilang-large", image=zq2, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    qw1 = Label(token_cla, text= " This model predicts the punctuation of English, Italian, French and German texts. We developed \n it to restore the punctuation of transcribed spoken language.\n\n This multilanguage model was trained on the Europarl Dataset provided by the SEPP-NLG \n Shared Task. Please note that this dataset consists of political speeches.\n Therefore the model might perform differently on texts from other domains.\n\n The model restores the following punctuation markers: "", . ? - :"" ")

    qw1.config(bg="white") #Change backgraund color
    qw1.config(font=('arial', 11)) #Change type and size of font
    qw1.config(justify=LEFT)
    qw1.config(fg="gray") #Change text color
    qw1.place_forget()


    #---------------------------------------dslim/bert-large-NER-----------------------------------------------------

    def Delete_or_show():
     if qw12.place_info() != {}:
            qw12.place_forget() 
     else:
        qw12.place(x=440, y=60)

    zq22 = Image.open('Icons/box.png')
    zq22 = zq22.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zq22 = ImageTk.PhotoImage(zq22)

    l = Button(token_cla, text=" dslim/bert-large-NER", image=zq22, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    qw12 = Label(token_cla, text= " bert-base-NER  \n\n Model description \n\nbert-large-NER is a fine-tuned BERT model that is ready to use for Named Entity \n Recognition and achieves state-of-the-art performance for the NER task. It has been \n trained to recognize four types of entities: location (LOC), organizations (ORG), person \n (PER) and Miscellaneous (MISC).\n\n Specifically, this model is a bert-large-cased model that was fine-tuned on the English \n version of the standard CoNLL-2003 Named Entity Recognition dataset.\n\n If you'd like to use a smaller BERT model fine-tuned on the same dataset, a bert-base-NER version is also available.")

    qw12.config(bg="white") #Change backgraund color
    qw12.config(font=('arial', 11)) #Change type and size of font
    qw12.config(justify=LEFT)
    qw12.config(fg="gray") #Change text color
    qw12.place_forget()


    if(token_cla):
        window3.withdraw()
    
    token_cla.mainloop()


                                             #-------------------------------
#-----------------------------------------------sentence Similarity---------------------------------------------------
                                             #-------------------------------


def sentece():

    global sentece
    sentece = Toplevel(window3) # create a next window from window2
    sentece.geometry("1300x600+500+200")
    
    Button(sentece, text="Back to Image", width=12, command=sentece_back).place(x=0, rely=0)

    #-----------------------------------------------sentence-transformers/all-MiniLM-L6-v2---------------------------------------------------

    def Delete_or_show():
     if a21.place_info() != {}:
            a21.place_forget() 
     else:
        a21.place(x=440, y=60)

    zq221 = Image.open('Icons/box.png')
    zq221 = zq221.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zq221 = ImageTk.PhotoImage(zq221)

    l = Button(sentece, text=" sentence-transformers/all-MiniLM-L6-v2", image=zq221, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    a21 = Label(sentece, text= " all-MiniLM-L6-v2 \n\n This is a sentence-transformers model: It maps sentences & paragraphs to a 384 \n dimensional dense vector space and can be used for tasks like clustering \n or semantic search.")

    a21.config(bg="white") #Change backgraund color
    a21.config(font=('arial', 11)) #Change type and size of font
    a21.config(justify=LEFT)
    a21.config(fg="gray") #Change text color
    a21.place_forget()


    #-----------------------------------------------sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2---------------------------------------------------

    def Delete_or_show():
     if a211.place_info() != {}:
            a211.place_forget() 
     else:
        a211.place(x=440, y=60)

    zq2211 = Image.open('Icons/box.png')
    zq2211 = zq2211.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    zq2211 = ImageTk.PhotoImage(zq2211)

    l = Button(sentece, text=" sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", image=zq2211, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    a211 = Label(sentece, text= " sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 \n\n This is a sentence-transformers model: It maps sentences & paragraphs to a 384 \n dimensional dense vector space and can be used for tasks like clustering or semantic search. ")

    a211.config(bg="white") #Change backgraund color
    a211.config(font=('arial', 11)) #Change type and size of font
    a211.config(justify=LEFT)
    a211.config(fg="gray") #Change text color
    a211.place_forget()

    #-----------------------------------------------sentence-transformers/paraphrase-MiniLM-L6-v2---------------------------------------------------

    def Delete_or_show():
     if b2.place_info() != {}:
            b2.place_forget() 
     else:
        b2.place(x=440, y=60)

    bq = Image.open('Icons/box.png')
    bq = bq.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    bq = ImageTk.PhotoImage(bq)

    l = Button(sentece, text=" sentence-transformers/paraphrase-MiniLM-L6-v2", image=bq, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    b2 = Label(sentece, text= " sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 \n\n This is a sentence-transformers model: It maps sentences & paragraphs to a 384 \n dimensional dense vector space and can be used for tasks like clustering or semantic search. ")

    b2.config(bg="white") #Change backgraund color
    b2.config(font=('arial', 11)) #Change type and size of font
    b2.config(justify=LEFT)
    b2.config(fg="gray") #Change text color
    b2.place_forget()


    #-----------------------------------------------shibing624/text2vec-base-chinese---------------------------------------------------

    def Delete_or_show():
     if b21.place_info() != {}:
            b21.place_forget() 
     else:
        b21.place(x=440, y=60)

    bq1 = Image.open('Icons/box.png')
    bq1 = bq1.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    bq1 = ImageTk.PhotoImage(bq1)

    l = Button(sentece, text=" shibing624/text2vec-base-chinese", image=bq1, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    b21 = Label(sentece, text= " shibing624/text2vec-base-chinese \n\n This is a CoSENT(Cosine Sentence) model: shibing624/text2vec-base-chinese.\n\n It maps sentences to a 768 dimensional dense vector space and can be used for\n tasks like sentence embeddings, text matching or semantic search. ")

    b21.config(bg="white") #Change backgraund color
    b21.config(font=('arial', 11)) #Change type and size of font
    b21.config(justify=LEFT)
    b21.config(fg="gray") #Change text color
    b21.place_forget()


    #-----------------------------------------------sentence-transformers/all-MiniLM-L12-v2---------------------------------------------------

    def Delete_or_show():
     if b21q.place_info() != {}:
            b21q.place_forget() 
     else:
        b21q.place(x=440, y=60)

    bq11 = Image.open('Icons/box.png')
    bq11 = bq11.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    bq11 = ImageTk.PhotoImage(bq11)

    l = Button(sentece, text=" sentence-transformers/all-MiniLM-L12-v2", image=bq11, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    b21q = Label(sentece, text= " todo-MiniLM-L12-v2 \n \n Este es un modelo de transformadores de oraciones : asigna oraciones y párrafos a un \n espacio vectorial denso de 384 dimensiones y puede usarse para tareas \n como agrupación o búsqueda semántica.")

    b21q.config(bg="white") #Change backgraund color
    b21q.config(font=('arial', 11)) #Change type and size of font
    b21q.config(justify=LEFT)
    b21q.config(fg="gray") #Change text color
    b21q.place_forget()


    if(sentece):
        window3.withdraw()
    
    sentece.mainloop()

#                                      #---------------------------------
#-----------------------------------------------Question answering-----------------------------------------
#                                      #---------------------------------


def question():

    global question
    question = Toplevel(window3) # create a next window from window2
    question.geometry("1300x600+500+200")
    
    Button(question, text="Back to Image", width=12, command=quest_back).place(x=0, rely=0)


    #-----------------------------------------------deepset/roberta-base-squad2---------------------------------------------------

    def Delete_or_show():
     if e1.place_info() != {}:
            e1.place_forget() 
     else:
        e1.place(x=440, y=60)

    e0 = Image.open('Icons/dedsep.png')
    e0 = e0.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0 = ImageTk.PhotoImage(e0)

    l = Button(question, text=" deepset/roberta-base-squad2", image=e0, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    e1 = Label(question, text= " roberta-base for QA \n\n This is the roberta-base model, fine-tuned using the SQuAD2.0 dataset. It's been trained \n on question-answer pairs, including unanswerable questions, \n for the task of Question Answering.")

    e1.config(bg="white") #Change backgraund color
    e1.config(font=('arial', 11)) #Change type and size of font
    e1.config(justify=LEFT)
    e1.config(fg="gray") #Change text color
    e1.place_forget()

    #-----------------------------------------------bert-large-uncased-whole-word-masking-finetuned-squad---------------------------------------------------

    def Delete_or_show():
     if e1e.place_info() != {}:
            e1e.place_forget() 
     else:
        e1e.place(x=440, y=60)

    e0e = Image.open('Icons/box.png')
    e0e = e0e.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0e = ImageTk.PhotoImage(e0e)

    l = Button(question, text=" bert-large-uncased-whole-word-masking-finetuned-squad", image=e0e, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    e1e = Label(question, text= " BERT large model (uncased) whole word masking finetuned on SQuAD \n\nPretrained model on English language using a masked language modeling (MLM) \n objective. It was introduced in this paper and first released in this repository. This model \n is uncased: it does not make a difference between english and English. \n\n Differently to other BERT models, this model was trained with a new technique: Whole \n Word Masking. In this case, all of the tokens corresponding to a word are masked at once.\n The overall masking rate remains the same.")

    e1e.config(bg="white") #Change backgraund color
    e1e.config(font=('arial', 11)) #Change type and size of font
    e1e.config(justify=LEFT)
    e1e.config(fg="gray") #Change text color
    e1e.place_forget()


    #-----------------------------------------------deepset/minilm-uncased-squad2---------------------------------------------------

    def Delete_or_show():
     if e1ee.place_info() != {}:
            e1ee.place_forget() 
     else:
        e1ee.place(x=440, y=60)

    e0ee = Image.open('Icons/dedsep.png')
    e0ee = e0ee.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0ee = ImageTk.PhotoImage(e0ee)

    l = Button(question, text=" deepset/minilm-uncased-squad2", image=e0ee, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    e1ee = Label(question, text= " MiniLM-L12-H384-uncased for QA \n\nOverview\nLanguage model: microsoft/MiniLM-L12-H384-uncased\nLanguage: English\nDownstream-task: Extractive QA\nTraining data: SQuAD 2.0\nEval data: SQuAD 2.0\nCode: See example in FARM\nInfrastructure: 1x Tesla v100")

    e1ee.config(bg="white") #Change backgraund color
    e1ee.config(font=('arial', 11)) #Change type and size of font
    e1ee.config(justify=LEFT)
    e1ee.config(fg="gray") #Change text color
    e1ee.place_forget()



    #-----------------------------------------------distilbert-base-cased-distilled-squad---------------------------------------------------

    def Delete_or_show():
     if e1e1.place_info() != {}:
            e1e1.place_forget() 
     else:
        e1e1.place(x=440, y=60)

    e0z = Image.open('Icons/box.png')
    e0z = e0z.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0z = ImageTk.PhotoImage(e0z)

    l = Button(question, text=" distilbert-base-cased-distilled-squad", image=e0z, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    e1e1 = Label(question, text= " Model Details \n\n Model Description: The DistilBERT model was proposed in the blog post Smaller, faster, \n cheaper, lighter: Introducing DistilBERT, adistilled version of BERT, and the paper \n DistilBERT, adistilled version of BERT: smaller, faster, cheaper and lighter. DistilBERT is a small, fast, cheap and light Transformer model trained by distilling BERT base. It has 40% \n less parameters than bert-base-uncased, runs 60% faster while preserving over 95% of \n BERT's performances as measured on the GLUE language understanding benchmark. \n\n This model is a fine-tune checkpoint of DistilBERT-base-cased, fine-tuned using \n (a second step of) knowledge distillation on SQuAD v1.1.")

    e1e1.config(bg="white") #Change backgraund color
    e1e1.config(font=('arial', 11)) #Change type and size of font
    e1e1.config(justify=LEFT)
    e1e1.config(fg="gray") #Change text color
    e1e1.place_forget()





    #-----------------------------------------------distilbert-base-uncased-distilled-squad---------------------------------------------------

    def Delete_or_show():
     if e1p.place_info() != {}:
            e1p.place_forget() 
     else:
        e1p.place(x=440, y=60)

    e0p = Image.open('Icons/box.png')
    e0p = e0p.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0p = ImageTk.PhotoImage(e0p)

    l = Button(question, text=" deepset/roberta-base-squad2", image=e0p, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    e1p = Label(question, text= " Model Details \n\n Model Description: The DistilBERT model was proposed in the blog post Smaller, faster,\n cheaper, lighter: Introducing DistilBERT, adistilled version of BERT, and the paper \n DistilBERT, adistilled version of BERT: smaller, faster, cheaper and lighter. DistilBERT is a \n small, fast, cheap and light Transformer model trained by distilling BERT base. It has 40% \n less parameters than bert-base-uncased, runs 60""%"" faster while preserving over 95""%"" of \n BERT's performances as measured on the GLUE language understanding benchmark.")

    e1p.config(bg="white") #Change backgraund color
    e1p.config(font=('arial', 11)) #Change type and size of font
    e1p.config(justify=LEFT)
    e1p.config(fg="gray") #Change text color
    e1p.place_forget()


    if(question):
        window3.withdraw()
    
    question.mainloop()

#                                      #---------------------------------
#-------------------------------------------------------Summarization---------------------------------
#                                      #---------------------------------


def summarization():

    global summarization
    summarization = Toplevel(window3) # create a next window from window2
    summarization.geometry("1300x600+500+200")
    
    Button(summarization, text="Back to Image", width=12, command=summari_back).place(x=0, rely=0)


    #-----------------------------------------------facebook/bart-large-cnn---------------------------------------------------

    def Delete_or_show():
     if e1.place_info() != {}:
            e1.place_forget() 
     else:
        e1.place(x=440, y=60)

    e0 = Image.open('Icons/facebook.png')
    e0 = e0.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0 = ImageTk.PhotoImage(e0)

    l = Button(summarization, text=" facebook/bart-large-cnn", image=e0, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    e1 = Label(summarization, text= " BART (large-sized model), fine-tuned on CNN Daily Mail \n\n BART model pre-trained on English language, and fine-tuned on CNN Daily Mail. It was \n introduced in the paper BART: Denoising Sequence-to-Sequence Pre-training for Natural \n Language Generation, Translation, and Comprehension by Lewis et al. and first released \n in [this repository (https://github.com/pytorch/fairseq/tree/master/examples/bart). \n\n Disclaimer: The team releasing BART did not write a model card for this model \n so this model card has been written by the Hugging Face team.")

    e1.config(bg="white") #Change backgraund color
    e1.config(font=('arial', 11)) #Change type and size of font
    e1.config(justify=LEFT)
    e1.config(fg="gray") #Change text color
    e1.place_forget()

    #----------------------------------------------sshleifer/distilbart-xsum-12-3--------------------------------------------------

    def Delete_or_show():
     if e1e.place_info() != {}:
            e1e.place_forget() 
     else:
        e1e.place(x=440, y=60)

    e0e = Image.open('Icons/box.png')
    e0e = e0e.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0e = ImageTk.PhotoImage(e0e)

    l = Button(summarization, text=" sshleifer/distilbart-xsum-12-3", image=e0e, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    e1e = Label(summarization, text= " Usage\n\n This checkpoint should be loaded into BartForConditionalGeneration.from\n_pretrained. See the BART docs for more information.")
    e1e.config(bg="white") #Change backgraund color
    e1e.config(font=('arial', 11)) #Change type and size of font
    e1e.config(justify=LEFT)
    e1e.config(fg="gray") #Change text color
    e1e.place_forget()


    #---------------------------------------------------sshleifer/distilbart-cnn-12-6-------------------------------------------------------------

    def Delete_or_show():
     if e1ee.place_info() != {}:
            e1ee.place_forget() 
     else:
        e1ee.place(x=440, y=60)

    e0ee = Image.open('Icons/dedsep.png')
    e0ee = e0ee.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0ee = ImageTk.PhotoImage(e0ee)

    l = Button(summarization, text=" sshleifer/distilbart-cnn-12-6", image=e0ee, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    e1ee = Label(summarization, text= " Usage \n\n This checkpoint should be loaded into BartForConditionalGeneration.\n from_pretrained. See the BART docs for more information.")

    e1ee.config(bg="white") #Change backgraund color
    e1ee.config(font=('arial', 11)) #Change type and size of font
    e1ee.config(justify=LEFT)
    e1ee.config(fg="gray") #Change text color
    e1ee.place_forget()



    #-----------------------------------------------philschmid/bart-large-cnn-samsum--------------------------------------------------

    def Delete_or_show():
     if e1e1.place_info() != {}:
            e1e1.place_forget() 
     else:
        e1e1.place(x=440, y=60)

    e0z = Image.open('Icons/box.png')
    e0z = e0z.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0z = ImageTk.PhotoImage(e0z)

    l = Button(summarization, text=" philschmid/bart-large-cnn-samsum", image=e0z, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    e1e1 = Label(summarization, text= " bart-large-cnn-samsum  \n\n This model was trained using Amazon SageMaker and the new \n Hugging Face Deep Learning container.")

    e1e1.config(bg="white") #Change backgraund color
    e1e1.config(font=('arial', 11)) #Change type and size of font
    e1e1.config(justify=LEFT)
    e1e1.config(fg="gray") #Change text color
    e1e1.place_forget()





    #-----------------------------------------------google/pegasus-xsum---------------------------------------------------

    def Delete_or_show():
     if e1p.place_info() != {}:
            e1p.place_forget() 
     else:
        e1p.place(x=440, y=60)

    e0p = Image.open('Icons/icon01.png')
    e0p = e0p.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0p = ImageTk.PhotoImage(e0p)

    l = Button(summarization, text=" dgoogle/pegasus-xsum", image=e0p, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    e1p = Label(summarization, text= " The following is copied from the authors' README \n\n Mixed & Stochastic Checkpoints\n\n We train a pegasus model with sampled gap sentence ratios on both C4 and HugeNews, \n and stochastically sample important sentences. The updated the results are \nreported in this table.")

    e1p.config(bg="white") #Change backgraund color
    e1p.config(font=('arial', 11)) #Change type and size of font
    e1p.config(justify=LEFT)
    e1p.config(fg="gray") #Change text color
    e1p.place_forget()


    if(summarization):
        window3.withdraw()
    
    summarization.mainloop()


#                                      #---------------------------------
#----------------------------------------------text classification---------------------------------
#                                      #---------------------------------


def text_clasif():

    global text_clasif
    text_clasif = Toplevel(window3) # create a next window from window2
    text_clasif.geometry("1300x600+500+200")
    
    Button(text_clasif, text="Back to Image", width=12, command=text_cla_back).place(x=0, rely=0)


    #-----------------------------------------------distilbert-base-uncased-finetuned-sst-2-english--------------------------------------------------

    def Delete_or_show():
     if e1.place_info() != {}:
            e1.place_forget() 
     else:
        e1.place(x=440, y=60)

    e0 = Image.open('Icons/box.png')
    e0 = e0.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0 = ImageTk.PhotoImage(e0)

    l = Button(text_clasif, text=" distilbert-base-uncased-finetuned-sst-2-english", image=e0, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    e1 = Label(text_clasif, text= " Model Details \n\n Model Description: This model is a fine-tune checkpoint of DistilBERT-base-uncased, \n fine-tuned on SST-2. This model reaches an accuracy of 91.3 on the dev set (for \n comparison, Bert bert-base-uncased version reaches an accuracy of 92.7).")

    e1.config(bg="white") #Change backgraund color
    e1.config(font=('arial', 11)) #Change type and size of font
    e1.config(justify=LEFT)
    e1.config(fg="gray") #Change text color
    e1.place_forget()

    #----------------------------------------------cardiffnlp/twitter-roberta-base-sentiment--------------------------------------------------

    def Delete_or_show():
     if e1e.place_info() != {}:
            e1e.place_forget() 
     else:
        e1e.place(x=440, y=60)

    e0e = Image.open('Icons/box.png')
    e0e = e0e.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0e = ImageTk.PhotoImage(e0e)

    l = Button(text_clasif, text=" sshleifer/distilbart-xsum-12-3", image=e0e, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    e1e = Label(text_clasif, text= "Twitter-roBERTa-base for Sentiment Analysis \n\n This is a roBERTa-base model trained on ~58M tweets and finetuned for sentiment \n analysis with the TweetEval benchmark. This model is suitable for English\n (for a similar multilingual model, see XLM-T).")
    e1e.config(bg="white") #Change backgraund color
    e1e.config(font=('arial', 11)) #Change type and size of font
    e1e.config(justify=LEFT)
    e1e.config(fg="gray") #Change text color
    e1e.place_forget()


    #---------------------------------------------------Seethal/sentiment_analysis_generic_dataset-------------------------------------------------------------

    def Delete_or_show():
     if e1ee.place_info() != {}:
            e1ee.place_forget() 
     else:
        e1ee.place(x=440, y=60)

    e0ee = Image.open('Icons/dedsep.png')
    e0ee = e0ee.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0ee = ImageTk.PhotoImage(e0ee)

    l = Button(text_clasif, text=" Seethal/sentiment_analysis_generic_dataset", image=e0ee, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    e1ee = Label(text_clasif, text= " BERT base model (uncased) \n\n Pretrained model on English language using a masked language modeling (MLM)\n objective. This model is uncased: it does not \nmake a difference between english and English. \n\n Model description \n\n BERT is a transformers model pretrained on a large corpus of English data in a\n self-supervised fashion. This means it was pretrained on the raw texts only,\n with no humans labelling them in any way (which is why it can use lots of \npublicly available data) with an automatic process to generate inputs and labels from \nthose texts. More precisely, it was pretrained with two objectives:")

    e1ee.config(bg="white") #Change backgraund color
    e1ee.config(font=('arial', 11)) #Change type and size of font
    e1ee.config(justify=LEFT)
    e1ee.config(fg="gray") #Change text color
    e1ee.place_forget()



    #-----------------------------------------------ProsusAI/finbert--------------------------------------------------

    def Delete_or_show():
     if e1e1.place_info() != {}:
            e1e1.place_forget() 
     else:
        e1e1.place(x=440, y=60)

    e0z = Image.open('Icons/box.png')
    e0z = e0z.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0z = ImageTk.PhotoImage(e0z)

    l = Button(text_clasif, text=" ProsusAI/finbert", image=e0z, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    e1e1 = Label(text_clasif, text= " FinBERT is a pre-trained NLP model to analyze sentiment of financial text. It is built by \n further training the BERT language model in the finance domain, using a large financial \n corpus and thereby fine-tuning it for financial sentiment classification. Financial \n PhraseBank by Malo et al. (2014) is used for fine-tuning. For more details, please see \n the paper FinBERT: Financial Sentiment Analysis with Pre-trained Language\n  Models and our related blog post on Medium. \n\n The model will give softmax outputs for three labels: positive, negative or neutral.")

    e1e1.config(bg="white") #Change backgraund color
    e1e1.config(font=('arial', 11)) #Change type and size of font
    e1e1.config(justify=LEFT)
    e1e1.config(fg="gray") #Change text color
    e1e1.place_forget()





    #-----------------------------------------------cardiffnlp/twitter-roberta-base-emotion---------------------------------------------------

    def Delete_or_show():
     if e1p.place_info() != {}:
            e1p.place_forget() 
     else:
        e1p.place(x=440, y=60)

    e0p = Image.open('Icons/icon01.png')
    e0p = e0p.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0p = ImageTk.PhotoImage(e0p)

    l = Button(text_clasif, text=" cardiffnlp/twitter-roberta-base-emotion", image=e0p, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    e1p = Label(text_clasif, text= " Twitter-roBERTa-base for Emotion Recognition \n\n This is a roBERTa-base model trained on ~58M tweets and finetuned for \n emotion recognition with the TweetEval benchmark.")

    e1p.config(bg="white") #Change backgraund color
    e1p.config(font=('arial', 11)) #Change type and size of font
    e1p.config(justify=LEFT)
    e1p.config(fg="gray") #Change text color
    e1p.place_forget()


    if(text_clasif):
        window3.withdraw()
    
    text_clasif.mainloop()


#                                         #---------------------------------
#----------------------------------------------text generation---------------------------------
#                                          #---------------------------------


def text_genera():

    global text_genera
    text_genera = Toplevel(window3) # create a next window from window2
    text_genera.geometry("1300x600+500+200")
    
    Button(text_genera, text="Back to Image", width=12, command=text_gene_back).place(x=0, rely=0)


    #----------------------------------------------gpt2---------------------------------------------------

    def Delete_or_show():
     if e1.place_info() != {}:
            e1.place_forget() 
     else:
        e1.place(x=440, y=60)

    e0 = Image.open('Icons/box.png')
    e0 = e0.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0 = ImageTk.PhotoImage(e0)

    l = Button(text_genera, text=" gpt2", image=e0, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    e1 = Label(text_genera, text= " Model description  \n\n GPT-2 is a transformers model pretrained on a very large corpus of English data in a \n self-supervised fashion. This means it was pretrained on the raw texts only, with no humans \n labelling them in any way (which is why it can use lots of publicly available data) with an \n automatic process to generate inputs and labels from those texts. More precisely, it was \n trained to guess the next word in sentences.\n\n More precisely, inputs are sequences of continuous text of a certain length and the \n targets are the same sequence, shifted one token (word or piece of word) to the right. \n The model uses internally a mask-mechanism to make sure the predictions for the token i \n only uses the inputs from 1 to i but not the future tokens.")

    e1.config(bg="white") #Change backgraund color
    e1.config(font=('arial', 11)) #Change type and size of font
    e1.config(justify=LEFT)
    e1.config(fg="gray") #Change text color
    e1.place_forget()

    #----------------------------------------------EleutherAI/gpt-j-6B-------------------------------------------------

    def Delete_or_show():
     if e1e.place_info() != {}:
            e1e.place_forget() 
     else:
        e1e.place(x=440, y=60)

    e0e = Image.open('Icons/box.png')
    e0e = e0e.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0e = ImageTk.PhotoImage(e0e)

    l = Button(text_genera, text=" EleutherAI/gpt-j-6B", image=e0e, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    e1e = Label(text_genera, text= "GPT-J 6B \n\n Model Description \n \n GPT-J 6B is a transformer model trained using Ben Wang's Mesh Transformer JAX. ""GPT-J"" \n refers to the class of model, while ""6B"" represents the number of trainable parameters.")
    e1e.config(bg="white") #Change backgraund color
    e1e.config(font=('arial', 11)) #Change type and size of font
    e1e.config(justify=LEFT)
    e1e.config(fg="gray") #Change text color
    e1e.place_forget()


    #---------------------------------------------------gpt2-medium-------------------------------------------------------------

    def Delete_or_show():
     if e1ee.place_info() != {}:
            e1ee.place_forget() 
     else:
        e1ee.place(x=440, y=60)

    e0ee = Image.open('Icons/dedsep.png')
    e0ee = e0ee.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0ee = ImageTk.PhotoImage(e0ee)

    l = Button(text_genera, text=" gpt2-medium", image=e0ee, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    e1ee = Label(text_genera, text= " GPT-2 Medium \n\n Model Details \n\n Model Description: GPT-2 Medium is the 355M parameter version of GPT-2, \n a transformer-based language model created and released by OpenAI. The model is a \n pretrained model on English language using a causal language modeling (CLM) objective.")

    e1ee.config(bg="white") #Change backgraund color
    e1ee.config(font=('arial', 11)) #Change type and size of font
    e1ee.config(justify=LEFT)
    e1ee.config(fg="gray") #Change text color
    e1ee.place_forget()



    #-----------------------------------------------distilgpt2--------------------------------------------------

    def Delete_or_show():
     if e1e1.place_info() != {}:
            e1e1.place_forget() 
     else:
        e1e1.place(x=440, y=60)

    e0z = Image.open('Icons/box.png')
    e0z = e0z.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0z = ImageTk.PhotoImage(e0z)

    l = Button(text_genera, text=" distilgpt2", image=e0z, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    e1e1 = Label(text_genera, text= " DistilGPT2 \n\n DistilGPT2 (short for Distilled-GPT2) is an English-language model pre-trained with \n the supervision of the smallest version of Generative Pre-trained Transformer 2 (GPT-2). Like \n GPT-2, DistilGPT2 can be used to generate text. Users of this model card should also \n consider information about the design, training, and limitations of GPT-2.")

    e1e1.config(bg="white") #Change backgraund color
    e1e1.config(font=('arial', 11)) #Change type and size of font
    e1e1.config(justify=LEFT)
    e1e1.config(fg="gray") #Change text color
    e1e1.place_forget()





    #-----------------------------------------------EleutherAI/gpt-neo-2.7B---------------------------------------------------

    def Delete_or_show():
     if e1p.place_info() != {}:
            e1p.place_forget() 
     else:
        e1p.place(x=440, y=60)

    e0p = Image.open('Icons/back.png')
    e0p = e0p.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0p = ImageTk.PhotoImage(e0p)

    l = Button(text_genera, text=" EleutherAI/gpt-neo-2.7B", image=e0p, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    e1p = Label(text_genera, text= " GPT-Neo 2.7B \n\n Model Description\n\n GPT-Neo 2.7B is a transformer model designed using EleutherAI's replication of the GPT-3 \n architecture. GPT-Neo refers to the class of models, while 2.7B represents the number \n of parameters of this particular pre-trained model.")

    e1p.config(bg="white") #Change backgraund color
    e1p.config(font=('arial', 11)) #Change type and size of font
    e1p.config(justify=LEFT)
    e1p.config(fg="gray") #Change text color
    e1p.place_forget()


    if(text_genera):
        window3.withdraw()
    
    text_genera.mainloop()


    #-------------------------------------------------------------------------------------
#----------------------------------zero-shot-classfication----------------------------
#-------------------------------------------------------------------------------------



def zero_text():

    global zero_text
    zero_text = Toplevel(window2) # create a next window from window2
    zero_text.geometry("1300x600+500+200")
    
    Button(zero_text, text="Back to Image", width=12, command=zero_back).place(x=0, rely=0)
    
    #----------------------------------facebook/bart-large-mnli---------------------------

    def Delete_or_show():
     if ff.place_info() != {}:
            ff.place_forget() 
     else:
        ff.place(x=380, y=60)

    f = Image.open('Icons/facebook.png')
    f = f.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f = ImageTk.PhotoImage(f)

    l = Button(zero_text, text=" facebook/bart-large-mnli", image=f, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    ff = Label(zero_text, text=" NLI-based Zero Shot Text Classification \n\n Yin et al. proposed a method for using pre-trained NLI models as a ready-made zero-shot \n sequence classifiers. The method works by posing the sequence to be classified as the \n NLI premise and to construct a hypothesis from each candidate label. For example, if we \n want to evaluate whether a sequence belongs to the class politics, we could construct \n a hypothesis of This text is about politics.. The probabilities for entailment and \n contradiction are then converted to label probabilities.")
    ff.config(bg="white") #Change backgraund color
    ff.config(font=('arial', 11)) #Change type and size of font
    ff.config(justify=LEFT)
    ff.config(fg="gray") #Change text color
    ff.place_forget()

    #------------------------------------------joeddav/xlm-roberta-large-xnli---------------------------------------------------

    def Delete_or_show():
     if ff1.place_info() != {}:
            ff1.place_forget() 
     else:
        ff1.place(x=380, y=60)

    f1 = Image.open('Icons/box.png')
    f1 = f1.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1 = ImageTk.PhotoImage(f1)

    l = Button(zero_text, text=" joeddav/xlm-roberta-large-xnli", image=f1, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    ff1 = Label(zero_text, text=" Model Description \n\n This model takes xlm-roberta-large and fine-tunes it on a combination of NLI data in 15 languages. \n It is intended to be used for zero-shot text classification, such as with the Hugging Face ZeroShotClassificationPipeline.")
    ff1.config(bg="white") #Change backgraund color
    ff1.config(font=('arial', 11)) #Change type and size of font
    ff1.config(justify=LEFT)
    ff1.config(fg="gray") #Change text color
    ff1.place_forget()


    #------------------------------------------valhalla/distilbart-mnli-12-1---------------------------------------------------

    def Delete_or_show():
     if val.place_info() != {}:
            val.place_forget() 
     else:
        val.place(x=380, y=60)

    f12 = Image.open('Icons/box.png')
    f12 = f12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f12 = ImageTk.PhotoImage(f12)

    l = Button(zero_text, text=" valhalla/distilbart-mnli-12-1", image=f12, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    val = Label(zero_text, text=" DistilBart-MNLI \n\n distilbart-mnli is the distilled version of bart-large-mnli created using the No Teacher \nDistillation technique proposed for BART summarisation by Huggingface, here. \n\n We just copy alternating layers from bart-large-mnli and finetune more on \n the same data.")
    val.config(bg="white") #Change backgraund color
    val.config(font=('arial', 11)) #Change type and size of font
    val.config(justify=LEFT)
    val.config(fg="gray") #Change text color
    val.place_forget()

    #------------------------------------------typeform/distilbert-base-uncased-mnli---------------------------------------------------

    def Delete_or_show():
     if vall.place_info() != {}:
            vall.place_forget() 
     else:
        vall.place(x=380, y=60)

    f122 = Image.open('Icons/box.png')
    f122 = f122.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f122 = ImageTk.PhotoImage(f122)

    l = Button(zero_text, text=" typeform/distilbert-base-uncased-mnli", image=f122, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    vall = Label(zero_text, text=" Model Details \n\n Model Description: This is the uncased DistilBERT model fine-tuned on Multi-Genre\n Natural Language Inference (MNLI) dataset for the zero-shot classification task.")
    vall.config(bg="white") #Change backgraund color
    vall.config(font=('arial', 11)) #Change type and size of font
    vall.config(justify=LEFT)
    vall.config(fg="gray") #Change text color
    vall.place_forget()


    #------------------------------------------BaptisteDoyen/camembert-base-xnli---------------------------------------------------

    def Delete_or_show():
     if vall1.place_info() != {}:
            vall1.place_forget() 
     else:
        vall1.place(x=380, y=60)

    f1221 = Image.open('Icons/box.png')
    f1221 = f1221.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1221 = ImageTk.PhotoImage(f1221)

    l = Button(zero_text, text=" BaptisteDoyen/camembert-base-xnli", image=f1221, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    vall1 = Label(zero_text, text=" camembert-base-xnli \n\n Model description \n\n Camembert-base model fine-tuned on french part of XNLI dataset.\n One of the few Zero-Shot classification model working on french 🇫🇷")
    vall1.config(bg="white") #Change backgraund color
    vall1.config(font=('arial', 11)) #Change type and size of font
    vall1.config(justify=LEFT)
    vall1.config(fg="gray") #Change text color
    vall1.place_forget()


    if(zero_text):
        window2.withdraw()
    
    zero_text.mainloop()



def text_gene_back():
    window3.iconify()
    window3.deiconify()
    text_genera.destroy()


def text_cla_back():
    window3.iconify()
    window3.deiconify()
    text_clasif.destroy()


def summari_back():
    window3.iconify()
    window3.deiconify()
    summarization.destroy()


def quest_back():
    window3.iconify()
    window3.deiconify()
    question.destroy()

def sentece_back():
    window3.iconify()
    window3.deiconify()
    sentece.destroy()

def zero_back():
    window2.iconify()
    window2.deiconify()
    zero_text.destroy()

def token_back():
    window3.iconify()
    window3.deiconify()
    token_cla.destroy()

def fill_back():
    window3.iconify()
    window3.deiconify()
    fill.destroy()

def segmeg_back():
    window2.iconify()
    window2.deiconify()
    image_segme.destroy()

def trasla_back():
    window3.iconify()
    window3.deiconify()
    traslation.destroy()

def out_test():
    raiz.iconify()
    raiz.deiconify()
    test.destroy()

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