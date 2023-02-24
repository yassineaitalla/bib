from tkinter import * # pour importer la bibliotheque tkinter
from ast import Delete, excepthandler 
from cProfile import label
from email.mime import image
from logging import root
from re import L 

from subprocess import call 
from tkinter import ttk, messagebox #permet d'afficher les message d'erreur qu'on appel les messages box
from turtle import bgcolor, title
#from tkcalendar import *
import pymysql  
 

class AjouterDeslivres:  # classe formulaire:
    def __init__(self,root):                   
        self.PageAjouterDesAdherents = root
        self.PageAjouterDesAdherents.title("Ajouter un Adhérent")
        self.PageAjouterDesAdherents.geometry("1040x560+400+200")
        self.PageAjouterDesAdherents.resizable(width=False, height=False)
        self.PageAjouterDesAdherents.iconbitmap()       



        self.nomAdherent = StringVar()
        self.prenomAdherent = StringVar()
        self.codepostalAdherent = StringVar()
        self.villeAdherent = StringVar()
        


        self.Paneauvertdegestionlivres = Frame(self.PageAjouterDesAdherents, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageAjouterDesAdherents, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.imageicon2 = PhotoImage()
        self.btn = Button(self.PageAjouterDesAdherents,command=self.Versgestionlivres, text="",compound=LEFT,image=self.imageicon2, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn.place(x=0 , y=0) 
        
        self.imageicon3 = PhotoImage()
        self.btn1 = Button(self.PageAjouterDesAdherents,command=self.VersPageAdherents, text="",compound=LEFT,image=self.imageicon3, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn1.place(x=0 , y=140) 

        self.imageicon4 = PhotoImage()
        self.btn2 = Button(self.PageAjouterDesAdherents,command=self.Versgestiondesprets, text="",compound=LEFT,image=self.imageicon4, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn2.place(x=0 , y=280) 

        self.imageicon5 = PhotoImage()
        self.btn3 = Button(self.PageAjouterDesAdherents,command=self.PourSedeconnecter, text="",compound=LEFT,image=self.imageicon5, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn3.place(x=0 , y=420)

        labelgestionlivres = Label(self.PageAjouterDesAdherents, text=" Gestion Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionlivres.place(x=0, y=100,width=190)

        labeladherents = Label(self.PageAjouterDesAdherents, text="Adhérents",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labeladherents.place(x=0, y=240,width=190)

        labelgestionprets = Label(self.PageAjouterDesAdherents, text=" Gestion Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionprets.place(x=0, y=380,width=190)

        labelsedeconnecter = Label(self.PageAjouterDesAdherents, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelsedeconnecter.place(x=0, y=520,width=190) 

        labelgestionlivretitre = Label(self.PageAjouterDesAdherents, text=" Ajouter un adhérent ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        labelgestionlivretitre.place(x=350, y=20,width=500)

        #label pour ajouter un livre 

        labeltitres = Label(self.PageAjouterDesAdherents, text=" Nom ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labeltitres.place(x=300, y=150,width=100)

        labelauteurs = Label(self.PageAjouterDesAdherents, text=" Prénom ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelauteurs.place(x=310, y=200,width=100)

        labelcollections = Label(self.PageAjouterDesAdherents, text=" Code postal ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelcollections.place(x=323, y=240,width=100)

        labelediteurs = Label(self.PageAjouterDesAdherents, text=" Ville ",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelediteurs.place(x=295, y=280,width=100)
        
        
        
        #Champs de saisie
        
        titre_entry= Entry(self.PageAjouterDesAdherents,textvariable=self.nomAdherent, font= (5), bg="white")
        titre_entry.place(x=500, y=150,width=150)

        auteurs_entry= Entry(self.PageAjouterDesAdherents, textvariable=self.prenomAdherent,font= (5), bg="white")
        auteurs_entry.place(x=500, y=200,width=150)

        collections_entry= Entry(self.PageAjouterDesAdherents,textvariable=self.codepostalAdherent, font= (5), bg="white")
        collections_entry.place(x=500, y=240,width=150)

        editeurs_entry= Entry(self.PageAjouterDesAdherents,textvariable=self.villeAdherent, font= (5), bg="white")
        editeurs_entry.place(x=500, y=280,width=150)

        
        
        # bouton
        BoutonAjouterUnAdherent = Button(self.PageAjouterDesAdherents, command=self.ClickBoutonAjouterUnAdherent, text="Ajouter un adhérent",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterUnAdherent.place(x=700, y=400)


    def VersPageAdherents(self): #fonction qui permet de supprimer la page
        self.PageAjouterDesAdherents.destroy()
        call(["python", "Adherents.py"])

    def Versgestiondesprets(self):
        self.PageAjouterDesAdherents.destroy()
        call(["python", "Gestiondesprets.py"])
        
    def Versgestionlivres(self):
        self.PageAjouterDesAdherents.destroy()
        call(["python", "Gestionlivres.py"])

    def PourSedeconnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageAjouterDesAdherents)
        if lemessagebox == YES:
         self.PageAjouterDesAdherents.destroy()
         call(["python", "Connexion.py"])

    
    def ClickBoutonAjouterUnAdherent(self):
        if self.nomAdherent.get()=="" or self.prenomAdherent.get()=="" or self.codepostalAdherent.get()=="" or self.villeAdherent.get()=="":
         messagebox.showerror("Erreur", "Veuillez remplir tout les champs", parent=self.PageAjouterDesAdherents) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
        
        else:
           try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
                cur=con.cursor()
                cur.execute("select * from ajouterdesadherents where nomAdherent=%s",self.nomAdherent.get())
                row= cur.fetchone()

                if row!= None:
                    messagebox.showerror("Erreur", "Cet adherent existe déja", parent=self.PageAjouterDesAdherents)
                else:
                   cur.execute("insert into ajouterdesadherents(nomAdherent, prenomAdherent, codepostalAdherent, villeAdherent) values (%s,%s,%s,%s)",
                   (
                       
                       self.nomAdherent.get(),
                       self.prenomAdherent.get(),
                       self.codepostalAdherent.get(),
                       self.villeAdherent.get(),
                       
                    ))

                   messagebox.showinfo("Succes","L'adhérent à été ajouter avec succés", parent=self.PageAjouterDesAdherents)
                   
                con.commit()
                con.close
           except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageAjouterDesAdherents)

    

root =Tk()
obj = AjouterDeslivres(root)
root.mainloop()