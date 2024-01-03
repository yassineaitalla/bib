from tkinter import * #importer la bibliotheque tkinter
import tkinter as tk  #
from tkinter import ttk, messagebox #bibliotheque pour afficher nos message d'erreur dans l'application
from turtle import bgcolor, title #permetre de gerer les selections et les message derreur  afficher ou de securite
from tkcalendar import * #Bibliothéque pour importer les calendrier 
import pymysql #bibliotheque pour interagir avec la base de données
#import os #faire des actions diretement au niveau du systeme  
from subprocess import call   #bibliotheque pour pouvoir changer de page  


                    
class gestionprets:  # classe formulaire:
    def __init__(self,root):                   
        self.PageGestiondesprets = root #changer
        self.PageGestiondesprets.title("Gestionprets") #titre de la fenetre 
        self.PageGestiondesprets.geometry("1040x560+400+200")#pour gerer la taille de l'application
        
        self.PageGestiondesprets.resizable(width=False, height=False)#Pour eviter d'agrandir notre application
        self.PageGestiondesprets.iconbitmap() #pour gerer l'icone de notre application
       
        
        
        self.var_dateemprunt = StringVar()  # on declare des variables pour ensuite les recuperer
        self.var_nomdelhadherent = StringVar()  # Mémorise une chaîne de caractères; sa valeur par défaut est ''
        self.var_livre = StringVar()
        self.var_dateretour = StringVar()
        self.recherche_par = StringVar()
        self.recherche = StringVar()
        self.nomdelhadherent_list=[]
        self.four_list=[]
        self.list_nomdelhadherent_four()  

        
        


        self.Paneauvertdegestionlivres = Frame(self.PageGestiondesprets, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageGestiondesprets, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.imageicon2 = PhotoImage()
        self.BoutonPourAllerVersGestionLivres = Button(self.PageGestiondesprets,command=self.VersGestionLivres, text="",compound=LEFT,image=self.imageicon2, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionLivres.place(x=0 , y=0) 
        
        self.imageicon3 = PhotoImage()
        self.BoutonPourAllerVersAdherents = Button(self.PageGestiondesprets,command=self.VersAdherents, text="",compound=LEFT,image=self.imageicon3, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersAdherents.place(x=0 , y=140) 

        self.imageicon4 = PhotoImage()
        self.btn2 = Button(self.PageGestiondesprets, text="",compound=LEFT,image=self.imageicon4, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.btn2.place(x=0 , y=280) 

        self.imageicon5 = PhotoImage()

        self.BoutonPourSedeconnecter = Button(self.PageGestiondesprets, text="",command=self.PourSeDeConnecter,compound=LEFT,image=self.imageicon5, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourSedeconnecter.place(x=0 , y=420) 

        #Labels
        
        labelgestionlivres = Label(self.PageGestiondesprets, text=" Gestion Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionlivres.place(x=0, y=100,width=190)

        labeladherents = Label(self.PageGestiondesprets, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labeladherents.place(x=0, y=240,width=190)

        labelgestionprets = Label(self.PageGestiondesprets, text=" Gestion Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelgestionprets.place(x=0, y=380,width=190)

        labelsedeconnecter = Label(self.PageGestiondesprets, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        labelsedeconnecter.place(x=0, y=520,width=190)

        labelgestionpretstitre = Label(self.PageGestiondesprets, text=" Gestion Prêts ",font =("algarian", 20,"bold"), bg="#ff7f00", fg="black")
        labelgestionpretstitre.place(x=470, y=20,width=210)

        labelgestionpretstitre = Label(self.PageGestiondesprets, text=" Rechercher par :",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        
        labelgestionpretstitre.place(x=190, y=90,width=210)

        

        ecri_question = ttk.Combobox(self.PageGestiondesprets,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        ecri_question["values"]=("ID", "Nom") 
        ecri_question.place(x=370, y=87, width=110) #.place pour la position du ttk.combobox 
        ecri_question.current(0)


        


        self.ChampsDesaisiePourRechercherDeslivres= Entry(self.PageGestiondesprets,textvariable=self.recherche ,font= (5), bg="white")
        self.ChampsDesaisiePourRechercherDeslivres.place(x=500, y=90,width=150)

        BoutonPourRechercherUnLivre = Button(self.PageGestiondesprets,command=self.rechercher_info, text="Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonPourRechercherUnLivre.place(x=700, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonActualiser = Button(self.PageGestiondesprets,command=self.BoutonActualiser, text="Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=790, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonPourAjouterUnlivre = Button(self.PageGestiondesprets,command=self.PageEmprunt, text="Emprunter un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black", )
        BoutonPourAjouterUnlivre.place(x=215, y=500)

        
        

        BoutonRetournerUnLivre = Button(self.PageGestiondesprets,command=self.SupprimerDesLivres, text="Retourner un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonRetournerUnLivre.place(x=890, y=500)
        #cursor pour mettre la main quand on clique sur le bouton 
        #affichage

        ###################################
                                         
        ###################################

        frametableau = Frame(self.PageGestiondesprets, bd=5,relief=GROOVE,bg="green") #self.root pour mettre le table sur cette frame la 
        frametableau.place(x=215, y=130,width=800, height=350)

        scroll_x = Scrollbar(frametableau,orient=HORIZONTAL)
        scroll_y = Scrollbar(frametableau, orient=VERTICAL)
        
        self.tableau = ttk.Treeview(frametableau,columns=("id", "nom", "livre","date_emprunt","date_retour"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y) 

        self.tableau.heading("id", text="ID")
        self.tableau.heading("nom", text="Nom")
        self.tableau.heading("livre", text="Livre emprunter")
        #self.tableau.heading("quantite", text="Quantité")
        self.tableau.heading("date_emprunt", text="Emprunter le")
        self.tableau.heading("date_retour", text="Retour le")



        

        self.tableau["show"]="headings"

        self.tableau.column("id",  width=80)
        self.tableau.column("nom", width=80)
        self.tableau.column("livre", width=80)
        #self.tableau.column("quantite", width=80)
        self.tableau.column("date_emprunt", width=80)
        self.tableau.column("date_retour", width=80)


        self.tableau.pack(fill=BOTH, expand=1)
        
        
        self.tableau.bind("<ButtonRelease-1>",self.information)
        self.actualiser()

    def BoutonActualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
        cur=con.cursor()
        cur.execute("select * from emprunterdeslivres ")
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableau.delete(*self.tableau.get_children())
            for row in rows:
                self.tableau.insert("", END, values=row)
    


    
    def rechercher_info(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso") # connexion a la base de donnes
        cur=con.cursor()        
        cur.execute("select * from emprunterdeslivres where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
           self.tableau.delete(*self.tableau.get_children())
           for row in rows:
            self.tableau.insert('', END, values=row)
        con.commit()
        con.close()




    def SupprimerDesLivres(self): # fonction supprimerlivre qui prendra pour parametre self
                
        
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso") # connexion a la base de donnes 
                cur=con.cursor()
                cur.execute("delete from emprunterdeslivres where nomAdherent = %s", self.var_nomdelhadherent.get()) #supprimer la ligne 
                cur.execute(" update ajouterdeslivres set Etat ='Disponible' where TitreLivre=%s",self.var_livre.get()),
                con.commit()
                messagebox.showinfo("Succes","Le livre à bien été rendu, Merci", parent=self.PageGestiondesprets)  
                self.actualiser ()
                
                con.close()

    def information(self,ev):  # on recupere les informations pour ensuite les modifier ou supprimer
        cursor_row = self.tableau.focus()
        contents = self.tableau.item(cursor_row)
        row = contents["values"]
        
        self.var_nomdelhadherent.set(row[1]),
        
        self.var_livre.set(row[2]),
        self.var_dateemprunt.set(row[3])
        self.var_dateretour.set(row[4]),
        #self.var_qte.set(row[4]),
        #self.var_status.set(row[5]),

    def PourSeDeConnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageGestiondesprets)
        if lemessagebox == YES:
         self.PageGestiondesprets.destroy()
         call(["python", "Connexion.py"])
         
    def VersGestionLivres(self):
        self.PageGestiondesprets.destroy()
        call(["python", "Gestionlivres.py"]) 
        
                             #pour detruire une fenetre 
    
    def VersAdherents(self):
        self.PageGestiondesprets.destroy()
        call(["python", "Adherents.py"])
       

   

###################emprunt
    
    def list_nomdelhadherent_four(self):  #recuperer les nom et livres dispo dans la base de donnes 
            self.nomdelhadherent_list.append("Vide")
            self.four_list.append("Vide")
            con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
            cur=con.cursor()
            try:
                cur.execute("select nomAdherent from ajouterdesadherents")
                nomdelhadherent=cur.fetchall()
                if len(nomdelhadherent)>0:
                    del self.nomdelhadherent_list[:]
                    self.nomdelhadherent_list.append("Select")
                    for i in nomdelhadherent:
                        self.nomdelhadherent_list.append(i[0])

                cur.execute("select TitreLivre from ajouterdeslivres")
                four=cur.fetchall()
                if len(four)>0:
                    del self.four_list[:]
                    self.four_list.append("Select")
                    for i in four:
                        self.four_list.append(i[0])
                
                    

            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def actualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso") #
        cur=con.cursor()
        cur.execute("select * from emprunterdeslivres ") #ligne sql pour récuperer la table ajoutlivres
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableau.delete(*self.tableau.get_children())
            for row in rows:
                self.tableau.insert("", END, values=row)
        con.commit()
        con.close()



    def PageEmprunt(self):          
        self.PageEmprunt= Toplevel() # top level fenetre fille a la fenetre mere 
        self.PageEmprunt.title("Emprunter un livre") # titre de la frame
        self.PageEmprunt.config(bg="#ff6600")  # background de la frame 
        self.PageEmprunt.geometry("1056x560+400+200") # la taille de la frame
        self.PageEmprunt.focus_force()  
        self.PageEmprunt.grab_set() # si on lance une fenetre on poura pas cliquer ailleurs 
        self.PageEmprunt.resizable(width=False, height=False)
        self.PageEmprunt.iconbitmap()

        #self.root.withdraw()
        

        nom = Label(self.PageEmprunt, text=" Nom ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        nom.place(x=10, y=50)

        txt_categori = ttk.Combobox(self.PageEmprunt,values=self.nomdelhadherent_list,   textvariable=self.var_nomdelhadherent,font=("goudy old style",20), state="readonly", justify=CENTER)
        txt_categori.place(x=200, y=50, width=140)
        txt_categori.current(0)

        livre = Label(self.PageEmprunt, text="Livre ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        livre.place(x=10, y=100)

        txt_fournisseur = ttk.Combobox(self.PageEmprunt,values= self.four_list, textvariable=self.var_livre,font=("goudy old style",20), state="readonly", justify=CENTER)
        txt_fournisseur.place(x=200, y=100, width=140)
        txt_fournisseur.current(0)

        #quantite = Label(self.root1, text="Quantité ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        #quantite.place(x=10, y=150)

        self.date_emprunte = Label(self.PageEmprunt, text="Date Emprunter ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        self.date_emprunte.place(x=10, y=200)

        date_retour = Label(self.PageEmprunt, text="Date Retour ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        date_retour.place(x=10, y=250)
        ############################################# 

        # LES ENTRY
        #txt_quantite = Entry(self.root1, textvariable=self.var_quantite,font=("goudy old style",20),bg="lightyellow")
        #txt_quantite.place(x=200, y=150, width=140)

        self.txt_date_emprunte=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray",textvariable=self.var_dateemprunt, date_pattern="dd/mm/yy")
        self.txt_date_emprunte.place(x=200, y=200, width=140)

        self.txt_date_retour=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray", textvariable=self.var_dateretour,date_pattern="dd/mm/yy")
        self.txt_date_retour.place(x=200, y=250, width=140)

        BoutonAjouter = Button(self.PageEmprunt, command=self.ClickBoutonEmprunter, text="Ajouter",font=("times new roman", 20),cursor="hand2", bg="green").place(x=10, y=300, height=60, width=150)
        #modif_btn = Button(self.PageEmprunt,text="Modifier", font=("times new roman", 20),cursor="hand2", bg="yellow").place(x=170, y=300, height=60, width=150)
        #supp_btn = Button(self.PageEmprunt,text="Supprimer",font=("times new roman", 20),cursor="hand2", bg="red").place(x=10, y=400, height=60, width=150)
        #reini_btn = Button(self.PageEmprunt,text="Réinitialiser",command=self.reni, font=("times new roman", 20),cursor="hand2", bg="gray").place(x=170, y=400, height=60, width=150)
        
        #command=lambda c'est pour passer deux commandes en meme temps

      
        
   
    

    

        #########Fin Fonction Root1
    
    def ClickBoutonEmprunter(self):
        try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")

                cur=con.cursor()
                cur.execute("select * from emprunterdeslivres where nomAdherent=%s",self.var_nomdelhadherent.get())
                row= cur.fetchone()

                if row!= None:

                   messagebox.showerror("Erreur", "Cet adhérent à déja emprunter un livre", parent=self.PageEmprunt)
                
                  
                elif cur.execute("select * from emprunterdeslivres where titreLivre=%s",self.var_livre.get()):

                  messagebox.showerror("Erreur", "livre deja emprunter", parent=self.PageEmprunt)
                
                else:
                
                 cur.execute("insert into emprunterdeslivres (nomAdherent,titreLivre,dateEmprunt,dateRetour) values (%s,%s,%s,%s)",
                   
                   (
                       
                       self.var_nomdelhadherent.get(),
                       self.var_livre.get(),
                       #self.var_quantite.get(),
                       self.var_dateemprunt.get(),
                       self.var_dateretour.get(),
                       
                    ))

                 cur.execute(" update ajouterdeslivres set Etat ='Emprunter' where TitreLivre=%s",self.var_livre.get()),

                 messagebox.showinfo("Succes", "Votre livre à bien été emprunter", parent= self.PageEmprunt)
                   
                 con.commit()
                 con.close
        except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexionnnn{str(es)}",parent=self.PageEmprunt)

    ############################# def pour si un livre a deja ete emprunter on peut pas lemprunter plusieurs fois

   ######################################## test


    def reni(self):
        try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso")
                cur=con.cursor()
                messagebox.showinfo("Succes","Votre livre à été gérée", parent= self.PageEmprunt)
                   
                con.commit()
                con.close
        except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexionnnn{str(es)}",parent=self.PageEmprunt) 

root =Tk()
obj = gestionprets(root)
root.mainloop() #executer tkinter