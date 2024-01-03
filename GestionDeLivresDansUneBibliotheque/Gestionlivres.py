from ast import excepthandler
from cProfile import label
from distutils.cmd import Command
from email.mime import image
from logging import root
import operator 
from re import L      
from tkinter import * # pour importer la bibliotheque tkinter
from subprocess import call #permet dimporter le call pour ouvrir les fenetre
from tkinter import ttk, messagebox #importer des messages box  
from turtle import bgcolor, title #
 #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
import pymysql #pour récuperer la bibliotheque de la base de donnée
  
                    
class gestionlivres:  #classe formulaire
    def __init__(self,root):                   
        self.Pagegestionlivres = root  
        self.Pagegestionlivres.title("Gestionlivress")#Titre de l'application gestion livres
        self.Pagegestionlivres.geometry("1040x560+400+200")#Taille de notre Application    

        self.Pagegestionlivres.resizable(width=False, height=False) #eviter d'agrandir la fenetre  
        self.Pagegestionlivres.iconbitmap() #Icone de l'application 


        #Déclarer des variables pour ensuite les récuperer
        self.id = StringVar()
        self.titre = StringVar()
        self.auteurs = StringVar()
        self.editeurs = StringVar()
        self.collections = StringVar()
        self.Etat = StringVar()
        
        self.recherche_par= StringVar()
        self.recher= StringVar()



        self.Paneauvertdegestionlivres = Frame(self.Pagegestionlivres, bg="#bedb0d") 
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.Pagegestionlivres, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.imageicon2 = PhotoImage()
        self.btn = Button(self.Pagegestionlivres, text="",compound=LEFT,image=self.imageicon2, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn.place(x=0 , y=0) 
        # Si vous souhaitez que l’étique affiche à la fois un texte et un graphique (soit un bitmap, soit une image),
        # cette option sert à préciser l’orientation relative de l’image par rapport au texte. Les valeur peuvent-être 'left', 'right', 'center', 'bottom' ou 'top'.

        self.imageicon3 = PhotoImage()
        self.btn1 = Button(self.Pagegestionlivres,command=self.VersPageAdherents, text="",compound=LEFT,image=self.imageicon3, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn1.place(x=0 , y=140) 

        self.imageicon4 = PhotoImage()
        self.btn2 = Button(self.Pagegestionlivres,command=self.VersPageGestionDesPrets, text="",compound=LEFT,image=self.imageicon4, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn2.place(x=0 , y=280) 

        self.imageicon5 = PhotoImage()
        self.btn3 = Button(self.Pagegestionlivres, text="",command=self.BoutonDeconnexion,compound=LEFT,image=self.imageicon5, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn3.place(x=0 , y=420) 
        
        
        
        
        labelgestionlivres = Label(self.Pagegestionlivres, text="Gestion Livres", font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionlivres.place(x=0, y=100,width=190)

        labeladherents = Label(self.Pagegestionlivres, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labeladherents.place(x=0, y=240,width=190)
        
        labelgestionprets = Label(self.Pagegestionlivres, text=" Gestion Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionprets.place(x=0, y=380,width=190)

        labelsedeconnecter = Label(self.Pagegestionlivres, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelsedeconnecter.place(x=0, y=520,width=190)
        
        labelgestionlivretitre = Label(self.Pagegestionlivres, text=" Consultation des livres ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        labelgestionlivretitre.place(x=350, y=20,width=500)

        labelgestionpretstitre = Label(self.Pagegestionlivres, text="Rechercher livres disponible par:",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        labelgestionpretstitre.place(x=210, y=90,width=260)

        self.rechercherlivres= Entry(self.Pagegestionlivres,textvariable=self.recher, font= (5), bg="white")
        self.rechercherlivres.place(x=610, y=90,width=150)

        btnrecherchelivre = Button(self.Pagegestionlivres,command=self.rechercher_info ,text="Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        btnrecherchelivre.place(x=800, y=90)

        btnactualiserlivre = Button(self.Pagegestionlivres,command=self.actualiser, text="Actualiser  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        btnactualiserlivre.place(x=890, y=90)

        BoutonAjouterlivre = Button(self.Pagegestionlivres,command=self.BoutonAjouterUnlivre, text="Ajouter livre  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterlivre.place(x=215, y=500)
        
        BoutonSupprimerUnlivre = Button(self.Pagegestionlivres, command=self.SupprimerDesLivres, text="Supprimer livre ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonSupprimerUnlivre.place(x=910, y=500)
        #cursor="hand2" pour mettre en mode cliquer sur un lien   
        

        ecri_question = ttk.Combobox(self.Pagegestionlivres,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        ecri_question["values"]=("TitreLivre", "Auteurs", "Collections") 
        ecri_question.place(x=480, y=90, width=110)
        ecri_question.current(0)
        #liste titres auteurs collections

        

        
       
    
        #affichage

        frametableau = Frame(self.Pagegestionlivres, bd=5,relief=GROOVE,bg="cyan")
        frametableau.place(x=215, y=130,width=800, height=350) 

        
        scroll_x = Scrollbar(frametableau,orient=HORIZONTAL)
        scroll_y = Scrollbar(frametableau, orient=VERTICAL) 
        
        self.tableau = ttk.Treeview(frametableau,columns=("id","titres", "auteurs", "collections", "editeurs","etat"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y) 
        
        self.tableau.heading("id", text="ID")
        self.tableau.heading("titres", text="TitresLivre")
        self.tableau.heading("auteurs", text="Auteurs")
        self.tableau.heading("collections", text="Collections")
        self.tableau.heading("editeurs", text="Editeurs")
        self.tableau.heading("etat", text="Etat")

        self.tableau["show"]="headings"

        self.tableau.heading("id", text="ID")
        self.tableau.column("titres",width=80)
        self.tableau.column("auteurs",width=80)
        self.tableau.column("collections",width=80)
        self.tableau.column("editeurs",width=80)
        self.tableau.column("etat", width=80)

        self.tableau.pack(side=TOP, fill=X)
        self.tableau.pack(fill=BOTH, expand=1) #pour agrandir le tableau
        
        
        self.tableau.bind("<ButtonRelease-1>",self.information)
        self.actualiser()# Pour actualiser   
    
    def rechercher_info(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso") #Connexion à la base de données
        cur=con.cursor()
        cur.execute("select * from ajouterdeslivres where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recher.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
           self.tableau.delete(*self.tableau.get_children())
           for row in rows:
            self.tableau.insert('', END, values=row)

        con.commit()
        con.close()
    

    def VersPageAdherents(self):
        self.Pagegestionlivres.destroy()
        call(["python", "Adherents.py"]) 

    def VersPageGestionDesPrets(self):
        self.Pagegestionlivres.destroy()
        call(["python", "Gestiondesprets.py"]) 

    def BoutonAjouterUnlivre(self):
        self.Pagegestionlivres.destroy()
        call(["python", "Ajouterdeslivres.py"]) 
    
    def BoutonDeconnexion(self): #fonction deconexion pour pouvoir se deconecter qui prend pour parametre self
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.Pagegestionlivres) #message box pour pouvoir se deconnecter
        if lemessagebox == YES: #si le la colonne yes a était selectionner  
         self.Pagegestionlivres.destroy() # fermer la fenetre                             
         call(["python", "Connexion.py"]) #appeler la page connexion 
         


    def actualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso") #
        cur=con.cursor()
        cur.execute("select * from ajouterdeslivres ") #ligne sql pour récuperer la table ajoutlivres
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableau.delete(*self.tableau.get_children())
            for row in rows:
                self.tableau.insert("", END, values=row)
        con.commit()
        con.close()

    
    def information(self,ev): #fonction information pour récuperer les lignes  
        cursor_row = self.tableau.focus()
        contents = self.tableau.item(cursor_row)
        row = contents["values"]
        self.id.set(row[0]),
        self.titre.set(row[1]),
        self.auteurs.set(row[2]),
        self.editeurs.set(row[3]),
        self.collections.set(row[4]),
        self.Etat.set(row[5]),

    
    def SupprimerDesLivres(self): #fonction supprimer pour supprimer des livres   
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
                cur=con.cursor()
                cur.execute("delete from ajouterdeslivres where TitreLivre = %s", self.titre.get()) #commande delete pour supprimer une table dans la base données, self.titre.get pour récuperer le titre 
                con.commit()
                self.actualiser()
                con.close()


root =Tk()
obj = gestionlivres(root)
root.mainloop()

