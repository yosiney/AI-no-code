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
    Button(window2, text=" Zero-shot Image Classification", image=img5, width=198, height=30, compound="left", command=zero_shot_image).place(x=30, y=100)

    img6 = Image.open('Icons/Icon4.png')
    img6 = img6.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img6 = ImageTk.PhotoImage(img6)
    Button(window2, text=" Image-to-image", image=img6, width=198, height=30, compound="left", command=image_to_image).place(x=30, y=150)

    img7 = Image.open('Icons/Icon5.png')
    img7 = img7.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img7 = ImageTk.PhotoImage(img7)
    Button(window2, text=" Unconditional Image Generation", image=img7, width=198, height=30, compound="left", command=uncon_image_ge).place(x=30, y=190)
    
    img8 = Image.open('Icons/Icon6.png')
    img8 = img8.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img8 = ImageTk.PhotoImage(img8)
    Button(window2, text=" OBject Detection", image=img8, width=198, height=30, compound="left", command=object_detecttion_).place(x=30, y=230)

    img9 = Image.open('Icons/Icon7.png')
    img9 = img9.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img9 = ImageTk.PhotoImage(img9)
    Button(window2, text=" Video Classification", image=img9, width=198, height=30, compound="left", command=video_clasifi).place(x=260, y=230)
    
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
    Button(window3, text=" Zero-Shot-Classification", image=img16, width=198, height=30, compound="left", command=zero_shot_cla).place(x=30, y=200)

    img17 = Image.open('Icons/Icon1.png')
    img17 = img17.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img17 = ImageTk.PhotoImage(img17)
    Button(window3, text=" Text Classification", image=img17, width=198, height=30, compound="left", command=text_clasif).place(x=30, y=250)

    img18 = Image.open('Icons/Icon6.png')
    img18 = img18.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img18 = ImageTk.PhotoImage(img18)
    Button(window3, text=" Text2Text Generation", image=img18, width=198, height=30, compound="left", command=Text2_Ge).place(x=250, y=250)

    img19 = Image.open('Icons/Icon5.png')
    img19 = img19.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img19 = ImageTk.PhotoImage(img19)
    Button(window3, text=" Text Generation", image=img19, width=198, height=30, compound="left", command=text_genera).place(x=30, y=300)

    img20 = Image.open('Icons/Icon1.png')
    img20 = img20.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img20 = ImageTk.PhotoImage(img20)
    Button(window3, text=" Conversational", image=img20, width=198, height=30, compound="left", command=conver_nal).place(x=250, y=300)

    img21 = Image.open('Icons/Icon1.png')
    img21 = img21.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    img21 = ImageTk.PhotoImage(img21)
    Button(window3, text=" Table Question Answering", image=img21, width=198, height=30, compound="left", command=table_question).place(x=30, y=350)


    if(window3):
        window1.withdraw()

    window3.mainloop()



#-------------------------------------------image---------------------------------------
#-----------------------------------image classification--------------------------------
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
#---------------------------------------------------------------------------------------
#-----------------------------------image semegtation-----------------------------------
#---------------------------------------------------------------------------------------
def image_segme():

    global image_segme
    image_segme = Toplevel(window2) # create a next window from window2
    image_segme.geometry("1300x600+500+200")
    
    Button(image_segme, text="Back to Image", width=12, command=segmeg_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(image_segme, text="Test", image=imggz, width=300, height=30, compound="left", command=test2 ).place(x=600, y=400)

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

def zero_shot_image():

    global zero_shot_image
    zero_shot_image = Toplevel(window2) # create a next window from window2
    zero_shot_image.geometry("1300x600+500+200")
    
    Button(zero_shot_image, text="Back to Image", width=12, command=zero_shot_image_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(zero_shot_image, text="Test", image=imggz, width=300, height=30, compound="left", command=test3 ).place(x=600, y=400)

    #--------------------------openai/clip-vit-large-patch14--------------------

    def Delete_or_show():
     if pe.place_info() != {}:
            pe.place_forget() 
     else:
        pe.place(x=380, y=60)

    cr = Image.open('Icons/Icon2.png')
    cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    cr = ImageTk.PhotoImage(cr)

    l = Button(zero_shot_image, text=" openai/clip-vit-large-patch14", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    pe = Label(zero_shot_image, text=" Model Details \n \n  The CLIP model was developed by researchers at OpenAI to learn about what contributes\n to robustness in computer vision tasks. The model was also developed to test the ability \nof models to generalize to arbitrary image classification tasks in a zero-shot manner. It \nwas not developed for general model deployment - to deploy models like CLIP, researchers will first\n need to carefully study their capabilities in relation to the specific\n context they’re being deployed within.")
    pe.config(bg="white") #Change backgraund color
    pe.config(font=('arial', 11)) #Change type and size of font
    pe.config(justify=LEFT)
    pe.config(fg="gray") #Change text color
    pe.place_forget()


    #--------------------------openai/clip-vit-base-patch32-----------------

    def Delete_or_show():
     if pri.place_info() != {}:
            pri.place_forget() 
     else:
        pri.place(x=380, y=60)

    rc = Image.open('Icons/box.png')
    rc = rc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rc = ImageTk.PhotoImage(rc)

    l = Button(zero_shot_image, text=" openai/clip-vit-base-patch32", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    pri = Label(zero_shot_image, text=" Model Details \n\n The CLIP model was developed by researchers at OpenAI to learn about what contributes \n to robustness in computer vision tasks. The model was also developed to test the ability \nof models to generalize to arbitrary image classification tasks in a zero-shot manner. It \n was not developed for general model deployment - to deploy models like CLIP, researchers \nwill first need to carefully study their capabilities in relation to the specific \ncontext they’re being deployed within.")
    pri.config(bg="white") #Change backgraund color
    pri.config(font=('arial', 11)) #Change type and size of font
    pri.config(justify=LEFT)
    pri.config(fg="gray") #Change text color
    pri.place_forget()

    #--------------------------openai/clip-vit-large-patch14-336-----------------

    def Delete_or_show():
     if gt.place_info() != {}:
            gt.place_forget() 
     else:
        gt.place(x=380, y=60)

    rcc = Image.open('Icons/box.png')
    rcc = rcc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rcc = ImageTk.PhotoImage(rcc)

    l = Button(zero_shot_image, text=" openai/clip-vit-large-patch14-336", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    gt = Label(zero_shot_image, text=" clip-vit-large-patch14-336 \n\nThis model was trained from scratch on an unknown dataset. It achieves the following results on the evaluation set:\n\nModel description\nMore information needed\n\nIntended uses & limitations\nMore information needed")
    gt.config(bg="white") #Change backgraund color
    gt.config(font=('arial', 11)) #Change type and size of font
    gt.config(justify=LEFT)
    gt.config(fg="gray") #Change text color
    gt.place_forget()
  

    #--------------------------laion/CLIP-ViT-H-14-laion2B-s32B-b79K-----------------

    def Delete_or_show():
     if gtt.place_info() != {}:
            gtt.place_forget() 
     else:
        gtt.place(x=380, y=60)

    rccl = Image.open('Icons/nvidia.png')
    rccl = rccl.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccl = ImageTk.PhotoImage(rccl)

    l = Button(zero_shot_image, text=" laion/CLIP-ViT-H-14-laion2B-s32B-b79K", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    gtt = Label(zero_shot_image, text=" Model Description \n \n  A CLIP ViT-H/14 model trained with the LAION-2B English subset of LAION-5B\n  (https://laion.ai/blog/laion-5b/) using OpenCLIP \n(https://github.com/mlfoundations/open_clip).\n\n Model training done by Romain Beaumont on the stability.ai cluster.\n\n Uses\n\n As per the original OpenAI CLIP model card, this model is intended as a research output \n for research communities. We hope that this model will enable researchers to better \n understand and explore zero-shot, arbitrary image classification. We also hope it can be \n used for interdisciplinary studies of the potential impact of such model.")
    gtt.config(bg="white") #Change backgraund color
    gtt.config(font=('arial', 11)) #Change type and size of font
    gtt.config(justify=LEFT)
    gtt.config(fg="gray") #Change text color
    gtt.place_forget()


    #--------------------------openai/clip-vit-base-patch16-----------------

    def Delete_or_show():
     if gttn.place_info() != {}:
            gttn.place_forget() 
     else:
        gttn.place(x=380, y=60)

    rccln = Image.open('Icons/facebook.png')
    rccln = rccln.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccln = ImageTk.PhotoImage(rccln)

    l = Button(zero_shot_image, text=" openai/clip-vit-base-patch16", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    gttn = Label(zero_shot_image, text=" Model Card: CLIP\n\nDisclaimer: The model card is taken and modified from \nthe official CLIP repository, it can be found here.\n\nModel Details\n\nThe CLIP model was developed by researchers at OpenAI to learn about what contributes \n to robustness in computer vision tasks. The model was also developed to test the ability \nof models to generalize to arbitrary image classification tasks in a zero-shot manner. It\n  was not developed for general model deployment - to deploy models like CLIP, researchers\n will first need to carefully study their capabilities in relation to the specific \ncontext they’re being deployed within.")
    gttn.config(bg="white") #Change backgraund color
    gttn.config(font=('arial', 11)) #Change type and size of font
    gttn.config(justify=LEFT)
    gttn.config(fg="gray") #Change text color
    gttn.place_forget()

    if(zero_shot_image):
        window2.withdraw()
    

    zero_shot_image.mainloop()

def image_to_image():

    global image_to_image
    image_to_image = Toplevel(window2) # create a next window from window2
    image_to_image.geometry("1300x600+500+200")
    
    Button(image_to_image, text="Back to Image", width=12, command=image_to_image_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(image_to_image, text="Test", image=imggz, width=300, height=30, compound="left", command=test4 ).place(x=600, y=400)

    #--------------------------lambdalabs/sd-image-variations-diffusers-----------------

    def Delete_or_show():
     if pe.place_info() != {}:
            pe.place_forget() 
     else:
        pe.place(x=380, y=60)

    cr = Image.open('Icons/nvidia.png')
    cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    cr = ImageTk.PhotoImage(cr)

    l = Button(image_to_image, text=" lambdalabs/sd-image-variations-diffusers", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    pe = Label(image_to_image, text=" Stable Diffusion Image Variations Model Card \n \n   Image Variations is now natively supported in Diffusers! \n\nThis version of Stable Diffusion has been fine tuned from CompVis/stable-diffusion-v1-3-original\n to accept CLIP image embedding rather than text embeddings. This allows the creation of\n image variations similar to DALLE-2 using Stable Diffusion. This version of the weights has \nbeen ported to huggingface Diffusers, to use this with the Diffusers\n library requires the Lambda Diffusers repo.")
    pe.config(bg="white") #Change backgraund color
    pe.config(font=('arial', 11)) #Change type and size of font
    pe.config(justify=LEFT)
    pe.config(fg="gray") #Change text color
    pe.place_forget()


    #--------------------------keras-io/lowlight-enhance-mirnet-----------------

    def Delete_or_show():
     if pri.place_info() != {}:
            pri.place_forget() 
     else:
        pri.place(x=380, y=60)

    rc = Image.open('Icons/facebook.png')
    rc = rc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rc = ImageTk.PhotoImage(rc)

    l = Button(image_to_image, text=" keras-io/lowlight-enhance-mirnet", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    pri = Label(image_to_image, text=" Model description  \n \nThis repo contains the model and the notebook Low-light image enhancement using MIRNet. \n \nWith the goal of recovering high-quality image content from its degraded version, image  \nrestoration enjoys numerous applications, such as photography, security, medical imaging, \n and remote sensing. The MIRNet model for low-light image enhancement is a  \nfully-convolutional architecture that learns an enriched set of features that combines contextual  \ninformation from multiple scales, while simultaneously preserving the high-resolution \n spatial details")
    pri.config(bg="white") #Change backgraund color
    pri.config(font=('arial', 11)) #Change type and size of font
    pri.config(justify=LEFT)
    pri.config(fg="gray") #Change text color
    pri.place_forget()

    #--------------------------google/maxim-s3-deblurring-gopro-----------------

    def Delete_or_show():
     if gt.place_info() != {}:
            gt.place_forget() 
     else:
        gt.place(x=380, y=60)

    rcc = Image.open('Icons/icon01.png')
    rcc = rcc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rcc = ImageTk.PhotoImage(rcc)

    l = Button(image_to_image, text=" google/maxim-s3-deblurring-gopro", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    gt = Label(image_to_image, text=" Model description \n\n MAXIM introduces a shared MLP-based backbone for different image processing \ntasks such as image deblurring, deraining, denoising, dehazing, low-light image enhancement,\n and retouching. The following figure depicts the main components of MAXIM:")
    gt.config(bg="white") #Change backgraund color
    gt.config(font=('arial', 11)) #Change type and size of font
    gt.config(justify=LEFT)
    gt.config(fg="gray") #Change text color
    gt.place_forget()
  

    #-------------------------google/maxim-s2-deraining-raindrop-----------------

    def Delete_or_show():
     if gtt.place_info() != {}:
            gtt.place_forget() 
     else:
        gtt.place(x=380, y=60)

    rccl = Image.open('Icons/icon01.png')
    rccl = rccl.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccl = ImageTk.PhotoImage(rccl)

    l = Button(image_to_image, text=" google/maxim-s2-deraining-raindrop", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    gtt = Label(image_to_image, text=" Model description \n\n MAXIM introduces a shared MLP-based backbone for different image processing tasks \n such as image deblurring, deraining, denoising, dehazing, low-light image enhancement, \n and retouching. The following figure depicts the main components of MAXIM:")
    gtt.config(bg="white") #Change backgraund color
    gtt.config(font=('arial', 11)) #Change type and size of font
    gtt.config(justify=LEFT)
    gtt.config(fg="gray") #Change text color
    gtt.place_forget()


    #--------------------------google/maxim-s3-denoising-sidd-----------------

    def Delete_or_show():
     if gttn.place_info() != {}:
            gttn.place_forget() 
     else:
        gttn.place(x=380, y=60)

    rccln = Image.open('Icons/facebook.png')
    rccln = rccln.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccln = ImageTk.PhotoImage(rccln)

    l = Button(image_to_image, text=" google/maxim-s3-denoising-sidd", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    gttn = Label(image_to_image, text=" MAXIM pre-trained on SIDD for image denoising \n\n MAXIM model pre-trained for image denoising. It was introduced in the paper MAXIM: \n Multi-Axis MLP for Image Processing by Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng\n Yang, Peyman Milanfar, Alan Bovik, Yinxiao Li and first released in this repository.Disclaimer: The team releasing MAXIM did not write a model card for this\n model so this model card has been written by the Hugging Face team.")
    gttn.config(bg="white") #Change backgraund color
    gttn.config(font=('arial', 11)) #Change type and size of font
    gttn.config(justify=LEFT)
    gttn.config(fg="gray") #Change text color
    gttn.place_forget()

    if(image_to_image):
        window2.withdraw()
    

    image_to_image.mainloop()

def uncon_image_ge():

    global uncon_image_ge
    uncon_image_ge = Toplevel(window2) # create a next window from window2
    uncon_image_ge.geometry("1300x600+500+200")
    
    Button(uncon_image_ge, text="Back to Image", width=12, command=uncon_image_ge_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(uncon_image_ge, text="Test", image=imggz, width=300, height=30, compound="left", command=test5 ).place(x=600, y=400)

    #--------------------------google/ddpm-cifar10-32----------------------------

    def Delete_or_show():
     if pe.place_info() != {}:
            pe.place_forget() 
     else:
        pe.place(x=380, y=60)

    cr = Image.open('Icons/icon01.png')
    cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    cr = ImageTk.PhotoImage(cr)

    l = Button(uncon_image_ge, text=" google/ddpm-cifar10-32", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    pe = Label(uncon_image_ge, text=" Abstract: \n \nWe present high quality image synthesis results using diffusion probabilistic models, a \n class of latent variable models inspired by considerations from nonequilibrium \nthermodynamics. Our best results are obtained by training on a weighted variational \nbound designed according to a novel connection between diffusion probabilistic models  \nand denoising score matching with Langevin dynamics, and our models naturally admit a progressive \nlossy decompression scheme that can be interpreted as a generalization of autoregressive\n decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of\n 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain\n sample quality similar to ProgressiveGAN.")
    pe.config(bg="white") #Change backgraund color
    pe.config(font=('arial', 11)) #Change type and size of font
    pe.config(justify=LEFT)
    pe.config(fg="gray") #Change text color
    pe.place_forget()


    #--------------------------google/ddpm-celebahq-256-----------------

    def Delete_or_show():
     if pri.place_info() != {}:
            pri.place_forget() 
     else:
        pri.place(x=380, y=60)

    rc = Image.open('Icons/icon01.png')
    rc = rc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rc = ImageTk.PhotoImage(rc)

    l = Button(uncon_image_ge, text=" google/ddpm-celebahq-256", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    pri = Label(uncon_image_ge, text=" Abstract: \n \nWe present high quality image synthesis results using diffusion probabilistic models, a \n class of latent variable models inspired by considerations from nonequilibrium \nthermodynamics. Our best results are obtained by training on a weighted variational \nbound designed according to a novel connection between diffusion probabilistic models  \nand denoising score matching with Langevin dynamics, and our models naturally admit a progressive \nlossy decompression scheme that can be interpreted as a generalization of autoregressive\n decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of\n 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain\n sample quality similar to ProgressiveGAN.")
    pri.config(bg="white") #Change backgraund color
    pri.config(font=('arial', 11)) #Change type and size of font
    pri.config(justify=LEFT)
    pri.config(fg="gray") #Change text color
    pri.place_forget()

    #--------------------------google/ddpm-church-256-----------------

    def Delete_or_show():
     if gt.place_info() != {}:
            gt.place_forget() 
     else:
        gt.place(x=380, y=60)

    rcc = Image.open('Icons/icon01.png')
    rcc = rcc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rcc = ImageTk.PhotoImage(rcc)

    l = Button(uncon_image_ge, text=" google/ddpm-church-256", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    gt = Label(uncon_image_ge, text=" Abstract: \n \nWe present high quality image synthesis results using diffusion probabilistic models, a \n class of latent variable models inspired by considerations from nonequilibrium \nthermodynamics. Our best results are obtained by training on a weighted variational \nbound designed according to a novel connection between diffusion probabilistic models  \nand denoising score matching with Langevin dynamics, and our models naturally admit a progressive \nlossy decompression scheme that can be interpreted as a generalization of autoregressive\n decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of\n 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain\n sample quality similar to ProgressiveGAN.")
    gt.config(bg="white") #Change backgraund color
    gt.config(font=('arial', 11)) #Change type and size of font
    gt.config(justify=LEFT)
    gt.config(fg="gray") #Change text color
    gt.place_forget()
  

    #--------------------------CompVis/ldm-celebahq-256-----------------

    def Delete_or_show():
     if gtt.place_info() != {}:
            gtt.place_forget() 
     else:
        gtt.place(x=380, y=60)

    rccl = Image.open('Icons/box.png')
    rccl = rccl.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    rccl = ImageTk.PhotoImage(rccl)

    l = Button(uncon_image_ge, text=" CompVis/ldm-celebahq-256", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    gtt = Label(uncon_image_ge, text=" Abstract:\n \n By decomposing the image formation process into a sequential application of denoising \n autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image \n data and beyond. Additionally, their formulation allows for a guiding mechanism to control \n the image generation process without retraining. However, since these models typically \n operate directly in pixel space, optimization of powerful DMs often consumes hundreds of \n GPU days and inference is expensive due to sequential evaluations. To enable DM training on \n limited computational resources while retaining their quality and flexibility, we apply \n them in the latent space of powerful pretrained autoencoders. In contrast to previous work,\n training diffusion models on such a representation allows for the first time to reach a \n near-optimal point between complexity reduction and detail preservation, \n greatly boosting visual fidelity")
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

    l = Button(uncon_image_ge, text=" facebook/detr-resnet-101-panoptic", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    gttn = Label(uncon_image_ge, text=" DETR (End-to-End Object Detection) model with ResNet-101 backbone \n \n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k \n annotated images). It was introduced in the paper End-to-End Object Detection with \n Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for \n this model so this model card has been written by the Hugging Face team.")
    gttn.config(bg="white") #Change backgraund color
    gttn.config(font=('arial', 11)) #Change type and size of font
    gttn.config(justify=LEFT)
    gttn.config(fg="gray") #Change text color
    gttn.place_forget()

    if(uncon_image_ge):
        window2.withdraw()
    

    uncon_image_ge.mainloop()

def object_detecttion_():

    global object_detecttion_
    object_detecttion_ = Toplevel(window2) # create a next window from window2
    object_detecttion_.geometry("1300x600+500+200")
    
    Button(object_detecttion_, text="Back to Image", width=12, command=object_detecttion_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(object_detecttion_, text="Test", image=imggz, width=300, height=30, compound="left", command=test6 ).place(x=600, y=400)

    #--------------------------facebook/detr-resnet-50----------------

    def Delete_or_show():
     if pe.place_info() != {}:
            pe.place_forget() 
     else:
        pe.place(x=380, y=60)

    cr = Image.open('Icons/facebook.png')
    cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    cr = ImageTk.PhotoImage(cr)

    l = Button(object_detecttion_, text=" facebook/detr-resnet-50", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    pe = Label(object_detecttion_, text=" Model description \n \n The DETR model is an encoder-decoder transformer with a convolutional backbone. Two \n heads are added on top of the decoder outputs in order to perform object detection: a linear layer for the class labels and a MLP (multi-layer perceptron) for the bounding boxes. The model uses so-called object queries to detect objects in an image. Each object query looks for a particular object in the image. For COCO, the number of object queries is set to 100.")
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

    l = Button(object_detecttion_, text=" facebook/detr-resnet-50-panoptic", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    pri = Label(object_detecttion_, text=" DETR (End-to-End Object Detection) model with ResNet-50 backbone \n\n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k annotated images). \n It was introduced in the paper End-to-End Object Detection with Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been \n written by the Hugging Face team.")
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

    l = Button(object_detecttion_, text=" facebook/maskformer-swin-tiny-ade", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    gt = Label(object_detecttion_, text=" MaskFormer \n\n  MaskFormer model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). \n It was introduced in the paper Per-Pixel Classification is Not All You \n Need for Semantic Segmentation and first released in this repository. \n\n Disclaimer: The team releasing MaskFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

    l = Button(object_detecttion_, text=" nvidia/segformer-b1-finetuned-cityscapes-1024-1024", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    gtt = Label(object_detecttion_, text=" SegFormer (b1-sized) model fine-tuned on CityScapes \n \n SegFormer model fine-tuned on CityScapes at resolution 1024x1024. It was introduced in \n the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with \n Transformers by Xie et al. and first released in this repository. \n\n Disclaimer: The team releasing SegFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

    l = Button(object_detecttion_, text=" facebook/detr-resnet-101-panoptic", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    gttn = Label(object_detecttion_, text=" DETR (End-to-End Object Detection) model with ResNet-101 backbone \n \n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k \n annotated images). It was introduced in the paper End-to-End Object Detection with \n Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for \n this model so this model card has been written by the Hugging Face team.")
    gttn.config(bg="white") #Change backgraund color
    gttn.config(font=('arial', 11)) #Change type and size of font
    gttn.config(justify=LEFT)
    gttn.config(fg="gray") #Change text color
    gttn.place_forget()

    if(object_detecttion_):
        window2.withdraw()
    

    object_detecttion_.mainloop()

def video_clasifi():

    global video_clasifi
    video_clasifi = Toplevel(window2) # create a next window from window2
    video_clasifi.geometry("1300x600+500+200")
    
    Button(video_clasifi, text="Back to Image", width=12, command=video_clasifi_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(video_clasifi, text="Test", image=imggz, width=300, height=30, compound="left", command=test7 ).place(x=600, y=400)

    #--------------------------nvidia/segformer-b0-finetuned-ade-512-512-----------------

    def Delete_or_show():
     if pe.place_info() != {}:
            pe.place_forget() 
     else:
        pe.place(x=380, y=60)

    cr = Image.open('Icons/nvidia.png')
    cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    cr = ImageTk.PhotoImage(cr)

    l = Button(video_clasifi, text=" nvidia/segformer-b0-finetuned-ade-512-512", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    pe = Label(video_clasifi, text=" SegFormer (b0-sized) model fine-tuned on ADE20k \n \n SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper SegFormer: Simple \n and Efficient Design for Semantic Segmentation with Transformers by Xie et al. and first released in this repository. \n\nDisclaimer: The team releasing SegFormer did not write a model card for this model so \n this model card has been written by the Hugging Face team.")
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

    l = Button(video_clasifi, text=" facebook/detr-resnet-50-panoptic", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    pri = Label(video_clasifi, text=" DETR (End-to-End Object Detection) model with ResNet-50 backbone \n\n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k annotated images). \n It was introduced in the paper End-to-End Object Detection with Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been \n written by the Hugging Face team.")
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

    l = Button(video_clasifi, text=" facebook/maskformer-swin-tiny-ade", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    gt = Label(video_clasifi, text=" MaskFormer \n\n  MaskFormer model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). \n It was introduced in the paper Per-Pixel Classification is Not All You \n Need for Semantic Segmentation and first released in this repository. \n\n Disclaimer: The team releasing MaskFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

    l = Button(video_clasifi, text=" nvidia/segformer-b1-finetuned-cityscapes-1024-1024", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    gtt = Label(video_clasifi, text=" SegFormer (b1-sized) model fine-tuned on CityScapes \n \n SegFormer model fine-tuned on CityScapes at resolution 1024x1024. It was introduced in \n the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with \n Transformers by Xie et al. and first released in this repository. \n\n Disclaimer: The team releasing SegFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

    l = Button(video_clasifi, text=" facebook/detr-resnet-101-panoptic", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    gttn = Label(video_clasifi, text=" DETR (End-to-End Object Detection) model with ResNet-101 backbone \n \n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k \n annotated images). It was introduced in the paper End-to-End Object Detection with \n Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for \n this model so this model card has been written by the Hugging Face team.")
    gttn.config(bg="white") #Change backgraund color
    gttn.config(font=('arial', 11)) #Change type and size of font
    gttn.config(justify=LEFT)
    gttn.config(fg="gray") #Change text color
    gttn.place_forget()

    if(video_clasifi):
        window2.withdraw()
    

    video_clasifi.mainloop()

def test():

    global test
    test = Toplevel(window2) # create a next window from window2
    test.geometry("1300x500+500+200")
    
    Button(test, text="Back to Image", width=12, command=out_test).place(x=0, rely=0)  

    if(raiz):
        window2.withdraw()
    

    raiz.mainloop()

def test2():

    global test2
    test2 = Toplevel(window2) # create a next window from window2
    test2.geometry("1300x500+500+200")
    
    Button(test2, text="Back to Image", width=12, command=out_test2).place(x=0, rely=0)  

    if(image_segme):
        window2.withdraw()
    

    image_segme.mainloop()

def test3():

    global test3
    test3 = Toplevel(zero_shot_image) # create a next window from window2
    test3.geometry("1300x500+500+200")
    
    Button(test3, text="Back to Image", width=12, command=out_test3).place(x=0, rely=0)  

    if(zero_shot_image):
        zero_shot_image.withdraw()
    

    zero_shot_image.mainloop()

def test4():

    global test4
    test4 = Toplevel(image_to_image) # create a next window from window2
    test4.geometry("1300x500+500+200")
    
    Button(test4, text="Back to Image", width=12, command=out_test4).place(x=0, rely=0)  

    if(image_to_image):
        image_to_image.withdraw()
    

    image_to_image.mainloop()

def test5():

    global test5
    test5 = Toplevel(uncon_image_ge) # create a next window from window2
    test5.geometry("1300x500+500+200")
    
    Button(test5, text="Back to Image", width=12, command=out_test5).place(x=0, rely=0)  

    if(uncon_image_ge):
        uncon_image_ge.withdraw()
    

    uncon_image_ge.mainloop()

def test6():

    global test6
    test6 = Toplevel(video_clasifi) # create a next window from window2
    test6.geometry("1300x500+500+200")
    
    Button(test6, text="Back to Image", width=12, command=out_test6).place(x=0, rely=0)  

    if(video_clasifi):
        video_clasifi.withdraw()
    

    video_clasifi.mainloop()

def test7():

    global test7
    test7 = Toplevel(video_clasifi) # create a next window from window2
    test7.geometry("1300x500+500+200")
    
    Button(test7, text="Back to Image", width=12, command=out_test7).place(x=0, rely=0)  

    if(video_clasifi):
        video_clasifi.withdraw()
    

    video_clasifi.mainloop()
#-------------------------------------NLP------------------------------
#----------------------------------TRASLATION--------------------------
#----------------------------------------------------------------------
def traslation():

    global traslation
    traslation = Toplevel(window3) # create a next window from window2
    traslation.geometry("1300x600+500+200")
    
    Button(traslation, text="Back to Image", width=12, command=trasla_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(traslation, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_0 ).place(x=600, y=400)

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

#----------------------------------------------------------------------
#----------------------------------fill-Mask---------------------------
#----------------------------------------------------------------------
def fill():

    global fill
    fill = Toplevel(window3) # create a next window from window2
    fill.geometry("1300x600+500+200")
    
    Button(fill, text="Back to Image", width=12, command=fill_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(fill, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_1 ).place(x=600, y=400)

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
#----------------------------------------------------------------------
#----------------------------------Token Classification---------------
#----------------------------------------------------------------------
def token_cla():

    global token_cla
    token_cla = Toplevel(window3) # create a next window from window2
    token_cla.geometry("1300x600+500+200")
    
    Button(token_cla, text="Back to Image", width=12, command=token_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(token_cla, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_2 ).place(x=600, y=400)

  #---------------------------------
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

#----------------------------------------------------------------------
#----------------------------------sentence Similarity-----------------
#----------------------------------------------------------------------
def sentece():

    global sentece
    sentece = Toplevel(window3) # create a next window from window2
    sentece.geometry("1300x600+500+200")
    
    Button(sentece, text="Back to Image", width=12, command=sentece_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(sentece, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_3 ).place(x=600, y=400)

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
#----------------------------------------------------------------------
#----------------------------------Question answering------------------
#----------------------------------------------------------------------
def question():

    global question
    question = Toplevel(window3) # create a next window from window2
    question.geometry("1300x600+500+200")
    
    Button(question, text="Back to Image", width=12, command=quest_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(question, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_4 ).place(x=600, y=400)

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
#----------------------------------------------------------------------
#----------------------------------Summarization-----------------------
#----------------------------------------------------------------------
def summarization():

    global summarization
    summarization = Toplevel(window3) # create a next window from window2
    summarization.geometry("1300x600+500+200")
    
    Button(summarization, text="Back to Image", width=12, command=summari_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(summarization, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_5 ).place(x=600, y=400)

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
#----------------------------------------------------------------------
#----------------------------------text classification-----------------
#----------------------------------------------------------------------
def text_clasif():

    global text_clasif
    text_clasif = Toplevel(window3) # create a next window from window2
    text_clasif.geometry("1300x600+500+200")
    
    Button(text_clasif, text="Back to Image", width=12, command=text_cla_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(text_clasif, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_6 ).place(x=600, y=400)

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

#----------------------------------------------------------------------
#----------------------------------text generation---------------------
#----------------------------------------------------------------------

def text_genera():

    global text_genera
    text_genera = Toplevel(window3) # create a next window from window2
    text_genera.geometry("1300x600+500+200")
    
    Button(text_genera, text="Back to Image", width=12, command=text_gene_back).place(x=0, rely=0)

    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(text_genera, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_7 ).place(x=600, y=400)
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

    e0pc = Image.open('Icons/box.png')
    e0pc = e0pc.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    e0pc = ImageTk.PhotoImage(e0pc)

    l = Button(text_genera, text=" EleutherAI/gpt-neo-2.7B", image=e0pc, width=390, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    e1p = Label(text_genera, text= " GPT-Neo 2.7B \n\n Model Description\n\n GPT-Neo 2.7B is a transformer model designed using EleutherAI's replication of the GPT-3 \n architecture. GPT-Neo refers to the class of models, while 2.7B represents the number \n of parameters of this particular pre-trained model.")

    e1p.config(bg="white") #Change backgraund color
    e1p.config(font=('arial', 11)) #Change type and size of font
    e1p.config(justify=LEFT)
    e1p.config(fg="gray") #Change text color
    e1p.place_forget()


    if(text_genera):
        window3.withdraw()
    
    text_genera.mainloop()

#----------------------------------------------------------------------
#----------------------------------zero-shot-classfication-------------
#----------------------------------------------------------------------
def zero_shot_cla():

    global zero_shot_cla
    zero_shot_cla = Toplevel(window3) # create a next window from window2
    zero_shot_cla.geometry("1300x600+500+200")
    
    Button(zero_shot_cla, text="Back to Image", width=12, command=zero_back).place(x=0, rely=0)
    
    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(zero_shot_cla, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_8 ).place(x=600, y=400)

    #----------------------------------facebook/bart-large-mnli---------------------------

    def Delete_or_show():
     if ff.place_info() != {}:
            ff.place_forget() 
     else:
        ff.place(x=380, y=60)

    f = Image.open('Icons/facebook.png')
    f = f.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f = ImageTk.PhotoImage(f)

    l = Button(zero_shot_cla, text=" facebook/bart-large-mnli", image=f, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    ff = Label(zero_shot_cla, text=" NLI-based Zero Shot Text Classification \n\n Yin et al. proposed a method for using pre-trained NLI models as a ready-made zero-shot \n sequence classifiers. The method works by posing the sequence to be classified as the \n NLI premise and to construct a hypothesis from each candidate label. For example, if we \n want to evaluate whether a sequence belongs to the class politics, we could construct \n a hypothesis of This text is about politics.. The probabilities for entailment and \n contradiction are then converted to label probabilities.")
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

    l = Button(zero_shot_cla, text=" joeddav/xlm-roberta-large-xnli", image=f1, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    ff1 = Label(zero_shot_cla, text=" Model Description \n\n This model takes xlm-roberta-large and fine-tunes it on a combination of NLI data in 15 languages. \n It is intended to be used for zero-shot text classification, such as with the Hugging Face ZeroShotClassificationPipeline.")
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

    l = Button(zero_shot_cla, text=" valhalla/distilbart-mnli-12-1", image=f12, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    val = Label(zero_shot_cla, text=" DistilBart-MNLI \n\n distilbart-mnli is the distilled version of bart-large-mnli created using the No Teacher \nDistillation technique proposed for BART summarisation by Huggingface, here. \n\n We just copy alternating layers from bart-large-mnli and finetune more on \n the same data.")
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

    l = Button(zero_shot_cla, text=" typeform/distilbert-base-uncased-mnli", image=f122, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    vall = Label(zero_shot_cla, text=" Model Details \n\n Model Description: This is the uncased DistilBERT model fine-tuned on Multi-Genre\n Natural Language Inference (MNLI) dataset for the zero-shot classification task.")
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

    l = Button(zero_shot_cla, text=" BaptisteDoyen/camembert-base-xnli", image=f1221, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    vall1 = Label(zero_shot_cla, text=" camembert-base-xnli \n\n Model description \n\n Camembert-base model fine-tuned on french part of XNLI dataset.\n One of the few Zero-Shot classification model working on french 🇫🇷")
    vall1.config(bg="white") #Change backgraund color
    vall1.config(font=('arial', 11)) #Change type and size of font
    vall1.config(justify=LEFT)
    vall1.config(fg="gray") #Change text color
    vall1.place_forget()


    if(zero_shot_cla):
        window3.withdraw()
    
    zero_shot_cla.mainloop()

#----------------------------------------------------------------------
#----------------------------------Text2Text Generation----------------
#----------------------------------------------------------------------
def Text2_Ge():

    global Text2_Ge
    Text2_Ge = Toplevel(window3) # create a next window from window2
    Text2_Ge.geometry("1300x600+500+200")
    
    Button(Text2_Ge, text="Back to Image", width=12, command=text2_ge_back).place(x=0, rely=0)
    
    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(Text2_Ge, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_9 ).place(x=600, y=400)

    #----------------------------------prithivida/parrot_paraphraser_on_T5---------------------------

    def Delete_or_show():
     if ff.place_info() != {}:
            ff.place_forget() 
     else:
        ff.place(x=380, y=60)

    f = Image.open('Icons/facebook.png')
    f = f.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f = ImageTk.PhotoImage(f)

    l = Button(Text2_Ge, text=" prithivida/parrot_paraphraser_on_T5", image=f, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    ff = Label(Text2_Ge, text=" What is Parrot? \n\n Parrot is a paraphrase based utterance augmentation framework purpose built to \n accelerate training NLU models. A paraphrase framework is more than just a \n paraphrasing model. For more details on the library and usage please refer to the github page")
    ff.config(bg="white") #Change backgraund color
    ff.config(font=('arial', 11)) #Change type and size of font
    ff.config(justify=LEFT)
    ff.config(fg="gray") #Change text color
    ff.place_forget()

    #------------------------------------------allenai/led-base-16384---------------------------------------------------

    def Delete_or_show():
     if ff1.place_info() != {}:
            ff1.place_forget() 
     else:
        ff1.place(x=380, y=60)

    f1 = Image.open('Icons/box.png')
    f1 = f1.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1 = ImageTk.PhotoImage(f1)

    l = Button(Text2_Ge, text=" allenai/led-base-16384", image=f1, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    ff1 = Label(Text2_Ge, text=" Introduction \n\n Allenai's Longformer Encoder-Decoder (LED).\n\n As described in Longformer: The Long-Document Transformer by Iz Beltagy, \n Matthew E. Peters, Arman Cohan, led-base-16384 was initialized from bart-base since both models\n share the exact same architecture. To be able to process 16K tokens, bart-base's position\n embedding matrix was simply copied 16 times. \n\n This model is especially interesting for long-range \n summarization and question answering.")
    ff1.config(bg="white") #Change backgraund color
    ff1.config(font=('arial', 11)) #Change type and size of font
    ff1.config(justify=LEFT)
    ff1.config(fg="gray") #Change text color
    ff1.place_forget()


    #------------------------------------------mrm8488/t5-base-finetuned-question-generation-ap---------------------------------------------------

    def Delete_or_show():
     if val.place_info() != {}:
            val.place_forget() 
     else:
        val.place(x=380, y=60)

    f12 = Image.open('Icons/box.png')
    f12 = f12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f12 = ImageTk.PhotoImage(f12)

    l = Button(Text2_Ge, text=" t5-base-finetuned-question-generation-ap", image=f12, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    val = Label(Text2_Ge, text=" Details of T5 \n\n The T5 model was presented in Exploring the Limits of Transfer Learning with a Unified \nText-to-Text Transformer by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, \nSharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu in Here the abstract:\n\n Transfer learning, where a model is first pre-trained on a data-rich task before being \nfine-tuned on a downstream task, has emerged as a powerful technique in natural language\n processing (NLP). The effectiveness of transfer learning has given rise to a diversity\n of approaches, methodology, and practice. In this paper, we explore the landscape\n of transfer learning techniques for NLP by introducing a unified framework that converts \nevery language problem into a text-to-text format.")
    val.config(bg="white") #Change backgraund color
    val.config(font=('arial', 11)) #Change type and size of font
    val.config(justify=LEFT)
    val.config(fg="gray") #Change text color
    val.place_forget()

    #------------------------------------------facebook/m2m100_418M--------------------------------------------------

    def Delete_or_show():
     if vall.place_info() != {}:
            vall.place_forget() 
     else:
        vall.place(x=380, y=60)

    f122 = Image.open('Icons/facebook.png')
    f122 = f122.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f122 = ImageTk.PhotoImage(f122)

    l = Button(Text2_Ge, text=" facebook/m2m100_418M", image=f122, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    vall = Label(Text2_Ge, text=" M2M100 418M \n\n M2M100 is a multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many\n multilingual translation. It was introduced in this paper and first released \n in this repository. \n\n The model that can directly translate between the 9,900 directions of 100 languages. \nTo translate into a target language, the target language id is forced as the first generated \n  token. To force the target language id as the first generated token, pass the\n  forced_bos_token_id parameter to the generate method.")
    vall.config(bg="white") #Change backgraund color
    vall.config(font=('arial', 11)) #Change type and size of font
    vall.config(justify=LEFT)
    vall.config(fg="gray") #Change text color
    vall.place_forget()


    #------------------------------------------google/mt5-small--------------------------------------------------

    def Delete_or_show():
     if vall1.place_info() != {}:
            vall1.place_forget() 
     else:
        vall1.place(x=380, y=60)

    f1221 = Image.open('Icons/icon01.png')
    f1221 = f1221.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1221 = ImageTk.PhotoImage(f1221)

    l = Button(Text2_Ge, text=" google/mt5-small", image=f1221, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    vall1 = Label(Text2_Ge, text=" Abstract \n\n The recent Text-to-Text Transfer Transformer (T5) leveraged a unified text-to-text format\n and scale to attain state-of-the-art results on a wide variety of English-language NLP\n tasks. In this paper, we introduce mT5, a multilingual variant of T5 that was pre-trained \n on a new Common Crawl-based dataset covering 101 languages. We describe the design \n and modified training of mT5 and demonstrate its state-of-the-art performance on many \nmultilingual benchmarks. All of the code and model checkpoints used in this \nwork are publicly available.")
    vall1.config(bg="white") #Change backgraund color
    vall1.config(font=('arial', 11)) #Change type and size of font
    vall1.config(justify=LEFT)
    vall1.config(fg="gray") #Change text color
    vall1.place_forget()


    if(Text2_Ge):
        window3.withdraw()
    
    Text2_Ge.mainloop()
#----------------------------------------------------------------------
#----------------------------------conversational----------------------
#----------------------------------------------------------------------
def conver_nal():

    global conver_nal
    conver_nal = Toplevel(window3) # create a next window from window2
    conver_nal.geometry("1300x600+500+200")
    
    Button(conver_nal, text="Back to Image", width=12, command=conver_back).place(x=0, rely=0)
    
    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(conver_nal, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_10 ).place(x=600, y=400)

    #----------------------------------------microsoft/DialoGPT-medium---------------------------------------

    def Delete_or_show():
     if ff.place_info() != {}:
            ff.place_forget() 
     else:
        ff.place(x=380, y=60)

    f = Image.open('Icons/Icon00.png')
    f = f.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f = ImageTk.PhotoImage(f)

    l = Button(conver_nal, text=" microsoft/DialoGPT-medium", image=f, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    ff = Label(conver_nal, text=" A State-of-the-Art Large-scale Pretrained Response generation model (DialoGPT) \n\n DialoGPT is a SOTA large-scale pretrained dialogue response generation model \n for multiturn conversations. The human evaluation results indicate that the response \n generated from DialoGPT is comparable to human response quality under a single-turn \n conversation Turing test. The model is trained on 147M multi-turn \n dialogue from Reddit discussion thread.")
    ff.config(bg="white") #Change backgraund color
    ff.config(font=('arial', 11)) #Change type and size of font
    ff.config(justify=LEFT)
    ff.config(fg="gray") #Change text color
    ff.place_forget()

    #------------------------------------------facebook/blenderbot-400M-distill---------------------------------------------------

    def Delete_or_show():
     if ff1.place_info() != {}:
            ff1.place_forget() 
     else:
        ff1.place(x=380, y=60)

    f1 = Image.open('Icons/facebook.png')
    f1 = f1.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1 = ImageTk.PhotoImage(f1)

    l = Button(conver_nal, text=" facebook/blenderbot-400M-distill", image=f1, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    ff1 = Label(conver_nal, text=" Abstract \n\n Building open-domain chatbots is a challenging area for machine learning research. \n While prior work has shown that scaling neural models in the number of parameters \n and the size of the data they are trained on gives improved results, we show that other \n ingredients are important for a high-performing chatbot. Good conversation requires a \n number of skills that an expert conversationalist blends in a seamless way: providing \n engaging talking points and listening to their partners, both asking and answering \n questions, and displaying knowledge, empathy and personality appropriately, \n depending on the situation. We show that large scale models can learn these skills when \n given appropriate training data and choice of generation strategy. We build variants of\n these recipes with 90M, 2.7B and 9.4B parameter neural models, and make our models\n and code publicly available. Human evaluations show our best models are superior to \n existing approaches in multi-turn dialogue in terms of engagingness and humanness \n measurements. We then discuss the limitations of this work by analyzing failure cases of our models.")
    ff1.config(bg="white") #Change backgraund color
    ff1.config(font=('arial', 11)) #Change type and size of font
    ff1.config(justify=LEFT)
    ff1.config(fg="gray") #Change text color
    ff1.place_forget()


    #------------------------------------------microsoft/DialoGPT-large---------------------------------------------------

    def Delete_or_show():
     if val.place_info() != {}:
            val.place_forget() 
     else:
        val.place(x=380, y=60)

    f12 = Image.open('Icons/Icon00.png')
    f12 = f12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f12 = ImageTk.PhotoImage(f12)

    l = Button(conver_nal, text=" microsoft/DialoGPT-large", image=f12, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    val = Label(conver_nal, text=" A State-of-the-Art Large-scale Pretrained Response generation model (DialoGPT) \n\n DialoGPT is a SOTA large-scale pretrained dialogue response generation model for \n multiturn conversations. The human evaluation results indicate that the response \n generated from DialoGPT is comparable to human response quality under a single-turn \n conversation Turing test. The model is trained on 147M multi-turn dialogue\n  from Reddit discussion thread. \n\n Multi-turn generation examples from an interactive environment:")
    val.config(bg="white") #Change backgraund color
    val.config(font=('arial', 11)) #Change type and size of font
    val.config(justify=LEFT)
    val.config(fg="gray") #Change text color
    val.place_forget()

    #------------------------------------------microsoft/DialoGPT-small--------------------------------------------------

    def Delete_or_show():
     if vall.place_info() != {}:
            vall.place_forget() 
     else:
        vall.place(x=380, y=60)

    f122 = Image.open('Icons/Icon00.png')
    f122 = f122.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f122 = ImageTk.PhotoImage(f122)

    l = Button(conver_nal, text=" microsoft/DialoGPT-small", image=f122, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    vall = Label(conver_nal, text=" A State-of-the-Art Large-scale Pretrained Response generation model (DialoGPT) \n\n DialoGPT is a SOTA large-scale pretrained dialogue response generation model for \n multiturn conversations. The human evaluation results indicate that the response \n generated from DialoGPT is comparable to human response quality under a single-turn\n  conversation Turing test. The model is trained on 147M multi-turn dialogue \n from Reddit discussion thread.")
    vall.config(bg="white") #Change backgraund color
    vall.config(font=('arial', 11)) #Change type and size of font
    vall.config(justify=LEFT)
    vall.config(fg="gray") #Change text color
    vall.place_forget()


    #------------------------------------------facebook/blenderbot_small-90M--------------------------------------------------

    def Delete_or_show():
     if vall1.place_info() != {}:
            vall1.place_forget() 
     else:
        vall1.place(x=380, y=60)

    f1221 = Image.open('Icons/facebook.png')
    f1221 = f1221.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1221 = ImageTk.PhotoImage(f1221)

    l = Button(conver_nal, text=" facebook/blenderbot_small-90M", image=f1221, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    vall1 = Label(conver_nal, text=" Abstract \n\n Building open-domain chatbots is a challenging area for machine learning research. \nWhile prior work has shown that scaling neural models in the number of parameters and\n the size of the data they are trained on gives improved results, we show that other\n ingredients are important for a high-performing chatbot. Good conversation requires a \nnumber of skills that an expert conversationalist blends in a seamless way: providing \nengaging talking points and listening to their partners, both asking and answering \nquestions, and displaying knowledge, empathy and personality appropriately, \ndepending on the situation. We show that large scale models can learn these skills when \ngiven appropriate training data and choice of generation strategy. We build variants \n of these recipes with 90M, 2.7B and 9.4B parameter neural models, and make our models \n and code publicly available. Human evaluations show our best models are superior to\n existing approaches in multi-turn dialogue in terms of engagingness and humanness \n measurements. We then discuss the limitations of this work by analyzing failure \n cases of our models.")
    vall1.config(bg="white") #Change backgraund color
    vall1.config(font=('arial', 11)) #Change type and size of font
    vall1.config(justify=LEFT)
    vall1.config(fg="gray") #Change text color
    vall1.place_forget()


    if(conver_nal):
        window3.withdraw()
    
    conver_nal.mainloop()
#----------------------------------------------------------------------
#----------------------------------table question answering------------
#----------------------------------------------------------------------
def table_question():

    global table_question
    table_question = Toplevel(window3) # create a next window from window2
    table_question.geometry("1300x600+500+200")
    
    Button(table_question, text="Back to Image", width=12, command=table_question_back).place(x=0, rely=0)
    
    imggz = Image.open('Icons/1.png')
    imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    imggz = ImageTk.PhotoImage(imggz)
    cias = Button(table_question, text="Test", image=imggz, width=300, height=30, compound="left", command=test1_11 ).place(x=600, y=400)

    #----------------------------------------google/tapas-base-finetuned-wtq---------------------------------------

    def Delete_or_show():
     if ff.place_info() != {}:
            ff.place_forget() 
     else:
        ff.place(x=380, y=60)

    f = Image.open('Icons/icon01.png')
    f = f.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f = ImageTk.PhotoImage(f)

    l = Button(table_question, text=" google/tapas-base-finetuned-wtq", image=f, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
    ff = Label(table_question, text=" TAPAS base model fine-tuned on WikiTable Questions (WTQ) \n\n This model has 2 versions which can be used. The default version corresponds to the \n tapas_wtq_wikisql_sqa_inter_masklm_base_reset checkpoint of the original \n Github repository. This model was pre-trained on MLM and an additional step which the \n authors call intermediate pre-training, and then fine-tuned in a chain on SQA, WikiSQL \n and finally WTQ. It uses relative position embeddings (i.e. resetting the position index at\n  every cell of the table).")
    ff.config(bg="white") #Change backgraund color
    ff.config(font=('arial', 11)) #Change type and size of font
    ff.config(justify=LEFT)
    ff.config(fg="gray") #Change text color
    ff.place_forget()

    #------------------------------------------google/tapas-large-finetuned-wtq---------------------------------------------------

    def Delete_or_show():
     if ff1.place_info() != {}:
            ff1.place_forget() 
     else:
        ff1.place(x=380, y=60)

    f1 = Image.open('Icons/icon01.png')
    f1 = f1.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1 = ImageTk.PhotoImage(f1)

    l = Button(table_question, text=" google/tapas-large-finetuned-wtq", image=f1, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
    ff1 = Label(table_question, text=" TAPAS large model fine-tuned on WikiTable Questions (WTQ) \n\n This model has 2 versions which can be used. The default version corresponds to the \n tapas_wtq_wikisql_sqa_inter_masklm_large_reset checkpoint of the original Github repository. \n This model was pre-trained on MLM and an additional step which the authors call intermediate pre-training, \n and then fine-tuned in a chain on SQA, WikiSQL and finally WTQ. It uses relative position \n embeddings (i.e. resetting the position index at every cell of the table).")
    ff1.config(bg="white") #Change backgraund color
    ff1.config(font=('arial', 11)) #Change type and size of font
    ff1.config(justify=LEFT)
    ff1.config(fg="gray") #Change text color
    ff1.place_forget()


    #------------------------------------------google/tapas-small-finetuned-wtq---------------------------------------------------

    def Delete_or_show():
     if val.place_info() != {}:
            val.place_forget() 
     else:
        val.place(x=380, y=60)

    f12 = Image.open('Icons/icon01.png')
    f12 = f12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f12 = ImageTk.PhotoImage(f12)

    l = Button(table_question, text=" google/tapas-small-finetuned-wtq", image=f12, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
    val = Label(table_question, text=" TAPAS small model fine-tuned on WikiTable Questions (WTQ) \n\n This model has 2 versions which can be used. The default version corresponds to the \n tapas_wtq_wikisql_sqa_inter_masklm_small_reset checkpoint of the original Github repository. \n This model was pre-trained on MLM and an additional step which the authors \n call intermediate pre-training, and then fine-tuned in a chain on SQA, WikiSQL \n and finally WTQ. It uses relative position embeddings (i.e. resetting\n the position index at every cell of the table).")
    val.config(bg="white") #Change backgraund color
    val.config(font=('arial', 11)) #Change type and size of font
    val.config(justify=LEFT)
    val.config(fg="gray") #Change text color
    val.place_forget()

    #------------------------------------------microsoft/tapex-large-finetuned-wtq--------------------------------------------------

    def Delete_or_show():
     if vall.place_info() != {}:
            vall.place_forget() 
     else:
        vall.place(x=380, y=60)

    f122 = Image.open('Icons/Icon00.png')
    f122 = f122.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f122 = ImageTk.PhotoImage(f122)

    l = Button(table_question, text=" microsoft/tapex-large-finetuned-wtq", image=f122, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
    vall = Label(table_question, text=" TAPEX (large-sized model) \n \n TAPEX was proposed in TAPEX: Table Pre-training via Learning a Neural SQL Executor by Qian Liu,\n Bei Chen, Jiaqi Guo, Morteza Ziyadi, Zeqi Lin, Weizhu Chen, Jian-Guang Lou.\n The original repo can be found here.\n\n Model description \n\n TAPEX (Table Pre-training via Execution) is a conceptually simple and empirically \n powerful pre-training approach to empower existing models with table reasoning skills. \n TAPEX realizes table pre-training by learning a neural SQL executor over a synthetic \n corpus, which is obtained by automatically synthesizing executable SQL queries.")
    vall.config(bg="white") #Change backgraund color
    vall.config(font=('arial', 11)) #Change type and size of font
    vall.config(justify=LEFT)
    vall.config(fg="gray") #Change text color
    vall.place_forget()


    #------------------------------------------google/tapas-base-finetuned-sqa-------------------------------------------------

    def Delete_or_show():
     if vall1.place_info() != {}:
            vall1.place_forget() 
     else:
        vall1.place(x=380, y=60)

    f1221 = Image.open('Icons/icon01.png')
    f1221 = f1221.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
    f1221 = ImageTk.PhotoImage(f1221)

    l = Button(table_question, text=" google/tapas-base-finetuned-sqa", image=f1221, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
    vall1 = Label(table_question, text=" TAPAS base model fine-tuned on Sequential Question Answering (SQA) \n\n This model has 2 versions which can be used. The default version corresponds to the \n tapas_sqa_inter_masklm_base_reset checkpoint of the original Github repository. \n This model was pre-trained on MLM and an additional step which the authors call \n intermediate pre-training, and then fine-tuned on SQA. It uses relative position\n  embeddings (i.e. resetting the position index at every cell of the table).")
    vall1.config(bg="white") #Change backgraund color
    vall1.config(font=('arial', 11)) #Change type and size of font
    vall1.config(justify=LEFT)
    vall1.config(fg="gray") #Change text color
    vall1.place_forget()


    if(table_question):
        window3.withdraw()
    
    table_question.mainloop()



#---in this part put on just the button test because it a create a new window showing the results
def test1_0():

    global test1_0
    test1_0 = Toplevel(traslation) # create a next window from window3
    test1_0.geometry("1300x500+500+200")
    
    Button(test1_0, text="Back to Image", width=12, command=out_test1_0).place(x=0, rely=0)  

    if(traslation):
        traslation.withdraw()
    

    traslation.mainloop()

def test1_1():

    global test1_1
    test1_1 = Toplevel(fill) # create a next window from window3
    test1_1.geometry("1300x500+500+200")
    
    Button(test1_1, text="Back to Image", width=12, command=out_test1_1).place(x=0, rely=0)  

    if(fill):
        fill.withdraw()
    

    fill.mainloop()

def test1_2():

    global test1_2
    test1_2 = Toplevel(token_cla) # create a next window from window3
    test1_2.geometry("1300x500+500+200")
    
    Button(test1_2, text="Back to Image", width=12, command=out_test1_2).place(x=0, rely=0)  

    if(token_cla):
        token_cla.withdraw()
    

    token_cla.mainloop()

def test1_3():

    global test1_3
    test1_3 = Toplevel(token_cla) # create a next window from window3
    test1_3.geometry("1300x500+500+200")
    
    Button(test1_3, text="Back to Image", width=12, command=out_test1_3).place(x=0, rely=0)  

    if(token_cla):
        token_cla.withdraw()
    

    token_cla.mainloop()

def test1_4():

    global test1_4
    test1_4 = Toplevel(question) # create a next window from window3
    test1_4.geometry("1300x500+500+200")
    
    Button(test1_4, text="Back to Image", width=12, command=out_test1_4).place(x=0, rely=0)  

    if(question):
        question.withdraw()
    

    question.mainloop()

def test1_5():

    global test1_5
    test1_5 = Toplevel(summarization) # create a next window from window3
    test1_5.geometry("1300x500+500+200")
    
    Button(test1_5, text="Back to Image", width=12, command=out_test1_5).place(x=0, rely=0)  

    if(summarization):
        summarization.withdraw()
    

    summarization.mainloop()

def test1_6():

    global test1_6
    test1_6 = Toplevel(text_clasif) # create a next window from window3
    test1_6.geometry("1300x500+500+200")
    
    Button(test1_6, text="Back to Image", width=12, command=out_test1_6).place(x=0, rely=0)  

    if(text_clasif):
        text_clasif.withdraw()
    

    text_clasif.mainloop()

def test1_7():

    global test1_7
    test1_7 = Toplevel(text_genera) # create a next window from window3
    test1_7.geometry("1300x500+500+200")
    
    Button(test1_7, text="Back to Image", width=12, command=out_test1_7).place(x=0, rely=0)  

    if(text_genera):
        text_genera.withdraw()
    

    text_genera.mainloop()

def test1_8():

    global test1_8
    test1_8 = Toplevel(zero_shot_cla) # create a next window from window3
    test1_8.geometry("1300x500+500+200")
    
    Button(test1_8, text="Back to Image", width=12, command=out_test1_8).place(x=0, rely=0)  

    if(zero_shot_cla):
        zero_shot_cla.withdraw()
    

    zero_shot_cla.mainloop()

def test1_9():

    global test1_9
    test1_9 = Toplevel(Text2_Ge) # create a next window from window3
    test1_9.geometry("1300x500+500+200")
    
    Button(test1_9, text="Back to Image", width=12, command=out_test1_9).place(x=0, rely=0)  

    if(Text2_Ge):
        Text2_Ge.withdraw()
    
    Text2_Ge.mainloop()

def test1_10():

    global test1_10
    test1_10 = Toplevel(conver_nal) # create a next window from window3
    test1_10.geometry("1300x500+500+200")
    
    Button(test1_10, text="Back to Image", width=12, command=out_test1_10).place(x=0, rely=0)  

    if(conver_nal):
        conver_nal.withdraw()
    
    conver_nal.mainloop()

def test1_11():

    global test1_11
    test1_11 = Toplevel(table_question) # create a next window from window3
    test1_11.geometry("1300x500+500+200")
    
    Button(test1_11, text="Back to Image", width=12, command=out_test1_11).place(x=0, rely=0)  

    if(table_question):
        table_question.withdraw()
    
    table_question.mainloop()   

#--back
def zero_shot_image_back():
    window2.iconify()
    window2.deiconify()
    zero_shot_image.destroy()

def image_to_image_back():
    window2.iconify()
    window2.deiconify()
    image_to_image.destroy()

def uncon_image_ge_back():
    window2.iconify()
    window2.deiconify()
    uncon_image_ge.destroy()

def object_detecttion_back():
    window2.iconify()
    window2.deiconify()
    object_detecttion_.destroy()

def video_clasifi_back():
    window2.iconify()
    window2.deiconify()
    video_clasifi.destroy()


#--back

def table_question_back():
    window3.iconify()
    window3.deiconify()
    table_question.destroy()

def conver_back():
    window3.iconify()
    window3.deiconify()
    conver_nal.destroy()

def text2_ge_back():
    window3.iconify()
    window3.deiconify()
    Text2_Ge.destroy()

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
    window3.iconify()
    window3.deiconify()
    zero_shot_cla.destroy()

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





#--Back_IMAGE
def out_test():
    raiz.iconify()
    raiz.deiconify()
    test.destroy()

def out_test2():
    image_segme.iconify()
    image_segme.deiconify()
    test2.destroy()

def out_test3():
    zero_shot_image.iconify()
    zero_shot_image.deiconify()
    test3.destroy()

def out_test4():
    image_to_image.iconify()
    image_to_image.deiconify()
    test4.destroy()

def out_test5():
    uncon_image_ge.iconify()
    uncon_image_ge.deiconify()
    test5.destroy()   

def out_test6():
    object_detecttion_.iconify()
    object_detecttion_.deiconify()
    test6.destroy()

def out_test7():
    video_clasifi.iconify()
    video_clasifi.deiconify()
    test7.destroy()


#--Back_NLP
def out_test1_0():
    traslation.iconify()
    traslation.deiconify()
    test1_0.destroy()

def out_test1_1():
    fill.iconify()
    fill.deiconify()
    test1_1.destroy()

def out_test1_2():
    token_cla.iconify()
    token_cla.deiconify()
    test1_2.destroy()

def out_test1_3():
    sentece.iconify()
    sentece.deiconify()
    test1_3.destroy()

def out_test1_4():
    question.iconify()
    question.deiconify()
    test1_4.destroy()

def out_test1_5():
    summarization.iconify()
    summarization.deiconify()
    test1_5.destroy()

def out_test1_6():
    text_clasif.iconify()
    text_clasif.deiconify()
    test1_6.destroy()

def out_test1_7():
    text_genera.iconify()
    text_genera.deiconify()
    test1_7.destroy()

def out_test1_8():
    zero_shot_cla.iconify()
    zero_shot_cla.deiconify()
    test1_8.destroy()

def out_test1_9():
    Text2_Ge.iconify()
    Text2_Ge.deiconify()
    test1_9.destroy()

def out_test1_10():
    conver_nal.iconify()
    conver_nal.deiconify()
    test1_10.destroy()

def out_test1_11():
    table_question.iconify()
    table_question.deiconify()
    test1_11.destroy()


window1()
