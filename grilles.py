import numpy as np

def grille_zero(grille):
    grille = np.array([0]*81)
    grille = grille.reshape(9,9)
    return grille

def case_vers_numero(i,j):
    return i*9+j

def numero_vers_case(k):
    return (k//9,k%9)

def liste_vers_grille(liste):
    grille=[[0 for j in range(9)]for i in range(9)]
    for k in range(len(liste)):
        i,j = numero_vers_case(k)
        grille[i][j]=liste[k]
    return grille

#On rentre une grille comme une liste de 81 valeurs
#les deux listes suivantes sont complètes et correctes
liste_pleine_1=[5,3,4, 6,7,8, 9,1,2,
                6,7,2, 1,9,5, 3,4,8,
                1,9,8, 3,4,2, 5,6,7,
                8,5,9, 7,6,1, 4,2,3,
                4,2,6, 8,5,3, 7,9,1,
                7,1,3, 9,2,4, 8,5,6,
                9,6,1, 5,3,7, 2,8,4,
                2,8,7, 4,1,9, 6,3,5,
                3,4,5, 2,8,6, 1,7,9]


liste_pleine_2=[4,1,5, 6,3,8, 9,7,2,
                3,6,2, 4,7,9, 1,8,5,
                7,8,9, 2,1,5, 3,6,4,
                9,2,6, 3,4,1, 7,5,8,
                1,3,8, 7,5,6, 4,2,9,
                5,7,4, 9,8,2, 6,3,1,
                2,5,7, 1,6,4, 8,9,3,
                8,4,3, 5,9,7, 2,1,6,
                6,9,1, 8,2,3, 5,4,7]


liste_fausse=[4,8,3, 9,5,7, 6,1,2,
               7,5,6, 1,2,8, 4,9,3,
               1,9,2, 4,3,6, 5,7,8,
               2,3,1, 5,6,4, 7,8,9,
               5,7,4, 8,1,9, 2,3,6,
               8,6,9, 2,7,3, 1,4,5,
               6,4,7, 3,8,2, 9,5,1,
               9,1,8, 6,4,5, 3,2,3,
               3,2,5, 7,9,1, 8,6,4]


liste_incomplète=[2,0,4, 0,8,0, 0,5,0,
                7,0,0, 0,1,0, 0,0,2,
                8,0,0, 0,0,3, 6,0,0,
                0,0,9, 1,0,0, 2,0,5,
                4,0,5, 2,0,7, 9,0,3,
                6,0,8, 0,0,9, 7,0,0,
                0,0,7, 4,0,0, 0,0,6,
                5,0,0, 0,9,0, 0,0,8,
                0,4,0, 0,7,0, 5,0,9]

#on convertit les listes en grille:

grille_2=liste_vers_grille(liste_pleine_2)

grille_1=liste_vers_grille(liste_pleine_1)

grille_fausse=liste_vers_grille(liste_fausse)
grille_incomplète=liste_vers_grille(liste_incomplète)

def afficher_une_grille(grille):
    for k in range(9):
        for i in range(9):
            if grille[k][i] != 0:
                print(grille[k][i], end=" ")
            else:
                print("-", end=" ") # remplace les zéros par des tirets si les zéros représentent les nombres manquants
        print()

afficher_une_grille(grille_incomplète)

def verification_ligne_grille(grille): 
    dico_verificateur={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
    for k in range(9):
        a={}
        for i in range(9):
            if grille[k][i] in a.keys():
                a[grille[k][i]]+=1
            else :
                a[grille[k][i]]=1
        if a!=dico_verificateur:
            return False
    return True



def verification_colonne_grille(grille):
    dico_verificateur={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
    for k in range(9):
        a={}
        for i in range(9):
            if grille[i][k] in a.keys():
                a[grille[i][k]]+=1
            else :
                a[grille[i][k]]=1
        if a!=dico_verificateur:
            return False
    return True

def verification_carre_grille(grille):
    dico_verificateur = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    for j in range(3):
        for i in range(3):
            a={}
            for k in range(3):
                for h in range(3):
                    if grille[3*i+k][3*j+h] in a.keys():
                        a[grille[3*i+k][3*j+h]]+=1
                    else:
                        a[grille[3*i+k][3*j+h]] = 1
            if a != dico_verificateur:
                    return False
    return True


def grille_is_correct(grille):
    if verification_carre_grille(grille) and verification_colonne_grille(grille) and verification_ligne_grille(grille):
        return True
    else :
        return False

#print(grille_is_correct(grille_1))

# on considère que les chiffres manquants ou enlevés seront représentés par des zéros

def chiffres_lignes(i,grille): # cette fonction renvoie une liste avec tous les chiffres présents sur la ligne i hors zéro
    ligne=[]
    for k in range(9):
        if grille[i][k]!=0:
            ligne=ligne +[grille[i][k]]
    return ligne

def chiffres_colonnes(j,grille):# cette fonction renvoie une liste avec tous les chiffres présents sur la colonne j hors zéro
    colonne=[]
    for k in range(9):
        if grille[k][j]!= 0:
            colonne=colonne +[grille[k][j]]
    return colonne

def chiffres_carré(i,j,grille):# cette fonction renvoie une liste avec tous les chiffres présents sur la colonne j hors zéro
    a = 3*(i//3)
    b = 3*(j//3) # (a,b) représente les coordonnées du coin supérieur gauche du carré
    carré=[]
    for k in range(3):
        for h in range(3):
            if grille[a+k][b+h]!=0:
                carré = carré+ [grille[a+k][b+h]]
    return carré

#print(chiffres_carré(3,4,grille_1))

def possibilites_de_la_case(k,grille): # pour chaque case 0<=k<=80 d'une grille, on renvoie les chiffres possibles
    i,j = numero_vers_case(k)
    if grille[i][j] != 0: # si la case comporte un numéro, on le garde
        return [grille[i][j]]

    #chiffres_présents est une liste qui renvoi tous les chiffres dans la meme ligne, la meme colonne et le même carré que la case k
    chiffres_presents= chiffres_lignes(i,grille)+chiffres_colonnes(j,grille)+chiffres_carré(i,j,grille)

    chiffres_possibles=[i for i in range(1,10) if i not in chiffres_presents]
    return chiffres_possibles  #peut renvoyer une liste vide s'il n'y a pas de possibilités



# les fonctions suivantes ont pour but de déterminer par force brute toutes les possibilités de grille connaissant les chriffres du début


# pour chaque case 0<=k<=80 d'une grille, on renvoie les chiffres possibles en tenant compte
#des choix faits dans les cases précédentes

possibilites=[] #renvoie une liste contenant toutes les possibilités case par case




def derniere_valeur(): #on choisit la dernière valeur obtenue par la fonction possibilites_de_la_case()
    return [possibilites[k][-1] for k in range(len(possibilites))]
#print(derniere_valeur())

def possibilites_case(k,grille):
    i,j = numero_vers_case(k)
    if grille[i][j] != 0: # si la case comporte un numéro, on le garde
        return [grille[i][j]]
    valeur=derniere_valeur() #renvoie une liste des "derniers" chiffres possibles
    grille_essai=liste_vers_grille(valeur) #renvoie une grille contenant une combinaison possible
    for i in range(9):
        for j in range(9):
            if grille[i][j]!=0: # on rajoute dans notre grille essai les valeurs de la grille de départ
                grille_essai[i][j]=grille[i][j]

    #chiffres_présents est une liste qui renvoie tous les chiffres dans la même ligne, la meme colonne et le même carré que la case k
    chiffres_presents= chiffres_lignes(i,grille)+chiffres_colonnes(j,grille)+chiffres_carré(i,j,grille)

    chiffres_possibles=[i for i in range(1,10) if i not in chiffres_presents]
    return chiffres_possibles  #peut renvoyer une liste vide s'il n'y a pas de possibilités




def retour():#si jamais le choix conduit à une impasse
    global possibilites
    r =len(possibilites)-1   # avant dernière case
    while r>=0 and len(possibilites[r])==1:  #si il n'y a qu'une possibilité pour l'avant dernière case
        del possibilites[-1]
        r = r - 1
    if r >= 0:
        k = len(possibilites[r])
        possibilites[r]=possibilites[r][0:k-1]
    return

def combinaisons_correctes(grille):
    global possibilites
    possibilites=[]
    possibilites=[possibilites_de_la_case(0,grille)]
    termine = False
    while not termine:
        r = len(possibilites)
        print(possibilites)
        if r ==0: #plus de possibilités
            termine= True
        if 0<r<81:
            autre_combinaison=possibilites_de_la_case(r,grille)
            if len(autre_combinaison)!=0:
                possibilites=possibilites+[autre_combinaison]
            else:
                retour()
        if r ==81: # on a une solution
            print("solution:",derniere_valeur())
            retour()
            termine=True
    return derniere_valeur()



liste_solution=combinaisons_correctes(grille_incomplète)
grille_solution=liste_vers_grille(liste_solution)
afficher_une_grille(grille_solution)






