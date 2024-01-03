from ast import Delete, excepthandler
from cProfile import label
from email.mime import image
from logging import root
from re import L
from tkinter import * 
from subprocess import call #pour importer la bibliotheque tkinter
from tkinter import ttk, messagebox
from turtle import bgcolor, title #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
#from tkcalendar import *
import pymysql 
     

class ajoutlivres:  # classe formulaire:
    def __init__(self,root):                   
        self.PageAjouterDesLivres = root
        self.PageAjouterDesLivres.title("Ajouter un livre") #titre Ajouter un livre
        self.PageAjouterDesLivres.geometry("1040x560+400+200") #taille de l'application
        self.PageAjouterDesLivres.resizable(width=False, height=False)# eviter d'agrandir la fenetre
        self.PageAjouterDesLivres.iconbitmap()#importer l'icone 


        #on déclare des variables pour ensuite les récuperer
        self.TitreLivre = StringVar()
        self.Auteurs = StringVar()
        self.Editeurs = StringVar()
        self.Collections = StringVar()
        self.Etat = StringVar()

      
        


        #panneau vert gestion livres
        self.Paneauvertdegestionlivres = Frame(self.PageAjouterDesLivres, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        #panneau orange
        Paneauorangedegestionlivres = Frame(self.PageAjouterDesLivres, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.imageicon2 = PhotoImage()
        self.btn = Button(self.PageAjouterDesLivres,command=self.VersGestionlivres, text="",compound=LEFT,image=self.imageicon2, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn.place(x=0 , y=0) 
        
        self.imageicon3 = PhotoImage()
        self.btn1 = Button(self.PageAjouterDesLivres,command=self.VersAdherents ,text="",compound=LEFT,image=self.imageicon3, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn1.place(x=0 , y=140) 

        self.imageicon4 = PhotoImage()
        self.btn2 = Button(self.PageAjouterDesLivres,command=self.VersGestiondesprets, text="",compound=LEFT,image=self.imageicon4, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn2.place(x=0 , y=280) 

        self.imageicon5 = PhotoImage()
        self.btn3 = Button(self.PageAjouterDesLivres, text="",command=self.PourSedeconnecter,compound=LEFT,image=self.imageicon5, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn3.place(x=0 , y=420)

        labelgestionlivres = Label(self.PageAjouterDesLivres, text=" Gestion Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionlivres.place(x=0, y=100,width=190)

        labeladherents = Label(self.PageAjouterDesLivres, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labeladherents.place(x=0, y=240,width=190)

        labelgestionprets = Label(self.PageAjouterDesLivres, text=" Gestion Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionprets.place(x=0, y=380,width=190)

        labelsedeconnecter = Label(self.PageAjouterDesLivres, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelsedeconnecter.place(x=0, y=520,width=190) 

        labelgestionlivretitre = Label(self.PageAjouterDesLivres, text=" Ajouter un livre ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        labelgestionlivretitre.place(x=350, y=20,width=500)

        #label = les titres 

        labeltitres = Label(self.PageAjouterDesLivres, text=" Titre ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labeltitres.place(x=300, y=150,width=100)

        labelauteurs = Label(self.PageAjouterDesLivres, text=" Auteur ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelauteurs.place(x=310, y=200,width=100)

        labelcollections = Label(self.PageAjouterDesLivres, text=" Collection ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelcollections.place(x=323, y=240,width=100)

        labelediteurs = Label(self.PageAjouterDesLivres, text=" Editeur ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelediteurs.place(x=312, y=280,width=100)
        
      
        
        
        #ENTRY = Champs de saisie

        TitreLivre= Entry(self.PageAjouterDesLivres,textvariable=self.TitreLivre, font= (5), bg="white")
        TitreLivre.place(x=500, y=150,width=150)

        Auteurs= Entry(self.PageAjouterDesLivres, textvariable=self.Auteurs,font= (5), bg="white")
        Auteurs.place(x=500, y=200,width=150)

        Collections= Entry(self.PageAjouterDesLivres,textvariable=self.Collections, font= (5), bg="white")
        Collections.place(x=500, y=240,width=150)

        Editeurs= Entry(self.PageAjouterDesLivres,textvariable=self.Editeurs, font= (5), bg="white")
        Editeurs.place(x=500, y=280,width=150)

       
        
        # bouton
        BoutonAjouterUnlivre = Button(self.PageAjouterDesLivres,command=self.ClickAjouterUnLivre, text="Ajouter",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterUnlivre.place(x=700, y=400)


    def VersAdherents(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "Adherents.py"])

    def VersGestiondesprets(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "Gestiondesprets.py"])
        
    def VersGestionlivres(self):
        self.PageAjouterDesLivres.destroy()
        call(["python", "Gestionlivres.py"])
    
    def PourSedeconnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageAjouterDesLivres)
        if lemessagebox == YES:
         self.PageAjouterDesLivres.destroy()
         call(["python", "Connexion.py"])

    
    def ClickAjouterUnLivre(self):
        if self.TitreLivre.get()=="" or self.Auteurs.get()=="" or self.Editeurs.get()=="" or self.Collections.get()=="" or self.Etat.get()=="":
         messagebox.showerror("Erreur", "Veuillez remplir tout les champs", parent=self.PageAjouterDesLivres) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
        
        try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
                cur=con.cursor()
                cur.execute("select * from ajouterdeslivres where TitreLivre=%s",self.TitreLivre.get())
                row= cur.fetchone()

                if row!= None:
                    messagebox.showerror("Erreur", "Ce livre existe deja", parent=self.PageAjouterDesLivres)
                else:
                   cur.execute("insert into ajouterdeslivres (TitreLivre, Auteurs, Collections, Editeurs,Etat) values (%s,%s,%s,%s,%s)",
                   (
                    
                       self.TitreLivre.get(),
                       self.Auteurs.get(),
                       self.Editeurs.get(),
                       self.Collections.get(),
                       self.Etat.get()
                       
                    ))

                   messagebox.showinfo("Succes","Votre livre à été gérée", parent=self.PageAjouterDesLivres)
                   
                con.commit()
                con.close
        except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageAjouterDesLivres)
                
    

      

root =Tk()
obj = ajoutlivres(root)
root.mainloop()