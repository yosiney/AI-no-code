
from tkinter import *
from tkinter import Tk, Button
import tkinter as tk
from PIL import Image,ImageTk

#---------------------------------------Image------------------------------------------------------------------
class Window(tk.Toplevel):
 
       def __init__(self, parent):
              super().__init__(parent)

              #self = Toplevel(window1) # create a next window from window1
              self.geometry("800x500+500+200")
              self.title("image")
              
              if(self):          
                     parent.withdraw()
              def back_window():
              
                     parent.iconify() 
                     parent.deiconify() 
                     self.destroy()   
                         
              Button(self, text="Back to main", width=10, command=back_window).place(x=0, rely=0)
              img3 = Image.open('Icons/Icon1.png')
              img3 = img3.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img3 = ImageTk.PhotoImage(img3)
              Button(self, text=" Image classification",image=self.img3,  width=198, height=30, compound="left", command=self.raiz).place(x=30, y=50)
              img4 = Image.open('Icons/Icon2.png')
              img4 = img4.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img4 = ImageTk.PhotoImage(img4)
              Button(self, text=" Image Segmentation", image=self.img4,  width=198, height=30, compound="left", command= self.image_segme).place(x=260, y=50)
              img5 = Image.open('Icons/Icon3.png')
              img5 = img5.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img5 = ImageTk.PhotoImage(img5)
              Button(self, text=" Zero-shot Image Classification", image=self.img5, width=198, height=30, compound="left", command= self.zero_shot_image).place(x=30, y=100)
              img6 = Image.open('Icons/Icon4.png')
              img6 = img6.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img6 = ImageTk.PhotoImage(img6)
              Button(self, text=" Image-to-image", image=self.img6, width=198, height=30, compound="left", command= self.image_to_image).place(x=30, y=150)
              img7 = Image.open('Icons/Icon5.png')
              img7 = img7.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img7 = ImageTk.PhotoImage(img7)
              Button(self, text=" Unconditional Image Generation", image=self.img7,  width=198, height=30, compound="left", command= self.uncon_image_ge).place(x=30, y=190)

              img8 = Image.open('Icons/Icon6.png')
              img8 = img8.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img8 = ImageTk.PhotoImage(img8)
              Button(self, text=" OBject Detection",  image=self.img8, width=198, height=30, compound="left", command= self.object_detecttion_).place(x=30, y=230)
              img9 = Image.open('Icons/Icon7.png')
              img9 = img9.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              self.img9 = ImageTk.PhotoImage(img9)
              Button(self, text=" Video Classification",  image=self.img9, width=198, height=30, compound="left", command= self.video_clasifi).place(x=260, y=230)      
      
          
              
         
       
       def image_segme(self):

              global image_segme
              image_segme = Toplevel(self) # create a next window from self
              image_segme.geometry("1300x600+500+200")

              Button(image_segme, text="Back to Image", width=12, command=self.segmeg_back).place(x=0, rely=0)

              imggz = Image.open('Icons/1.png')
              imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              imggz = ImageTk.PhotoImage(imggz)
              cias = Button(image_segme, text="Test", image=imggz, width=300, height=30, compound="left", command=self.test2 ).place(x=600, y=400)

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
                  self.withdraw()


              image_segme.mainloop()

       
       def segmeg_back(self):
              self.iconify()
              self.deiconify()
              image_segme.destroy()
       
       
       def raiz(self):

           global raiz
           raiz = Toplevel(self) # create a next window from self
           raiz.geometry("1300x500+500+200")
       
           Button(raiz, text="Back to Image", width=12, command=self.back_window3).place(x=0, rely=0)

           imgg = Image.open('Icons/1.png')
           imgg = imgg.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
           imgg = ImageTk.PhotoImage(imgg)
           cias = Button(raiz, text="Test", image=imgg, width=300, height=30, compound="left", command=self.test ).place(x=600, y=400)
       
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
               self.withdraw()
       

           raiz.mainloop()
#---------------------

       def zero_shot_image(self):

              global zero_shot_image
              zero_shot_image = Toplevel(self) # create a next window from self
              zero_shot_image.geometry("1300x600+500+200")

              Button(zero_shot_image, text="Back to Image", width=12, command=self.zero_shot_image_back).place(x=0, rely=0)

              imggz = Image.open('Icons/1.png')
              imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              imggz = ImageTk.PhotoImage(imggz)
              cias = Button(zero_shot_image, text="Test", image=imggz, width=300, height=30, compound="left", command=self.test3 ).place(x=600, y=400)

              #--------------------------nvidia/segformer-b0-finetuned-ade-512-512-----------------

              def Delete_or_show():
               if pe.place_info() != {}:
                      pe.place_forget() 
               else:
                  pe.place(x=380, y=60)

              cr = Image.open('Icons/nvidia.png')
              cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
              cr = ImageTk.PhotoImage(cr)

              l = Button(zero_shot_image, text=" nvidia/segformer-b0-finetuned-ade-512-512", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
              pe = Label(zero_shot_image, text=" SegFormer (b0-sized) model fine-tuned on ADE20k \n \n SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper SegFormer: Simple \n and Efficient Design for Semantic Segmentation with Transformers by Xie et al. and first released in this repository. \n\nDisclaimer: The team releasing SegFormer did not write a model card for this model so \n this model card has been written by the Hugging Face team.")
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

              l = Button(zero_shot_image, text=" facebook/detr-resnet-50-panoptic", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
              pri = Label(zero_shot_image, text=" DETR (End-to-End Object Detection) model with ResNet-50 backbone \n\n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k annotated images). \n It was introduced in the paper End-to-End Object Detection with Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been \n written by the Hugging Face team.")
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

              l = Button(zero_shot_image, text=" facebook/maskformer-swin-tiny-ade", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
              gt = Label(zero_shot_image, text=" MaskFormer \n\n  MaskFormer model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). \n It was introduced in the paper Per-Pixel Classification is Not All You \n Need for Semantic Segmentation and first released in this repository. \n\n Disclaimer: The team releasing MaskFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

              l = Button(zero_shot_image, text=" nvidia/segformer-b1-finetuned-cityscapes-1024-1024", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
              gtt = Label(zero_shot_image, text=" SegFormer (b1-sized) model fine-tuned on CityScapes \n \n SegFormer model fine-tuned on CityScapes at resolution 1024x1024. It was introduced in \n the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with \n Transformers by Xie et al. and first released in this repository. \n\n Disclaimer: The team releasing SegFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

              l = Button(zero_shot_image, text=" facebook/detr-resnet-101-panoptic", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
              gttn = Label(zero_shot_image, text=" DETR (End-to-End Object Detection) model with ResNet-101 backbone \n \n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k \n annotated images). It was introduced in the paper End-to-End Object Detection with \n Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for \n this model so this model card has been written by the Hugging Face team.")
              gttn.config(bg="white") #Change backgraund color
              gttn.config(font=('arial', 11)) #Change type and size of font
              gttn.config(justify=LEFT)
              gttn.config(fg="gray") #Change text color
              gttn.place_forget()

              if(zero_shot_image):
                  self.withdraw()


              zero_shot_image.mainloop()


       def back_window3(self):
              self.iconify()
              self.deiconify()
              raiz.destroy()
              
       def test(self):

              global test
              test = Toplevel(self) # create a next window from self
              test.geometry("1300x500+500+200")
              
              Button(test, text="Back to Image", width=12, command=self.out_test).place(x=0, rely=0)  

              if(raiz):
                     self.withdraw()
              
       def zero_shot_image_back(self):
              self.iconify()
              self.deiconify()
              zero_shot_image.destroy()

       def out_test(self):
              raiz.iconify()
              raiz.deiconify()
              test.destroy()
       def test2(self):

              global test2
              test2 = Toplevel(self) # create a next window from window2
              test2.geometry("1300x500+500+200")
              
              Button(test2, text="Back to Image", width=12, command=self.out_test2).place(x=0, rely=0)  

              if(image_segme):
                     self.withdraw()
              

              image_segme.mainloop()
       
       
       def out_test2(self):
              image_segme.iconify()
              image_segme.deiconify()
              test2.destroy()
       def test3(self):

              global test3
              test3 = Toplevel(zero_shot_image) # create a next window from self
              test3.geometry("1300x500+500+200")
              
              Button(test3, text="Back to Image", width=12, command=self.out_test3).place(x=0, rely=0)  

              if(zero_shot_image):
                     zero_shot_image.withdraw()
              

              zero_shot_image.mainloop()
              
       
       def out_test3(self):
              zero_shot_image.iconify()
              zero_shot_image.deiconify()
              test3.destroy()
            
#-----------------------------------image semegtation-----------------------------------
#---------------------------------------------------------------------------------------




       def image_to_image(self):
       
          global image_to_image
          image_to_image = Toplevel(self) # create a next window from self
          image_to_image.geometry("1300x600+500+200")
          
          Button(image_to_image, text="Back to Image", width=12, command=self.image_to_image_back).place(x=0, rely=0)
       
          imggz = Image.open('Icons/1.png')
          imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
          imggz = ImageTk.PhotoImage(imggz)
          cias = Button(image_to_image, text="Test", image=imggz, width=300, height=30, compound="left", command=self.test4 ).place(x=600, y=400)
       
          #--------------------------nvidia/segformer-b0-finetuned-ade-512-512-----------------
       
          def Delete_or_show():
           if pe.place_info() != {}:
                  pe.place_forget() 
           else:
              pe.place(x=380, y=60)
       
          cr = Image.open('Icons/nvidia.png')
          cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
          cr = ImageTk.PhotoImage(cr)
       
          l = Button(image_to_image, text=" nvidia/segformer-b0-finetuned-ade-512-512", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
          pe = Label(image_to_image, text=" SegFormer (b0-sized) model fine-tuned on ADE20k \n \n SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper SegFormer: Simple \n and Efficient Design for Semantic Segmentation with Transformers by Xie et al. and first released in this repository. \n\nDisclaimer: The team releasing SegFormer did not write a model card for this model so \n this model card has been written by the Hugging Face team.")
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
       
          l = Button(image_to_image, text=" facebook/detr-resnet-50-panoptic", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
          pri = Label(image_to_image, text=" DETR (End-to-End Object Detection) model with ResNet-50 backbone \n\n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k annotated images). \n It was introduced in the paper End-to-End Object Detection with Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been \n written by the Hugging Face team.")
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
       
          l = Button(image_to_image, text=" facebook/maskformer-swin-tiny-ade", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
          gt = Label(image_to_image, text=" MaskFormer \n\n  MaskFormer model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). \n It was introduced in the paper Per-Pixel Classification is Not All You \n Need for Semantic Segmentation and first released in this repository. \n\n Disclaimer: The team releasing MaskFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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
       
          l = Button(image_to_image, text=" nvidia/segformer-b1-finetuned-cityscapes-1024-1024", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
          gtt = Label(image_to_image, text=" SegFormer (b1-sized) model fine-tuned on CityScapes \n \n SegFormer model fine-tuned on CityScapes at resolution 1024x1024. It was introduced in \n the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with \n Transformers by Xie et al. and first released in this repository. \n\n Disclaimer: The team releasing SegFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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
       
          l = Button(image_to_image, text=" facebook/detr-resnet-101-panoptic", image=rccln, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
          gttn = Label(image_to_image, text=" DETR (End-to-End Object Detection) model with ResNet-101 backbone \n \n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k \n annotated images). It was introduced in the paper End-to-End Object Detection with \n Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for \n this model so this model card has been written by the Hugging Face team.")
          gttn.config(bg="white") #Change backgraund color
          gttn.config(font=('arial', 11)) #Change type and size of font
          gttn.config(justify=LEFT)
          gttn.config(fg="gray") #Change text color
          gttn.place_forget()
       
          if(image_to_image):
              self.withdraw()
          
       
          image_to_image.mainloop()

       
       
       def image_to_image_back(self):
              self.iconify()
              self.deiconify()
              image_to_image.destroy()
              
              
       def test4(self):

              global test4
              test4 = Toplevel(image_to_image) # create a next window from self
              test4.geometry("1300x500+500+200")
              
              Button(test4, text="Back to Image", width=12, command=self.out_test4).place(x=0, rely=0)  

              if(image_to_image):
                     image_to_image.withdraw()
              

              image_to_image.mainloop()
              
              
       def out_test4(self):
              image_to_image.iconify()
              image_to_image.deiconify()
              test4.destroy()    
              
       def uncon_image_ge(self):

          global uncon_image_ge
          uncon_image_ge = Toplevel(self) # create a next window from self
          uncon_image_ge.geometry("1300x600+500+200")
          
          Button(uncon_image_ge, text="Back to Image", width=12, command=self.uncon_image_ge_back).place(x=0, rely=0)

          imggz = Image.open('Icons/1.png')
          imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
          imggz = ImageTk.PhotoImage(imggz)
          cias = Button(uncon_image_ge, text="Test", image=imggz, width=300, height=30, compound="left", command=self.test5 ).place(x=600, y=400)

          #--------------------------nvidia/segformer-b0-finetuned-ade-512-512-----------------

          def Delete_or_show():
           if pe.place_info() != {}:
                  pe.place_forget() 
           else:
              pe.place(x=380, y=60)

          cr = Image.open('Icons/nvidia.png')
          cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
          cr = ImageTk.PhotoImage(cr)

          l = Button(uncon_image_ge, text=" nvidia/segformer-b0-finetuned-ade-512-512", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
          pe = Label(uncon_image_ge, text=" SegFormer (b0-sized) model fine-tuned on ADE20k \n \n SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper SegFormer: Simple \n and Efficient Design for Semantic Segmentation with Transformers by Xie et al. and first released in this repository. \n\nDisclaimer: The team releasing SegFormer did not write a model card for this model so \n this model card has been written by the Hugging Face team.")
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

          l = Button(uncon_image_ge, text=" facebook/detr-resnet-50-panoptic", image=rc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
          pri = Label(uncon_image_ge, text=" DETR (End-to-End Object Detection) model with ResNet-50 backbone \n\n DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 panoptic (118k annotated images). \n It was introduced in the paper End-to-End Object Detection with Transformers by Carion et al. and first released in this repository. \n\n Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been \n written by the Hugging Face team.")
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

          l = Button(uncon_image_ge, text=" facebook/maskformer-swin-tiny-ade", image=rcc, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
          gt = Label(uncon_image_ge, text=" MaskFormer \n\n  MaskFormer model trained on ADE20k semantic segmentation (tiny-sized version, Swin backbone). \n It was introduced in the paper Per-Pixel Classification is Not All You \n Need for Semantic Segmentation and first released in this repository. \n\n Disclaimer: The team releasing MaskFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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

          l = Button(uncon_image_ge, text=" nvidia/segformer-b1-finetuned-cityscapes-1024-1024", image=rccl, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
          gtt = Label(uncon_image_ge, text=" SegFormer (b1-sized) model fine-tuned on CityScapes \n \n SegFormer model fine-tuned on CityScapes at resolution 1024x1024. It was introduced in \n the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with \n Transformers by Xie et al. and first released in this repository. \n\n Disclaimer: The team releasing SegFormer did not write a model card for this \n model so this model card has been written by the Hugging Face team.")
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
              self.withdraw()
          

          uncon_image_ge.mainloop()

       def uncon_image_ge_back(self):
              self.iconify()
              self.deiconify()
              uncon_image_ge.destroy()
              
       
       def test5(self):

              global test5
              test5 = Toplevel(uncon_image_ge) # create a next window from self
              test5.geometry("1300x500+500+200")
              
              Button(test5, text="Back to Image", width=12, command=self.out_test5).place(x=0, rely=0)  

              if(uncon_image_ge):
                     uncon_image_ge.withdraw()
              

              uncon_image_ge.mainloop()
              
       def out_test5(self):
              uncon_image_ge.iconify()
              uncon_image_ge.deiconify()
              test5.destroy() 

       def object_detecttion_(self):

          global object_detecttion_
          object_detecttion_ = Toplevel(self) # create a next window from self
          object_detecttion_.geometry("1300x600+500+200")
          
          Button(object_detecttion_, text="Back to Image", width=12, command=self.object_detecttion_back).place(x=0, rely=0)

          imggz = Image.open('Icons/1.png')
          imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
          imggz = ImageTk.PhotoImage(imggz)
          cias = Button(object_detecttion_, text="Test", image=imggz, width=300, height=30, compound="left", command=self.test6 ).place(x=600, y=400)

          #--------------------------nvidia/segformer-b0-finetuned-ade-512-512-----------------

          def Delete_or_show():
           if pe.place_info() != {}:
                  pe.place_forget() 
           else:
              pe.place(x=380, y=60)

          cr = Image.open('Icons/nvidia.png')
          cr = cr.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
          cr = ImageTk.PhotoImage(cr)

          l = Button(object_detecttion_, text=" nvidia/segformer-b0-finetuned-ade-512-512", image=cr, width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
          pe = Label(object_detecttion_, text=" SegFormer (b0-sized) model fine-tuned on ADE20k \n \n SegFormer model fine-tuned on ADE20k at resolution 512x512. It was introduced in the paper SegFormer: Simple \n and Efficient Design for Semantic Segmentation with Transformers by Xie et al. and first released in this repository. \n\nDisclaimer: The team releasing SegFormer did not write a model card for this model so \n this model card has been written by the Hugging Face team.")
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
              self.withdraw()
          

          object_detecttion_.mainloop()

       def object_detecttion_back(self):
              self.iconify()
              self.deiconify()
              object_detecttion_.destroy()
       
       def test6(self):

              global test6
              test6 = Toplevel(video_clasifi) # create a next window from self
              test6.geometry("1300x500+500+200")
              
              Button(test6, text="Back to Image", width=12, command=self.out_test6).place(x=0, rely=0)  

              if(video_clasifi):
                     video_clasifi.withdraw()
              

              video_clasifi.mainloop()    
       
       def out_test6():
              object_detecttion_.iconify()
              object_detecttion_.deiconify()
              test6.destroy() 
               
       def video_clasifi(self):

           global video_clasifi
           video_clasifi = Toplevel(self) # create a next window from self
           video_clasifi.geometry("1300x600+500+200")
       
           Button(video_clasifi, text="Back to Image", width=12, command=self.video_clasifi_back).place(x=0, rely=0)

           imggz = Image.open('Icons/1.png')
           imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
           imggz = ImageTk.PhotoImage(imggz)
           cias = Button(video_clasifi, text="Test", image=imggz, width=300, height=30, compound="left", command=self.test7 ).place(x=600, y=400)

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
               self.withdraw()
       

           video_clasifi.mainloop()



       def video_clasifi_back(self):
              self.iconify()
              self.deiconify()
              video_clasifi.destroy()
              
       def test7(self):

              global test7
              test7 = Toplevel(video_clasifi) # create a next window from self
              test7.geometry("1300x500+500+200")
              
              Button(test7, text="Back to Image", width=12, command=self.out_test7).place(x=0, rely=0)  

              if(video_clasifi):
                     video_clasifi.withdraw()
              

              video_clasifi.mainloop()
              
       
       
       def out_test7():
              video_clasifi.iconify()
              video_clasifi.deiconify()
              test7.destroy()
