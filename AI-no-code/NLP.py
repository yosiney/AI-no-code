from tkinter import *
from tkinter import Tk, Button
import tkinter as tk
from PIL import Image, ImageTk

# ---------------------------------------Image------------------------------------------------------------------


class NLPWindow(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        if (self):
            parent.withdraw()

        def back_window():

            parent.iconify()
            parent.deiconify()
            self.destroy()

        self.geometry("800x500+500+200")
        self.title("AI no code")
        
        Button(self, text="Back to main", width=10, command= back_window).place(x=0, rely=0)

        self.img10 = Image.open('Icons/Icon1.png')
        self.img10 = self.img10.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img10 = ImageTk.PhotoImage(self.img10)
        Button(self, text=" Traslation",image=self.img10, width=198, height=30, compound="left", command= self.traslation).place(x=30, y=50)

        self.img11 = Image.open('Icons/Icon7.png')
        self.img11 = self.img11.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img11 = ImageTk.PhotoImage(self.img11)
        Button(self, text=" Fill-Mask", image=self.img11, width=198, height=30, compound="left", command= self.fill).place(x=250, y=50)

        self.img12 = Image.open('Icons/Icon2.png')
        self.img12 = self.img12.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img12 = ImageTk.PhotoImage(self.img12)
        Button(self, text=" Token Classification", image=self.img12, width=198, height=30, compound="left", command= self.token_cla).place(x=30, y=100)

        self.img13 = Image.open('Icons/Icon7.png')
        self.img13 = self.img13.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img13 = ImageTk.PhotoImage(self.img13)
        Button(self, text=" Sentence Similarity", image=self.img13, width=198, height=30, compound="left", command= self.sentece).place(x=250, y=100)

        self.img14 = Image.open('Icons/Icon4.png')
        self.img14 = self.img14.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img14 = ImageTk.PhotoImage(self.img14)
        Button(self, text=" Question Answering", image= self.img14, width=198, height=30, compound="left", command= self.question).place(x=30, y=150)

        self.img15 = Image.open('Icons/Icon3.png')
        self.img15 = self.img15.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img15 = ImageTk.PhotoImage(self.img15)
        Button(self, text=" Summarization", image=self.img15, width=198, height=30, compound="left", command= self.summarization).place(x=250, y=150)

        self.img16 = Image.open('Icons/Icon4.png')
        self.img16 = self.img16.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img16 = ImageTk.PhotoImage(self.img16)
        Button(self, text=" Zero-Shot-Classification", image= self.img16, width=198, height=30, compound="left", command=self.zero_shot_cla).place(x=30, y=200)

        img17 = Image.open('Icons/Icon1.png')
        img17 = img17.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img17 = ImageTk.PhotoImage(img17)
        Button(self, text=" Text Classification", image=self.img17, width=198, height=30, compound="left", command=self.text_clasif).place(x=30, y=250)

        self.img18 = Image.open('Icons/Icon6.png')
        self.img18 = self.img18.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img18 = ImageTk.PhotoImage(self.img18)
        Button(self, text=" Text2Text Generation", image=self.img18, width=198, height=30, compound="left", command=self.Text2_Ge).place(x=250, y=250)

        self.img19 = Image.open('Icons/Icon5.png')
        self.img19 = self.img19.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img19 = ImageTk.PhotoImage(self.img19)
        Button(self, text=" Text Generation", image=self.img19, width=198, height=30, compound="left", command=self.text_genera).place(x=30, y=300)

        self.img20 = Image.open('Icons/Icon1.png')
        self.img20 = self.img20.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.mg20 = ImageTk.PhotoImage(self.img20)
        Button(self, text=" Conversational", image=self.img20, width=198, height=30, compound="left", command=self.conver_nal).place(x=250, y=300)

        self.img21 = Image.open('Icons/Icon1.png')
        self.img21 = self.img21.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        self.img21 = ImageTk.PhotoImage(self.img21)
        Button(self, text=" Table Question Answering", image=self.img21, width=198, height=30, compound="left", command=self.table_question).place(x=30, y=350)

    def traslation(self):

        global traslation
        traslation = Toplevel(self)  # create a next window from window2
        traslation.geometry("1300x600+500+200")

        Button(traslation, text="Back to Image", width=12,
               command=self.trasla_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        # Resize (Height, Width)
        imggz = imggz.resize((25, 25), Image.ANTIALIAS)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(traslation, text="Test", image=imggz, width=300, height=30,
                      compound="left", command=self.test1_0).place(x=600, y=400)

        # -----------------------------------t5-small----------------------------------------------

        def Delete_or_show():
            if wi.place_info() != {}:
                wi.place_forget()
            else:
                wi.place(x=380, y=60)

        img000 = Image.open('Icons/t1.png')
        # Resize (Height, Width)
        img000 = img000.resize((25, 25), Image.ANTIALIAS)
        img000 = ImageTk.PhotoImage(img000)

        imgtrass = Image.open('Icons/trasla-1.png')
        # Resize (Height, Width)
        imgtrass = imgtrass.resize((500, 300), Image.ANTIALIAS)
        imgtrass = ImageTk.PhotoImage(imgtrass)

        l = Button(traslation, text="t5-small", image=img000, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
        wi = Label(traslation, text=" Model Description \n \n The developers of the Text-To-Text Transfer Transformer (T5) write: \n \n > With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the \n input and output are always text strings, in contrast to BERT-style models that can only \n output either a class label or a span of the input. Our text-to-text framework allows us to \n use the same model, loss function, and hyperparameters on any NLP task.", image=imgtrass, compound="top")
        wi.config(bg="white")  # Change backgraund color
        wi.config(font=('arial', 11))  # Change type and size of font
        wi.config(justify=LEFT)
        wi.config(fg="gray")  # Change text color
        wi.place_forget()

        # -----------------------------------t5-base----------------------------------------------

        def Delete_or_show():
            if tc.place_info() != {}:
                tc.place_forget()
            else:
                tc.place(x=380, y=60)

        img00 = Image.open('Icons/t1.png')
        # Resize (Height, Width)
        img00 = img00.resize((25, 25), Image.ANTIALIAS)
        img00 = ImageTk.PhotoImage(img00)

        imgtras = Image.open('Icons/trasla-1.png')
        # Resize (Height, Width)
        imgtras = imgtras.resize((500, 300), Image.ANTIALIAS)
        imgtras = ImageTk.PhotoImage(imgtras)

        l = Button(traslation, text="t5-base", image=img00, width=300, height=30,
                   compound="left", command=Delete_or_show).place(x=30, y=120)
        tc = Label(traslation, text=" Model Description \n \n The developers of the Text-To-Text Transfer Transformer (T5) write: \n \n > With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the \n input and output are always text strings, in contrast to BERT-style models that can only \n output either a class label or a span of the input. Our text-to-text framework allows us to \n use the same model, loss function, and hyperparameters on any NLP task.", image=imgtras, compound="top")
        tc.config(bg="white")  # Change backgraund color
        tc.config(font=('arial', 11))  # Change type and size of font
        tc.config(justify=LEFT)
        tc.config(fg="gray")  # Change text color
        tc.place_forget()

        # ---------------------------Helsinki-NLP/opus-mt-ROMANCE-en---------------------------------------

        def Delete_or_show():
            if tcl.place_info() != {}:
                tcl.place_forget()
            else:
                tcl.place(x=380, y=60)

        strong = Image.open('Icons/box.png')
        # Resize (Height, Width)
        strong = strong.resize((25, 25), Image.ANTIALIAS)
        strong = ImageTk.PhotoImage(strong)

        l = Button(traslation, text=" Helsinki-NLP/opus-mt-ROMANCE-en", image=strong,
                   width=300, height=30, compound="left", command=Delete_or_show).place(x=30, y=180)
        tcl = Label(traslation, text=" opus-mt-ROMANCE-en \n \nsource languages: fr,fr_BE,fr_CA,fr_FR,wa,frp,oc,ca,rm,lld,fur,lij,lmo,es,\nes_AR,es_CL,es_CO,es_CR,es_DO,es_EC,es_ES,es_GT,es_HN,es_MX,es_NI,es_PA,es_PE,es_PR,es_SV,es_UY,\nes_VE,pt,pt_br,pt_BR,pt_PT,gl,lad,an,mwl,it,it_IT,co,nap,scn,vec,sc,ro,la \n\n target languages: en \n \nOPUS readme: fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR\nes_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE \nes_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la-en \n \ndataset: opus \n\n ")

        tcl.config(bg="white")  # Change backgraund color
        tcl.config(font=('arial', 11))  # Change type and size of font
        tcl.config(justify=LEFT)
        tcl.config(fg="gray")  # Change text color
        tcl.place_forget()

        # ---------------------------Helsinki-NLP/opus-mt-de-en---------------------------------------

        def Delete_or_show():
            if tclo.place_info() != {}:
                tclo.place_forget()
            else:
                tclo.place(x=380, y=60)

        strongs = Image.open('Icons/box.png')
        # Resize (Height, Width)
        strongs = strongs.resize((25, 25), Image.ANTIALIAS)
        strongs = ImageTk.PhotoImage(strongs)

        l = Button(traslation, text=" Helsinki-NLP/opus-mt-de-en", image=strongs, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
        tclo = Label(traslation, text=" opus-mt-de-en \n\nsource languages: de\n\ntarget languages: en\n\nOPUS readme: de-en\n\ndataset: opus\n\nmodel: transformer-align\n\npre-processing: normalization + SentencePiece\n\ndownload original weights: opus-2020-02-26.zip\n\ntest set translations: opus-2020-02-26.test.txt\n\ntest set scores: opus-2020-02-26.eval.txt")

        tclo.config(bg="white")  # Change backgraund color
        tclo.config(font=('arial', 11))  # Change type and size of font
        tclo.config(justify=LEFT)
        tclo.config(fg="gray")  # Change text color
        tclo.place_forget()

        # ---------------------------Helsinki-NLP/opus-mt-fr-en---------------------------------------

        def Delete_or_show():
            if tcz.place_info() != {}:
                tcz.place_forget()
            else:
                tcz.place(x=380, y=60)

        str = Image.open('Icons/box.png')
        str = str.resize((25, 25), Image.ANTIALIAS)  # Resize (Height, Width)
        str = ImageTk.PhotoImage(str)

        l = Button(traslation, text=" Helsinki-NLP/opus-mt-fr-en", image=str, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
        tcz = Label(traslation, text=" opus-mt-fr-en \n\nsource languages: fr\n\ntarget languages: en\n\nOPUS readme: fr-en\n\ndataset: opus\n\nmodel: transformer-align\n\npre-processing: normalization + SentencePiece\n\ndownload original weights: opus-2020-02-26.zip\n\ntest set translations: opus-2020-02-26.test.txt\n\ntest set scores: opus-2020-02-26.eval.txt")

        tcz.config(bg="white")  # Change backgraund color
        tcz.config(font=('arial', 11))  # Change type and size of font
        tcz.config(justify=LEFT)
        tcz.config(fg="gray")  # Change text color
        tcz.place_forget()

        if (traslation):
            self.withdraw()

        traslation.mainloop()

# ----------------------------------------------------------------------

    def trasla_back(self):
        self.iconify()
        self.deiconify()
        traslation.destroy()

    # ---in this part put on just the button test because it a create a new window showing the results
    def test1_0(self):

        global test1_0
        test1_0 = Toplevel(traslation)  # create a next window from self
        test1_0.geometry("1300x500+500+200")

        Button(test1_0, text="Back to Image", width=12,
               command=self.out_test1_0).place(x=0, rely=0)

        if (traslation):
            traslation.withdraw()

        traslation.mainloop()

    def out_test1_0(self):
        traslation.iconify()
        traslation.deiconify()
        test1_0.destroy()

    # ----------------------------------fill-Mask---------------------------
# ----------------------------------------------------------------------
    def fill(self):

        global fill
        fill = Toplevel(self)  # create a next window from window2
        fill.geometry("1300x600+500+200")

        Button(fill, text="Back to Image", width=12,
               command=self.fill_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        # Resize (Height, Width)
        imggz = imggz.resize((25, 25), Image.ANTIALIAS)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(fill, text="Test", image=imggz, width=300, height=30,
                      compound="left", command=self.test1_1).place(x=600, y=400)

        # -----------------------------------bert-base-uncased--------------------------------------------------

        def Delete_or_show():
            if zz.place_info() != {}:
                zz.place_forget()
            else:
                zz.place(x=380, y=60)

        zzl = Image.open('Icons/box.png')
        zzl = zzl.resize((25, 25), Image.ANTIALIAS)  # Resize (Height, Width)
        zzl = ImageTk.PhotoImage(zzl)

        l = Button(fill, text=" bert-base-uncased", image=zzl, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=60)
        zz = Label(fill, text=" BERT base model (uncased) \n\n Pretrained model on English language using a masked language modeling (MLM) \n objective. It was introduced in this paper and first released in this repository. This model \n is uncased: it does not make a difference between english and English. \n\n Disclaimer: The team releasing BERT did not write a model card for this model so this \n model card has been written by the Hugging Face team.")

        zz.config(bg="white")  # Change backgraund color
        zz.config(font=('arial', 11))  # Change type and size of font
        zz.config(justify=LEFT)
        zz.config(fg="gray")  # Change text color
        zz.place_forget()

        # -----------------------------------xlm-roberta-base-----------------------------------------------------

        def Delete_or_show():
            if zu.place_info() != {}:
                zu.place_forget()
            else:
                zu.place(x=380, y=60)

        zul = Image.open('Icons/box.png')
        zul = zul.resize((25, 25), Image.ANTIALIAS)  # Resize (Height, Width)
        zul = ImageTk.PhotoImage(zul)

        l = Button(fill, text=" xlm-roberta-base", image=zul, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=120)
        zu = Label(fill, text=" XLM-RoBERTa (base-sized model) \n\n XLM-RoBERTa model pre-trained on 2.5TB of filtered CommonCrawl data containing 100 \n languages. It was introduced in the paper Unsupervised Cross-lingual Representation \n Learning at Scale by Conneau et al. and first released in this repository. \n\n Disclaimer: The team releasing XLM-RoBERTa did not write a model card for this model \n so this model card has been written by the Hugging Face team.")

        zu.config(bg="white")  # Change backgraund color
        zu.config(font=('arial', 11))  # Change type and size of font
        zu.config(justify=LEFT)
        zu.config(fg="gray")  # Change text color
        zu.place_forget()

        # -----------------------------------roberta-base-----------------------------------------------------

        def Delete_or_show():
            if uu.place_info() != {}:
                uu.place_forget()
            else:
                uu.place(x=380, y=60)

        zull = Image.open('Icons/box.png')
        zull = zull.resize((25, 25), Image.ANTIALIAS)  # Resize (Height, Width)
        zull = ImageTk.PhotoImage(zull)

        l = Button(fill, text=" roberta-base", image=zull, width=300, height=30,
                   compound="left", command=Delete_or_show).place(x=30, y=180)
        uu = Label(fill, text=" XLM-RoBERTa (base-sized model) \n\n XLM-RoBERTa model pre-trained on 2.5TB of filtered CommonCrawl data containing 100 \n languages. It was introduced in the paper Unsupervised Cross-lingual Representation \n Learning at Scale by Conneau et al. and first released in this repository. \n\n Disclaimer: The team releasing XLM-RoBERTa did not write a model card for this model \n so this model card has been written by the Hugging Face team.")

        uu.config(bg="white")  # Change backgraund color
        uu.config(font=('arial', 11))  # Change type and size of font
        uu.config(justify=LEFT)
        uu.config(fg="gray")  # Change text color
        uu.place_forget()

        # -----------------------------------bert-base-multilingual-cased-----------------------------------------------------

        def Delete_or_show():
            if ut.place_info() != {}:
                ut.place_forget()
            else:
                ut.place(x=380, y=60)

        zulli = Image.open('Icons/box.png')
        # Resize (Height, Width)
        zulli = zulli.resize((25, 25), Image.ANTIALIAS)
        zulli = ImageTk.PhotoImage(zulli)

        l = Button(fill, text=" bert-base-multilingual-cased", image=zulli, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=240)
        ut = Label(fill, text=" BERT multilingual base model (cased) \n\n Pretrained model on the top 104 languages with the largest Wikipedia using a masked \n language modeling (MLM) objective. It was introduced in this paper and first released in \n  this repository. This model is case sensitive: it makes a difference between english and English. \n\n Disclaimer: The team releasing BERT did not write a model card for this model so this \n  model card has been written by the Hugging Face team.")

        ut.config(bg="white")  # Change backgraund color
        ut.config(font=('arial', 11))  # Change type and size of font
        ut.config(justify=LEFT)
        ut.config(fg="gray")  # Change text color
        ut.place_forget()

        # -----------------------------------distilbert-base-uncased-----------------------------------------------------

        def Delete_or_show():
            if utt.place_info() != {}:
                utt.place_forget()
            else:
                utt.place(x=380, y=60)

        zulliz = Image.open('Icons/box.png')
        # Resize (Height, Width)
        zulliz = zulliz.resize((25, 25), Image.ANTIALIAS)
        zulliz = ImageTk.PhotoImage(zulliz)

        l = Button(fill, text=" distilbert-base-uncased", image=zulliz, width=300,
                   height=30, compound="left", command=Delete_or_show).place(x=30, y=300)
        utt = Label(fill, text=" DistilBERT base model (uncased) \n\n This model is a distilled version of the BERT base model. It was introduced in this paper. \n The code for the distillation process can be found here. This model is uncased: it does not  \n make a difference between english and English.")

        utt.config(bg="white")  # Change backgraund color
        utt.config(font=('arial', 11))  # Change type and size of font
        utt.config(justify=LEFT)
        utt.config(fg="gray")  # Change text color
        utt.place_forget()

        if (fill):
            self.withdraw()

        fill.mainloop()
# ----------------------------------------------------------------------

    def fill_back(self):
        self.iconify()
        self.deiconify()
        fill.destroy()

    def test1_1(self):

        global test1_1
        test1_1 = Toplevel(fill)  # create a next window from self
        test1_1.geometry("1300x500+500+200")

        Button(test1_1, text="Back to Image", width=12,
               command=self.out_test1_1).place(x=0, rely=0)

        if (fill):
            fill.withdraw()

        fill.mainloop()

    def out_test1_1(self):
        fill.iconify()
        fill.deiconify()
        test1_1.destroy()

    
 #----------------------------------Token Classification---------------
#----------------------------------------------------------------------
    def token_cla(self):

        global token_cla
        token_cla = Toplevel(self) # create a next window from window2
        token_cla.geometry("1300x600+500+200")

        Button(token_cla, text="Back to Image", width=12, command= self.token_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(token_cla, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_2 ).place(x=600, y=400)

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
            self.withdraw()

        token_cla.mainloop()

#----------------------------------------------------------------------

    def token_back(self):
        self.iconify()
        self.deiconify()
        token_cla.destroy()
        
    def test1_2(self):

        global test1_2
        test1_2 = Toplevel(token_cla) # create a next window from self
        test1_2.geometry("1300x500+500+200")
        
        Button(test1_2, text="Back to Image", width=12, command=self.out_test1_2).place(x=0, rely=0)  

        if(token_cla):
            token_cla.withdraw()
        

        token_cla.mainloop()
        
    def out_test1_2(self):
        token_cla.iconify()
        token_cla.deiconify()
        test1_2.destroy()
        
#----------------------------------sentence Similarity-----------------
#----------------------------------------------------------------------
    def sentece(self):

        global sentece
        sentece = Toplevel(self) # create a next window from window2
        sentece.geometry("1300x600+500+200")

        Button(sentece, text="Back to Image", width=12, command= self.sentece_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(sentece, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_3 ).place(x=600, y=400)

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
            self.withdraw()

        sentece.mainloop()
#----------------------------------------------------------------------

    def sentece_back(self):
        self.iconify()
        self.deiconify()
        sentece.destroy()

    def test1_3(self):

        global test1_3
        test1_3 = Toplevel(token_cla) # create a next window from self
        test1_3.geometry("1300x500+500+200")
        
        Button(test1_3, text="Back to Image", width=12, command= self.out_test1_3).place(x=0, rely=0)  

        if(token_cla):
            token_cla.withdraw()
        

        token_cla.mainloop()
        
    def out_test1_3(self):
        sentece.iconify()
        sentece.deiconify()
        test1_3.destroy()

#----------------------------------Question answering------------------
#----------------------------------------------------------------------
    def question(self):

        global question
        question = Toplevel(self) # create a next window from window2
        question.geometry("1300x600+500+200")

        Button(question, text="Back to Image", width=12, command= self.quest_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(question, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_4 ).place(x=600, y=400)

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
            self.withdraw()

        question.mainloop()
#----------------------------------------------------------------------

    def quest_back(self):
        self.iconify()
        self.deiconify()
        question.destroy()
        
    
    def test1_4(self):

        global test1_4
        test1_4 = Toplevel(question) # create a next window from self
        test1_4.geometry("1300x500+500+200")
        
        Button(test1_4, text="Back to Image", width=12, command= self.out_test1_4).place(x=0, rely=0)  

        if(question):
            question.withdraw()
        

        question.mainloop()


    def out_test1_4(self): 
        question.iconify()
        question.deiconify()
        test1_4.destroy()
    #----------------------------------Summarization-----------------------
#----------------------------------------------------------------------
    def summarization(self):    

        global summarization
        summarization = Toplevel(self) # create a next window from window2
        summarization.geometry("1300x600+500+200")

        Button(summarization, text="Back to Image", width=12, command= self.summari_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(summarization, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_5 ).place(x=600, y=400)

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
            self.withdraw()

        summarization.mainloop()
#----------------------------------------------------------------------

    def summari_back(self):
        self.iconify()
        self.deiconify()
        summarization.destroy()
    
    def test1_5(self):

        global test1_5
        test1_5 = Toplevel(summarization) # create a next window from self
        test1_5.geometry("1300x500+500+200")
        
        Button(test1_5, text="Back to Image", width=12, command= self.out_test1_5).place(x=0, rely=0)  

        if(summarization):
            summarization.withdraw()
        

        summarization.mainloop()
    
    def out_test1_5(self):
        summarization.iconify()
        summarization.deiconify()
        test1_5.destroy()
        
    #----------------------------------zero-shot-classfication-------------
#----------------------------------------------------------------------
    def zero_shot_cla(self):

        global zero_shot_cla
        zero_shot_cla = Toplevel(self) # create a next window from window2
        zero_shot_cla.geometry("1300x600+500+200")

        Button(zero_shot_cla, text="Back to Image", width=12, command= self.zero_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(zero_shot_cla, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_8 ).place(x=600, y=400)

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
            self.withdraw()

        zero_shot_cla.mainloop()

#----------------------------------------------------------------------

    def zero_back(self):
        self.iconify()
        self.deiconify()
        zero_shot_cla.destroy()
    
    def test1_8(self):

        global test1_8
        test1_8 = Toplevel(zero_shot_cla) # create a next window from self
        test1_8.geometry("1300x500+500+200")
        
        Button(test1_8, text="Back to Image", width=12, command= self.out_test1_8).place(x=0, rely=0)  

        if(zero_shot_cla):
            zero_shot_cla.withdraw()
        

        zero_shot_cla.mainloop()
                
    def out_test1_8(self):
        zero_shot_cla.iconify()
        zero_shot_cla.deiconify()
        test1_8.destroy()
        
    #----------------------------------text classification-----------------
#----------------------------------------------------------------------
    def text_clasif(self):

        global text_clasif
        text_clasif = Toplevel(self) # create a next window from window2
        text_clasif.geometry("1300x600+500+200")

        Button(text_clasif, text="Back to Image", width=12, command= self.text_cla_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(text_clasif, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_6 ).place(x=600, y=400)

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
            self.withdraw()

        text_clasif.mainloop()

#----------------------------------------------------------------------

        
    def text_cla_back(self):
        self.iconify()
        self.deiconify()
        text_clasif.destroy()
        
    def test1_6(self):

        global test1_6
        test1_6 = Toplevel(text_clasif) # create a next window from self
        test1_6.geometry("1300x500+500+200")
        
        Button(test1_6, text="Back to Image", width=12, command= self.out_test1_6).place(x=0, rely=0)  

        if(text_clasif):
            text_clasif.withdraw()
        

        text_clasif.mainloop()
        
    def out_test1_6(self):
        text_clasif.iconify()
        text_clasif.deiconify()
        test1_6.destroy()
        
    #----------------------------------Text2Text Generation----------------
#----------------------------------------------------------------------
    def Text2_Ge(self):

        global Text2_Ge
        Text2_Ge = Toplevel(self) # create a next window from window2
        Text2_Ge.geometry("1300x600+500+200")

        Button(Text2_Ge, text="Back to Image", width=12, command= self.text2_ge_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(Text2_Ge, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_9 ).place(x=600, y=400)

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
            self.withdraw()

        Text2_Ge.mainloop()
#----------------------------------------------------------------------


    def text2_ge_back(self):
        self.iconify()
        self.deiconify()
        Text2_Ge.destroy()
        
    def test1_9(self):

        global test1_9
        test1_9 = Toplevel(Text2_Ge) # create a next window from self
        test1_9.geometry("1300x500+500+200")
        
        Button(test1_9, text="Back to Image", width=12, command= self.out_test1_9).place(x=0, rely=0)  

        if(Text2_Ge):
            Text2_Ge.withdraw()
        
        Text2_Ge.mainloop()
    
    def out_test1_9(self):
        Text2_Ge.iconify()
        Text2_Ge.deiconify()
        test1_9.destroy()
        
#----------------------------------text generation--------------------
#----------------------------------------------------------------------

    def text_genera(self):

        global text_genera
        text_genera = Toplevel(self) # create a next window from window2
        text_genera.geometry("1300x600+500+200")

        Button(text_genera, text="Back to Image", width=12, command= self.text_gene_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(text_genera, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_7 ).place(x=600, y=400)
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
            self.withdraw()

        text_genera.mainloop()

#----------------------------------------------------------------------

    def text_gene_back(self):
        self.iconify()
        self.deiconify()
        text_genera.destroy()

    def test1_7(self):

        global test1_7
        test1_7 = Toplevel(text_genera) # create a next window from self
        test1_7.geometry("1300x500+500+200")
        
        Button(test1_7, text="Back to Image", width=12, command= self.out_test1_7).place(x=0, rely=0)  

        if(text_genera):
            text_genera.withdraw()
        

        text_genera.mainloop()
    
    
    def out_test1_7(self):
        text_genera.iconify()
        text_genera.deiconify()
        test1_7.destroy()


    #----------------------------------------------------------------------
    def conver_nal(self):

        global conver_nal
        conver_nal = Toplevel(self) # create a next window from window2
        conver_nal.geometry("1300x600+500+200")
        
        Button(conver_nal, text="Back to Image", width=12, command= self.conver_back).place(x=0, rely=0)
        
        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(conver_nal, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_10 ).place(x=600, y=400)

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
            self.withdraw()
        
        conver_nal.mainloop()
    #----------------------------------------------------------------------
    
    def conver_back(self):
        self.iconify()
        self.deiconify()
        conver_nal.destroy()

    

    def test1_10(self):

        global test1_10
        test1_10 = Toplevel(conver_nal) # create a next window from self
        test1_10.geometry("1300x500+500+200")
        
        Button(test1_10, text="Back to Image", width=12, command=self.out_test1_10).place(x=0, rely=0)  

        if(conver_nal):
            conver_nal.withdraw()
        
        conver_nal.mainloop()
    
    def out_test1_10(self):
        conver_nal.iconify()
        conver_nal.deiconify()
        test1_10.destroy()



#----------------------------------table question answering------------
#----------------------------------------------------------------------
    def table_question(self):

        global table_question
        table_question = Toplevel(self) # create a next window from window2
        table_question.geometry("1300x600+500+200")

        Button(table_question, text="Back to Image", width=12, command= self.table_question_back).place(x=0, rely=0)

        imggz = Image.open('Icons/1.png')
        imggz = imggz.resize((25, 25), Image.ANTIALIAS) # Resize (Height, Width)
        imggz = ImageTk.PhotoImage(imggz)
        cias = Button(table_question, text="Test", image=imggz, width=300, height=30, compound="left", command= self.test1_11 ).place(x=600, y=400)

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
            self.withdraw()

        table_question.mainloop()
    
        
    def table_question_back(self):
        self.iconify()
        self.deiconify()
        table_question.destroy()

    def out_test1_11(self):
        table_question.iconify()
        table_question.deiconify()
        test1_11.destroy()

    def test1_11(self):

        global test1_11
        test1_11 = Toplevel(table_question) # create a next window from self
        test1_11.geometry("1300x500+500+200")
        
        Button(test1_11, text="Back to Image", width=12, command= self.out_test1_11).place(x=0, rely=0)  

        if(table_question):
            table_question.withdraw()
        
        table_question.mainloop()   