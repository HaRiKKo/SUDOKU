from tkinter import *
from tkinter import messagebox
from random import *
from time import*
from datetime import*
""" Le but du jeu de Sudoku est de complété une grille de 9x9 cases, divisée en 9 plus petit carré de 3x3, avec des nuléraux allant de 1 à 9, chaques lignes, chaques colonnes et chaques carrés doient comportés au UNE fois un des 9 numéraux.
Pour que le jeu fonctionne bien il faut,après avois choisie sa difficulté, cliquée sur l'une des cases puis le nombre sur le clavier numérique.
                            ___Bon jeu à vous!___ """

#CREATION DE PLUSIEUR LISTE;
#Une première liste vide:
LISTE=[[0 for i in range(9)] for j in range(9)]

#3 listes qui contiennent les grilles de difficultée "facile", "moyen, "difficile";
FACILE=[[0, 1, 9, 0, 3, 0, 2, 6, 0], [2, 0, 0, 6, 1, 7, 0, 0, 9], [6, 0, 0, 8, 0, 2, 0, 0, 3],
        [0, 4, 8, 3, 7, 6, 1, 2, 0], [7, 6, 0, 1, 2, 4, 0, 9, 8], [0, 2, 3, 5, 8, 9, 7, 4, 0],
        [4, 0, 0, 9, 0, 3, 0, 0, 2], [3, 0, 0, 7, 5, 1, 0, 0, 4], [0, 7, 6, 0, 4, 0, 9, 3, 0]]

MOYEN=[[0, 9, 0, 2, 0, 0, 0, 6, 0], [0, 2, 0, 0, 0, 0, 8, 0, 0], [1, 0, 7, 8, 0, 0, 5, 9, 0],
       [5, 0, 6, 0, 0, 0, 1, 2, 0], [7, 1, 0, 6, 5, 0, 0, 3, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0],
       [0, 5, 0, 1, 0, 4, 0, 0, 8], [2, 8, 9, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 8, 0, 0, 0, 0]]

DIFFICILE=[[0, 7, 0, 0, 1, 0, 0, 9, 0], [9, 0, 0, 8, 0, 0, 0, 0, 7], [0, 0, 3, 0, 0, 0, 0, 0, 6],
           [0, 4, 0, 0, 0, 1, 5, 0, 0], [0, 3, 0, 0, 0, 0, 0, 1, 0], [0, 0, 2, 7, 0, 0, 0, 6, 0],
           [5, 0, 0, 0, 0, 0, 6, 0, 0], [6, 0, 0, 0, 0, 5, 0, 0, 2], [0, 8, 0, 0, 2, 0, 0, 7, 0]]
    

#Liste utiliser plus tard dans le programme qui permet de récupérer les positions et le temps;
pos=[0,0]
T=[0,0]
        
#CREATION DE LA FENETRE PRINCIPAL;
fen = Tk()
fen.title("SUDOKU")

#Création du canvas grille, où seras cituer la futur grille de jeu;    
grille = Canvas(fen, height= 522, width=522,bg= 'white')
grille.grid(column=1,row=2, padx=10, pady=10)
#Création du canvas num, où seras cituer le futur clavier numérique;
num = Canvas(fen,height= 300, width=300, bg= 'white')
num.grid(column=2,row=2, padx=10, pady=10)


def draw_columns(X):
#Création des lignes verticales a l'aide d'une boucle "for";
    
    for i in range(11):
        grille.create_line(3, 1, 3, 522, fill='black',width=5)
        grille.create_line(X, 0, X, 522, fill='black')
        X+=58
    #Met une plus grosse épaiseur a certaines lignes.        
        if X==0 or X==174 or X==348 or X==522:
            grille.create_line(X, 0, X, 522, fill='black',width=5)
    return
    
def draw_lines(Y):
#creation des lignes horizontal a l'aide d'une boucle "for";   
        
    for i in range(11):
        grille.create_line(1, 3, 522, 3, fill='black',width=5)
        grille.create_line(0, Y, 522, Y, fill='black')
        Y+=58
    #Met une plus grosse épaiseur a certaines lignes.
        if Y==0 or Y==174 or Y==348 or Y==522:
            grille.create_line(0, Y, 522, Y, fill='black',width=5)
    return


def make_grille(A):    
#Permet de poser la grille selon le niveau de difficulté choisi;
    global LISTE
    LISTE=A
    grille.delete(ALL)
    draw_columns(0)
    draw_lines(0)

    for i in range (9):
        for j in range (9):
        
            if A [i][j]>0:
                grille.create_text((i*58)+30,(j*58)+32,text=str(A[i][j]),font=("helvetica",20), fill="black")
    chrono_start()
 
def Bfac():
    make_grille(FACILE)

def Bmoy():
    make_grille(MOYEN)
    
def Bdif():
    make_grille(DIFFICILE)


def draw_choix():
#Mise en place des boutons, "facile, "moyen", "difficile";

    choix=Label(fen,text='CHOISISSEZ VOTRE DIFFICULTE !',font=(10))
    choix.grid(column=1,row=0,pady=15)

    fac = Button(fen, text='Facile', height=2, width=10,command=Bfac)
    fac.grid(column=0, row=1, padx=5, pady=5)
    
    moy = Button(fen, text='Moyen',  height=2, width=10,command=Bmoy)
    moy.grid(column=1, row=1, padx=5, pady=5)
    
    dif = Button(fen, text='Difficile',  height=2, width=10,command=Bdif)
    dif.grid(column=2, row=1, padx=5, pady=5)

def chrono_start():
#Recupère le temp(t1) quand on choisie la difficultée;
    t1=datetime.now()
    T[0]=t1
  
def chrono_end():
#Récupère le temps(t2) une fois le sudoku complété et validé;
    t2=datetime.now()
    T[1]=t2

def chrono():
#soustraction des temps de debut et de fin = chronomètre;
    t1 ,t2=T
    t3=t2-t1
    
    win=Tk()
    c=Label(win,text="Vous avez gagnez en: "+str(t3),font=(5),fg="#03C61D")
    c.pack()
    
def click_position(event):
#Récupération des possition (x;y) du clic;
    pos[0]=event.x
    pos[1]=event.y

def event(num):
#Fonction de base qui permet de poser les numéraux dans la grille de jeu;
    X, Y=pos
    i = int((X - 1) / 58)
    j = int((Y - 1) / 58)
    LISTE[i][j]= num
    grille.create_rectangle((i*58)+6,(j*58)+6,(i*58)+55,(j*58)+55, fill="white",outline="white")
    grille.create_text((i*58)+30,(j*58)+32,text=str(LISTE[i][j]),font=("helvetica",20), fill="blue")

    #Permet de pausé les numéraux 1,2,3,4...,9;
def onClick1():
    event(1)
        
def onClick2():
    event(2)

def onClick3():
    event(3)

def onClick4():
    event(4)

def onClick5():
    event(5)

def onClick6():
    event(6)

def onClick7():
    event(7)

def onClick8():
    event(8)

def onClick9():
    event(9)

def effacer():
#Fonction qui permmet d'éffacer: crée un carré blanc et remet un 0 dans la LISTE;
    X, Y=pos
    i = int((X - 1) / 58)
    j = int((Y - 1) / 58)
    LISTE[i][j]=0
    grille.create_rectangle((i*58)+6,(j*58)+6,(i*58)+55,(j*58)+55, fill="white",outline="white")
        
    
def Bouton():
#Contient les autres boutons: quitter, valider... et le clavier numérique.
    quitter=Button(fen,text="Quitter",command=fen.destroy)
    quitter.grid(column=1,row=4)
    
    Effacer=Button(fen,text="Effacer",command=effacer)
    Effacer.grid(column=0,row=4)
    
    BcheckT=Button(fen,text="Verification globale",command=Bcheck)
    BcheckT.grid(column=2,row=4)

    #création de mylist et d'une boucle qui récupert les ellements de mylist pour crée le clavier numérique;    
mylist = [
        ["1", onClick1, 0, 0],
        ["2", onClick2, 1, 0],
        ["3", onClick3, 2, 0],
        ["4", onClick4, 0, 1],
        ["5", onClick5, 1, 1],
        ["6", onClick6, 2, 1],
        ["7", onClick7, 0, 2],
        ["8", onClick8, 1, 2],
        ["9", onClick9, 2, 2]
        ]

buttons = []
for elem in mylist:
        button = Button(num, text = elem[0],height= 3, width=6,command = elem[1] )
        button.grid(column=elem[2], row=elem[3])
buttons.append(0)


def checkL():
#Fonction qui vérifie les lignes : si la somme des nombre est égal a 45 et leur carré a 285;
    global LISTE
  
    for j in range(9):
        s=0
        S=0
        for i in range(9):

            s+=LISTE [i][j]
            S+=(LISTE [i][j])*(LISTE[i][j])
           
        if LISTE[i][j]==0:
            T=False
            break
      
        if s==45 and S==285:
            T=True
    
        else:
            T=False
            break
    print(T)
    return T

def checkC():
#Fonction qui vérifie les colonnes : si la somme des nombre est égal a 45 et leur carré a 285;
    global LISTE
 
    for i in range(9):
        s=0
        S=0
        for j in range (9):
        
            s+=LISTE [i][j]
            S+=(LISTE [i][j])*(LISTE[i][j])
            
            
        if LISTE[i][j]==0:
            T= False
            break
    
        if s==45 and S==285:
            T= True

        else:
            T= False
            break
    print (T)
    return T
    
def Bcheck():
#Verifie si checkC() et checkL() sont True(vrai); 
    global LISTE
    
    if checkL() and checkC() :
        chrono_end()
        chrono()
        
    else :
        loose=Tk()
        l=Label(loose,text="Essayez encore vous allez y arriver !",font=(5),fg="red")
        l.pack()

#APPELLE DES FONCTIONS;

draw_columns(0)
draw_lines(0)
draw_choix()
Bouton()

grille.bind('<Button-1>',click_position)
fen.mainloop()
