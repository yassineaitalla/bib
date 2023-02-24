from ast import excepthandler
from cProfile import label
from email.mime import image
from logging import root            # pour importer la bibliotheque tkinter
from re import L
from tkinter import * 
from subprocess import call

                       
 


from tkinter import ttk, messagebox
from turtle import bgcolor, title #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite

import pymysql 
      
                    
class adherents:  # classe formulaire:
    def __init__(self,root):                   
        self.PageAdherents = root
        self.PageAdherents.title("Adherents")
        self.PageAdherents.geometry("1040x560+400+200")
        self.PageAdherents.resizable(width=False, height=False)
        self.PageAdherents.iconbitmap()
        
        self.id = StringVar()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.codepostal= StringVar()
        self.ville = StringVar()


        self.Paneauvertdegestionlivres = Frame(self.PageAdherents, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageAdherents, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.imageicon2 = PhotoImage()
        self.btn = Button(self.PageAdherents, command=self.VersGestionsLivres,text="",compound=LEFT,image=self.imageicon2, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn.place(x=0 , y=0) 
        
        self.imageicon3 = PhotoImage()
        self.btn1 = Button(self.PageAdherents, text="",compound=LEFT,image=self.imageicon3, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn1.place(x=0 , y=140) 

        self.imageicon4 = PhotoImage()
        self.btn2 = Button(self.PageAdherents, command=self.VersGestionsdesPrets,text="",compound=LEFT,image=self.imageicon4, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn2.place(x=0 , y=280) 

        self.imageicon5 = PhotoImage()
        self.btn3 = Button(self.PageAdherents, text="",command=self.PourSeDeconnecter,compound=LEFT,image=self.imageicon5, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn3.place(x=0 , y=420)

        # command  ------> Réecuperer la fontion qu'oncrée
        # coupound ------> L’étique affiche à la fois un texte et un graphique 
        
        labelgestionlivres = Label(self.PageAdherents, text=" Gestion Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionlivres.place(x=0, y=100,width=190)

        labeladherents = Label(self.PageAdherents, text=" Gestion Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labeladherents.place(x=0, y=240,width=190)

        labelgestionprets = Label(self.PageAdherents, text=" Gestion Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionprets.place(x=0, y=380,width=190)

        labelsedeconnecter = Label(self.PageAdherents, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelsedeconnecter.place(x=0, y=520,width=190)

        labelgestionADHtitre = Label(self.PageAdherents, text=" Gestion Adhérents ",font =("algarian", 20,"bold"), bg="#ff7f00", fg="black")
        labelgestionADHtitre.place(x=470, y=20,width=250)

        btnajouterlivre = Button(self.PageAdherents, text="Ajout d'adhérent",command=self.AjouterunAdherent,cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        btnajouterlivre.place(x=215, y=500)

        BoutonSupprimerAdherent = Button(self.PageAdherents, command=self.SupprimerunAdherent,text="Supprimer Adhérent",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonSupprimerAdherent.place(x=890, y=500)



        #affichage

        frametableau = Frame(self.PageAdherents, bd=5,relief=GROOVE,bg="cyan")
        frametableau.place(x=215, y=130,width=800, height=350)

        scroll_x = Scrollbar(frametableau,orient=HORIZONTAL)
        scroll_y = Scrollbar(frametableau, orient=VERTICAL)
        
        self.tableau = ttk.Treeview(frametableau,columns=("id","nomAdherent", "prenomAdherent", "codepostalAdherent","villeAdherent"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y) 
        self.tableau.selection
        
        self.tableau.heading("id", text="idAdherent")
        self.tableau.heading("nomAdherent", text="nomAdherent")
        self.tableau.heading("prenomAdherent", text="prenomAdherent")
        
        self.tableau.heading("codepostalAdherent", text="codepostalAdherent")
        self.tableau.heading("villeAdherent", text="villeAdherent")

        self.tableau["show"]="headings"

        self.tableau.column("id",width=80)
        self.tableau.column("nomAdherent",width=80)
        self.tableau.column("prenomAdherent",width=80)
        self.tableau.column("codepostalAdherent",width=80)
        self.tableau.column("villeAdherent", width=80)

        self.tableau.pack(side=TOP, fill=X,)
        self.tableau.pack(fill=BOTH, expand=1)
        
        
        self.tableau.bind("<ButtonRelease-1>",self.information) # le self information est important si on souhaite faire la meme vhose ailleurs
        self.actualiser()
    
    def AjouterunAdherent(self):
        self.PageAdherents.destroy()
        call(["python", "ajouterdesadherents.py"]) 

    

    def actualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
        cur=con.cursor()
        cur.execute("select * from ajoutadesadherents ")
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableau.delete(*self.tableau.get_children())
            for row in rows:
                self.tableau.insert("", END, values=row)
        

    def VersGestionsLivres(self):
        self.PageAdherents.destroy()
        call(["python", "Gestionlivres.py"]) 

    
    def VersGestionsdesPrets(self):
        self.PageAdherents.destroy()
        call(["python", "GestionDesprets.py"]) 

    
    def PourSeDeconnecter(self):
        
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageAdherents)
        if lemessagebox == YES:
         self.PageAdherents.destroy()                           
         call(["python", "Connexion.py"])
        
        
      

    def information(self,ev):
        cursor_row = self.tableau.focus()
        contents = self.tableau.item(cursor_row)
        row = contents["values"]
        
        self.id.set(row[0]),
        self.nom.set(row[1]),
        self.prenom.set(row[2]),
        self.codepostal.set(row[3]),
        self.ville.set(row[4]),
    
    def actualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
        cur=con.cursor()
        cur.execute("select * from ajouterdesadherents ")
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableau.delete(*self.tableau.get_children())
            for row in rows:
                self.tableau.insert("", END, values=row)
                
                

        con.commit()
        con.close()



        
    def SupprimerunAdherent(self):
                
        
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
        cur=con.cursor()
        cur.execute("delete from ajouterdesadherents where villeAdherent = %s", self.ville.get())
        con.commit()
        self.actualiser ()
                
        con.close()

          

root =Tk()
obj = adherents(root)
root.mainloop()