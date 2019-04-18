import numpy as np

def grille_zero(grille):
    grille = np.array([0]*81)
    grille = grille.reshape(9,9)
    return grille

#les deux grilles suivantes sont complètes et correctes
grille_pleine_1=np.array([5,3,4,6,7,8,9,1,2,6,7,2,1,9,5,3,4,8,1,9,8,3,4,2,5,6,7,8,5,9,7,6,1,4,2,3,4,2,6,8,5,3,7,9,1,7,1,3,9,2,4,8,5,6,9,6,1,5,3,7,2,8,4,2,8,7,4,1,9,6,3,5,3,4,5,2,8,6,1,7,9])
grille_pleine_1=grille_pleine_1.reshape(9,9)
#print(grille_pleine_1)

grille_pleine_2=np.array([4,1,5,6,3,8,9,7,2,3,6,2,4,7,9,1,8,5,7,8,9,2,1,5,3,6,4,9,2,6,3,4,1,7,5,8,1,3,8,7,5,6,4,2,9,5,7,4,9,8,2,6,3,1,2,5,7,1,6,4,8,9,3,8,4,3,5,9,7,2,1,6,6,9,1,8,2,3,5,4,7])
grille_pleine_2=grille_pleine_2.reshape(9,9)
#print(grille_pleine_2)

#print(grille_pleine_2[1][3])


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

print(verification_colonne_grille(grille_pleine_1))

def verification_carre_grille(grille):
    dico_verificateur = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    for k in range(9):
        a={}
        grille_bis=np.copy(grille)
        grille_bis=np.reshape(grille_bis,81)
        for i in range(9):
            if grille_bis[9*k+i] in a.keys():
                a[grille_bis[9*k+i]]+=1
            else:
                a[grille_bis[9 * k + i]] = 1
        if a != dico_verificateur:
                return False
        return True

print(verification_carre_grille(grille_pleine_1))
