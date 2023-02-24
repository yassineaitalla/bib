from distutils.cmd import Command # c'est des bibliotheque qu'on a importer pour pouvoir bosser avec 
#pour pouvoir importer ces bibiotheques on utilise pip install dns l'invite de commande
from logging import root 
from tkinter import *    #pour importer la bibliotheque tkinter
  
from tkinter import ttk, messagebox #pour les messages derreur
import pymysql #c'est une bibliothèque python qui permet d'interagir avec une base de données
from subprocess import call #bibliotheque pour changer de page


class PagedeConnexion:  #classe formulaire 
    def __init__(self,root): #self représente l'instance de la classe. En utilisant le mot clé " self " nous pouvons accéder aux attributs et méthodes de la classe en python. 
        self.PagedeConnexion = root  
        self.PagedeConnexion.title("Connexion") #titre en haut de la page
        self.PagedeConnexion.geometry("1040x560+400+200")  #taille de page
        
        self.PagedeConnexion.resizable(width=False, height=False) #pour que le bouton agrandir ne puisse pas marcher
        self.PagedeConnexion.iconbitmap() #a modifier importer l'icone de l'application
        
         
        #champs du formulaire
        PaneauOrangeDuHaut = Frame(self.PagedeConnexion, bg="#ff7f00") #Frame est un conteneur qui permets de gérer des widgets paneau orange du haut 
        PaneauOrangeDuHaut.place(x=0, y=-30, width=1100, height=140) #largeur longeur taille du panneau

        self.imageicon5 = PhotoImage() # logo a gauche des livres 
        self.btn3 = Label(root, text="",compound=LEFT,image=self.imageicon5, width=500, height=320, font="arial 12 bold") 
        #Compound si on souhaite que l’étiquette affiche à la fois un texte et un graphique (soit un bitmap, soit une image) 
        self.btn3.place(x=50,y=150) #place du logo

        PaneauOrangeDuBas = Frame(self.PagedeConnexion, bg="#ff7f00") #Frame est Un cadre est simplement un conteneur pour d’autre widgets.
        PaneauOrangeDuBas.place(x=0, y=460, width=1100, height=140) 

        PanneauGrisDuMilieu = Frame(self.PagedeConnexion, bg="#ff7f00") #Frame est Un cadre est simplement un conteneur pour d’autre widgets.
        PanneauGrisDuMilieu.place(x=670, y=180, width=350, height=240) 


        #Labels 
        titlepourbibyaso = Label(PaneauOrangeDuHaut, text=" BibYaso Pour Les Lecteurs !", font =("algarian", 20,"bold"), bg="grey", fg="black")
        titlepourbibyaso.place(x=350, y=40) 

        titlepouryassineso = Label(PaneauOrangeDuHaut, text="By Yassine Sofiane ", font =("Arial", 15,), bg="#ff7f00", fg="black")
        titlepouryassineso.place(x=460, y=80)
  
        bienvenue =  Label(PanneauGrisDuMilieu, text="S'identifier", font =("Arial", 15,"bold"), bg="grey", fg="black")
        bienvenue.place(x=148, y=16)

        Email = Label(PanneauGrisDuMilieu, text="E-mail:", font =("Arial", 12,"bold"), bg="grey", fg="black")
        Email.place(x=10, y=80)
        
        motdepasse = Label(PanneauGrisDuMilieu, text="Mot de passe:", font =("Arial", 12,"bold"), bg="grey", fg="black")
        motdepasse.place(x=10, y=120)
        
        
        #Entry champs de saisie
        self.txt_email= Entry(PanneauGrisDuMilieu, font= (5), bg="lightgray") 
        self.txt_email.place(x=150, y=80,width=150)


        self.txt_motdepasse= Entry(PanneauGrisDuMilieu, show="*",font= (5), bg="lightgray")
        self.txt_motdepasse.place(x=150, y=120,width=150)
        # show="*" pour cacher le mot de passe

        

        #Bouton Cree un compte
        Creeuncompte = Button(PanneauGrisDuMilieu, text="Crée un compte",command=self.PageCreationDeCompte, cursor="hand2", font=("times new roman",10,"bold"), bd=0,bg="grey",fg="black")
        Creeuncompte.place(x=150, y=200)
        #command=self.creeuncompte est utilisé pour récuperer la fonction creeuncompte qu'on a declarer en bas 

        #Bouton mot de passe 
        Boutonmotdepasseoublie = Button(PanneauGrisDuMilieu, text="Mot de passe oublié ?", command=self.CliquerMotdepasseOublie, cursor="hand2", font=("times new roman",11), bd=0,bg="grey",fg="white")
        Boutonmotdepasseoublie.place(x=10, y=170)
        #command=self.motdepasseoublie est utilisé pour recuperer la fonction mot de passe oublie qu'on a declarer en bas

        
        #bouton connexion
        BoutonConnexion = Button(PanneauGrisDuMilieu, text="Connexion",command=self.CliquerBoutonConnexion, cursor="hand2", font=("times new roman",12), bd=0,bg="#40E0D0",fg="black")
        BoutonConnexion.place(x=260, y=170)
        #command=self.connexion est utilisé pour recuperer la fonction pour recuperer le self.connexion qu'on a declarer en bas
    """
    def effacerchampssaisieconnexion(self): #on declare une fonction pour effacer champs de saisie apres une connexion
        self.txt_email.delete(0, END) #efface le champs de saisie email
        self.txt_motdepasse.delete(0, END) #efface le champs de saisie mot de passe
    """
    
    def CliquerBoutonConnexion(self): #fonction Connexion qui prendra pour parametre self
        if self.txt_email.get()=="" or self.txt_motdepasse.get()=="":  #si le champs de saisie mail est égal à null et si le champ de saisie mot de passe est égal à null  
           messagebox.showerror("Erreur", "Veuillez Saisir Email Mot depasse", parent=self.PagedeConnexion) # si les champs ne sont pas rempli alors affiche une message pour dire "Veuillez Saisir Email Mot depasse"
        else: #sinon
           try:
                con = pymysql.connect(host="localhost", user="root",password="", database="bibyaso")
                cur = con.cursor()
                cur.execute("select * from comptes where email=%s and password=%s", (self.txt_email.get(), self.txt_motdepasse.get()))  #.get recuperer les informations saisie
                row = cur.fetchone()
                if row == None:
                   messagebox.showerror("Erreur", "E-mail ou le password est incorrect ", parent=self.PagedeConnexion)
                   #self.effacerchampssaisieconnexion()
                else: #alors 
                   messagebox.showinfo("Succes", "Bienvenue") #affiche un message box Bienvenue
                   #self.effacerchampssaisieconnexion() #Appel la fonction effacerchampssaisieconnexion pour supprimer les champs de saisie 
                   self.OuvrirLaPageGestionLivres()
                   con.close()
                
           except Exception as ex:
               messagebox.showerror("Erreur", f"erreur de connexion{str(ex)}", parent=self.PagedeConnexion)
    
    
    def CliquerMotdepasseOublie(self): #fonction mot de passe oublié
        if self.txt_email.get()=="": #si le champs email est null alors
            messagebox.showerror("erreur", "Veuillez donner un mail valide", parent=self.PagedeConnexion)#on affiche un message d'erreur pour donner un mail valide
        else:
            try:
                con = pymysql.connect(host="localhost", user="root",password="", database="bibyaso") #connexion à la base de donnes 
                cur = con.cursor()
                cur.execute("select * from comptes where email=%s ", self.txt_email.get()) #.get recuperer les informations saisie
                row = cur.fetchone()
                if row == None: #si les champs ne corresponde pas a ceux dans la base de données alors 
                    messagebox.showerror("Erreur", "Invalide l'email et le password", parent=self.PagedeConnexion) # Alors affiche un messagebox pour dire que le message et le password sont invalide   
                else:
                    con.close() #
                    self.PageDeMotdepasseOublie= Toplevel() #Fenetre Mere
                    self.PageDeMotdepasseOublie.title("Mot de passe oublie") #titre de mot de passe oublie
                    self.PageDeMotdepasseOublie.config(bg="#ff6600") #couleur du background 
                    self.PageDeMotdepasseOublie.geometry("350x350+800+500") #taille de l'application
                    self.PageDeMotdepasseOublie.focus_force()# 
                    self.PageDeMotdepasseOublie.grab_set()#  
                    
                    #titre
                    labelmotdepasseoublie = Label(self.PageDeMotdepasseOublie, text="Mot de passe oublié ?", font =("Arial", 12,"bold"), fg="black")
                    labelmotdepasseoublie.place(x=93, y=20) 
                    

                    selectionunequestion = Label(self.PageDeMotdepasseOublie, text="Séléctionnez une question", font =("Arial", 10,"bold"), fg="black")
                    selectionunequestion.place(x=10, y =70)
                    
                    #liste questions
                    self.ecri_question = ttk.Combobox(self.PageDeMotdepasseOublie, font=("times new roman", 15), state="readonly")
                    self.ecri_question["values"]=("Select", "ton prenom", "Lieu de naissance", "Meilleur ami", "Film préféré") 
                    self.ecri_question.place(x=10, y=100, width=110)
                    self.ecri_question.current(0)# combox pour récuperer les champs prenom lieu de naissance   
                    
                    # champs repondre a une question
                    repondreunequestion = Label(self.PageDeMotdepasseOublie, text="Répondre", font =("Arial", 10,"bold"), fg="black")
                    repondreunequestion.place(x=10, y =150)


                    self.repondreunequestion_entry = Entry(self.PageDeMotdepasseOublie, font= (5), bg="white")
                    self.repondreunequestion_entry.place(x=10, y =190)
                    #label pour répondre     
                    
                    
                    
                    
                    # Label mot de passe
                    nouveaumotdepasse = Label(self.PageDeMotdepasseOublie, text="Nouveau Mot de passe", font =("Arial", 10,"bold"), fg="black")
                    nouveaumotdepasse.place(x=10, y =230)

                    # Champs de saisie mot de passe
                    self.nouveaumotdepasse_entry = Entry(self.PageDeMotdepasseOublie,show="*", font=(5), bg="white")
                    self.nouveaumotdepasse_entry.place(x=10, y =270)
                    #show="*" permet de rendre le mot de passe invisible 
                    
                    
                    #bouton pour modifier mot de passe
                    btnmotdepasseoublie = Button(self.PageDeMotdepasseOublie, text="Modifier",command=self.MotdePasseOublie,cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
                    btnmotdepasseoublie.place(x=150, y=320)

                    #self.password_oublie pour récuperer la variable qu'on a creer en haut 
                    
            except Exception as ex:
                 messagebox.showerror("Erreur", f"erreur de connexion{str(ex)}", parent=self.CliquerBoutonCreeuncompte)


    def effacerchampssaisie(self): #  
        self.ecri_question.current(0)
        self.repondreunequestion_entry.delete(0, END)
        self.nouveaumotdepasse_entry.delete(0, END)
    
    
    def MotdePasseOublie(self):
        if self.ecri_question.get()=="" or self.repondreunequestion_entry.get()=="" or self.nouveaumotdepasse_entry.get()=="": #si les champs ne sont pas rempli
            messagebox.showerror("Erreur","Remplir tous les champs",parent=self.PageDeMotdepasseOublie) #alors affiche un message box pour dire remplir tout les champs
        else:
            try:
                con = pymysql.connect(host="localhost", user="root",password="", database="bibyaso")
                cur = con.cursor()
                cur.execute("select * from comptes where email=%s and question=%s and reponse=%s",( self.txt_email.get(), self.ecri_question.get(), self.repondreunequestion_entry.get()))
                row= cur.fetchone()

                if row == None: #si cest faux alors affiche message box  
                   messagebox.showerror("Erreur", "Vous n'avez pas bien répondu a la question séléctionnez",parent= self.PageDeMotdepasseOublie)
                
                else:  # si cest correct alors
                    cur.execute("update comptes set password=%s where email=%s",(self.nouveaumotdepasse_entry.get(),self.txt_email.get()))
                    con.commit()
                    con.close() # pour fermer la base de donnes
                    
                    messagebox.showinfo("Success","Vous avez modifier votre mot de passe", parent=self.PageDeMotdepasseOublie)
                    self.effacerchampssaisie() #pour affacer les champs de saisie
            
            except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}", parent=self.PageDeMotdepasseOublie)#    

            #On utilise Except pour eviter les erreurs
    
    def PageCreationDeCompte(self): #Page pour créer un compte utilisateur
                
                    self.PageCreationDeCompte= Toplevel() #Page mere,  Toplevel()-----> fenetre fille 
                    self.PageCreationDeCompte.title("Crée un compte") #Titre de la page
                    self.PageCreationDeCompte.config(bg="#ff6600") #Couleur de la page 
                    self.PageCreationDeCompte.geometry("400x500+750+200") #taille de la page 
                    
                    self.PageCreationDeCompte.focus_force()  
                    self.PageCreationDeCompte.grab_set() #Grab_set our eviter de cliquer sur d'autre page tout en ettant sur la principal
                    
                    
                    #Label ----> etiquette
                    titreDeLaPageCreeunCompte = Label(self.PageCreationDeCompte, text="Crée un compte", font =("Arial", 12,"bold"), fg="black")
                    titreDeLaPageCreeunCompte.place(x=140, y=20)

                    labelNom = Label(self.PageCreationDeCompte, text=" Nom : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    labelNom.place(x=10, y=80)
                    
                    labelPrenom = Label(self.PageCreationDeCompte, text=" Prénom : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    labelPrenom.place(x=10, y=120)

                    self.emailcreeuncompte = Label(self.PageCreationDeCompte, text=" Email : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    self.emailcreeuncompte.place(x=10, y=160)

                    telcreeuncompte = Label(self.PageCreationDeCompte, text=" Téléphone : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    telcreeuncompte.place(x=10, y=200)
                    
                    selecunequestioncreeuncompte = Label(self.PageCreationDeCompte, text=" Séléctionnez une question : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    selecunequestioncreeuncompte.place(x=10, y=240)

                    repunequestioncreeuncompte = Label(self.PageCreationDeCompte, text=" Répondre : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    repunequestioncreeuncompte.place(x=10, y=280)
                    
                    motdepassecreeuncompte = Label(self.PageCreationDeCompte, text=" Mot de passe : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    motdepassecreeuncompte.place(x=10, y=320)

                    confmotdepassecreeuncompte = Label(self.PageCreationDeCompte, text=" Confirmée mot de passe : ", font =("algarian", 11,), bg="#ff6600", fg="black")
                    confmotdepassecreeuncompte.place(x=10, y=360)

                    
                    
                    
                    #Champs de saisie
                    self.nom_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.nom_creeuncompte.place(x=190, y=80,width=150)

                    self.prenom_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.prenom_creeuncompte.place(x=190, y=120,width=150)

                    self.email_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.email_creeuncompte.place(x=190, y=160,width=150)
                    
                    self.telephone_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.telephone_creeuncompte.place(x=190, y=200,width=150)

                    self.ecri_questioncreeuncompte = ttk.Combobox(self.PageCreationDeCompte, font=("times new roman", 15), state="readonly")
                    self.ecri_questioncreeuncompte["values"]=("ton prenom", "Lieu de naissance", "Meilleur ami", "Film préféré") 
                    self.ecri_questioncreeuncompte.place(x=190, y=240,width=150)
                    self.ecri_questioncreeuncompte.current(0)

                    self.rep_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.rep_creeuncompte.place(x=190, y=280,width=150)

                    self.motdepasse_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.motdepasse_creeuncompte.place(x=190, y=320,width=150)

                    self.confirmemotdepasse_creeuncompte= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.confirmemotdepasse_creeuncompte.place(x=190, y=360,width=150)

                    self.BoutonBoutonPourAccepterLesConditions = IntVar() 
                    #On déclare la variable BoutonBoutonPourAccepterLesConditions pour ensuite la récuperer  
                    BoutonPourAccepterLesConditions = Checkbutton(self.PageCreationDeCompte, variable=self.BoutonBoutonPourAccepterLesConditions, onvalue=1, offvalue=0 , text="J'accepte les conditions et les termes", font=("times new roman",12), bg="white").place(x=10, y=400)
                    #On Recupere la varibale BoutonBoutonPourAccepterLesConditions
                    
                    BoutonCreeuncompte = Button(self.PageCreationDeCompte, text="Crée un compte",command=self.CliquerBoutonCreeuncompte,cursor="hand2", font=("times new roman",12), bd=0,bg="white",fg="black")
                    BoutonCreeuncompte.place(x=270, y=440)
                    #Bouton creation de compte qui prend comme parametre command de la fonction self.CliquerBoutonCreeuncompte qu'on à declarer juste en bas 
    

    def CliquerBoutonCreeuncompte(self): #Fonction en cas de 
        if self.nom_creeuncompte.get()=="" or self.prenom_creeuncompte.get()=="" or self.email_creeuncompte.get()=="" or self.telephone_creeuncompte.get()=="" or self.ecri_questioncreeuncompte.get()=="" or self.rep_creeuncompte.get()=="" or  self.telephone_creeuncompte.get()=="" or self.motdepasse_creeuncompte.get()=="" or self.confirmemotdepasse_creeuncompte.get()=="":
         messagebox.showerror("Erreur", "Remplir tous les champs", parent=self.PageCreationDeCompte) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
        elif self.motdepasse_creeuncompte.get()!= self.confirmemotdepasse_creeuncompte.get():#si les mots de passe ne sont pas pareils
         messagebox.showerror("Erreur", "les mots de passe ne sont pas conforme", parent=self.PageCreationDeCompte) #alors affiche un message box en disant que ses mots de passe ne sont pas pareils
        elif self.accepteconditions.get()==0: #si le champ conditions n'est pas rempli 
         messagebox.showerror("Erreur","Accepter les conditions", parent=self.PageCreationDeCompte)#alors affiche un message box pour accepter les conditions

        else:
            try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bibyaso") #pour faire la connexion à la base de données
                cur=con.cursor()
                cur.execute("select * from comptes where email=%s",self.email_creeuncompte.get()) # récuperer la table mail dans la base de données
                row= cur.fetchone()  #La méthode fetchone() récupère ensuite la première ligne de ce résultat.

                if row != None: #si se qu'on a rentrer se trouve  dans la base de données alors 
                    messagebox.showerror("Erreur", "Ce mail existe déja", parent=self.PageCreationDeCompte) #alors affiche un message box pour dire que ce mail existe déja dans la base de donnés
                else:
                   cur.execute("insert into comptes (prenom, nom, email, telephone, question,reponse,password) values (%s,%s,%s,%s,%s,%s,%s)",#on insere dans la base de donnes les champs prenom, email,telephone, question,reponse,password
                   (
                       self.nom_creeuncompte.get(),
                       self.prenom_creeuncompte.get(),
                       self.email_creeuncompte.get(),
                       self.telephone_creeuncompte.get(),
                       self.ecri_questioncreeuncompte.get(),
                       self.rep_creeuncompte.get(),
                       self.motdepasse_creeuncompte.get(),
                    ))

                   messagebox.showinfo("Succes","Votre compte à été crée", parent=self.PageCreationDeCompte) #On affiche un message box pour dire que le compte à bien été crée
                   self.EffacerChampsdeSaisiedelaPageCreationdecompte()#Fonction pour effacer les champs de saisie apres avoir creer un compte  
                
                con.commit()
                con.close

            except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageCreationDeCompte) 
    
    
    def EffacerChampsdeSaisiedelaPageCreationdecompte(self): #Fonction pour effacer les champs de saisie de la page creation de compte
        self.nom_creeuncompte.delete(0, END) #efface le champs de saisie creeuncompte
        self.prenom_creeuncompte.delete(0, END) #efface le champs de saisie prenom
        self.email_creeuncompte.delete(0, END) #efface le champs de saisie email
        self.telephone_creeuncompte.delete(0, END) #efface le champs de saisie telephone
        self.ecri_questioncreeuncompte.delete(0, END) #efface le champs de saisie question
        self.rep_creeuncompte.delete(0, END) #efface le champs de saisie repondre a une question
        self.motdepasse_creeuncompte.delete(0, END) #efface le champs de saisie mot de passe
        self.confirmemotdepasse_creeuncompte.delete(0, END) #efface le champs de saisie confirmee mot de passe
        

        
    def OuvrirLaPageGestionLivres(self): #On declare une fonction pour ouvrir la page gestion livres
        self.PagedeConnexion.destroy() #Pour fermer la page dans la quelle on se trouve 
        call(["python", "gestionlivres.py"])# et avec le call on ouvre la page dans la quelle on souhaite aller
        
root =Tk() 
obj = PagedeConnexion(root) 
root.mainloop() #est une méthode sur la fenêtre principale que nous exécutons lorsque nous voulons exécuter notre application 