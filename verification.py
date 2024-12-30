#fonctions pour vérifier si la boule est placable 
from fltk import*
from constants import TAILLE_CASE,AD 

def is_placable(my_map, corner):
    i = -1
    while i < 2:
        k = - 1
        while k < 2:
            
            if k == 0 and i == 0:
                k += 1
            verifX,verifY = corner[0] + i,corner[1] + k
            
            if verifX < 0:              #Permet de vérifier si il y a dépassement en haut
                i += 1
            elif verifX == len(my_map): #Permet de vérifier si il y a dépassement en bas
                break
            if verifY == len(my_map[0]): #Permet de vérifier si il y a dépassement à droite 
                break
            elif verifY < 0:            #Permet de vérifier si il y a dépassement à gauche
                k += 1
            
            if my_map[corner[0] + i][corner[1] + k] != 'empty':
                return True
            k += 1
        i += 1
    print("Veuillez entrer des valeurs valides")
    return False


def verif_case(my_map, corner):
    
    if my_map[corner[0]][corner[1]] != 'empty':
        print("Veuillez entrer des valeurs valides \n")
        return False
    return True

#fonction pour vérifier les coordoonnées à capturer

def voisin_axe(my_map,corner,cote,player_and_colr_table,i):
    
    """
    Capture en axiale les corneronnes voisines au point place par le joueur
    x = LIGNE du plateau
    y = COLONNE du plateau
    cote = longueur et largeur du plateau 

    """
    lst_voisin = []
    x,y = corner
    for k in range(1,cote):                                             #haut     
        if x-k>= 0:
            if my_map[x-k][y] == 'empty':
                break
            if my_map[x-k][y] == player_and_colr_table[i][1]:               
                for m in range(1,k):
                    my_map[x-m][y] = player_and_colr_table[i][1]
                    cercle(AD/2 + (y*2 + 1)*TAILLE_CASE/2, AD + ((x-m)*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3)
            lst_voisin.append((x-k,y))


    for k in range(1,cote):                                             #bas
        if x+k< cote:
            if my_map[x+k][y] == 'empty':
                break
            if my_map[x+k][y] == player_and_colr_table[i][1]:               
                for m in range(1,k):
                    my_map[x+m][y] = player_and_colr_table[i][1]
                    cercle(AD/2 + (y*2 + 1)*TAILLE_CASE/2, AD + ((x + m)*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3)
            lst_voisin.append((x+k,y))


    for k in range(1,cote):                                             #gauche 
        if y-k>= 0:
            if my_map[x][y-k] == 'empty':
                break
            if my_map[x][y-k] == player_and_colr_table[i][1]:               
                for m in range(1,k):
                    my_map[x][y-m] = player_and_colr_table[i][1]
                    cercle(AD/2 + ((y - m)*2 + 1)*TAILLE_CASE/2, AD + (x*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3)

            lst_voisin.append((x,y-k))


    for k in range(1,cote):                                             #droite
        if y+k < cote :
            if my_map[x][y+k] == 'empty':
                break
            if my_map[x][y+k] == player_and_colr_table[i][1]:               
                for m in range(1,k):
                    my_map[x][y+m] = player_and_colr_table[i][1]
                    cercle(AD/2 + ((y + m)*2 + 1)*TAILLE_CASE/2, AD + (x*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3)

            lst_voisin.append((x,y+k))

    return lst_voisin


def voisin_diag(my_map,corner,cote,player_and_colr_table,i):
    """Capture en diagonale les corneronnées voisines au point placé par le joueur
    x = LIGNE du plateau
    y = COLONNE du plateau
    cote = longueur et largeur du plateau 
    """
    l_diag = []
    x, y = corner

    for k in range(1, cote):  # haut gauche
        if x-k >= 0 and y-k >= 0:
            if my_map[x-k][y-k] == 'empty':  # Si une case blanche est sur le chemin, c'est CIAOOO
                break
            if my_map[x-k][y-k] == player_and_colr_table[i][1]:  
                for m in range(1, k):  
                    my_map[x-m][y-m] = player_and_colr_table[i][1]
                    cercle(AD/2 + ((y - m)*2 + 1)*TAILLE_CASE/2, AD + ((x-m)*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3) 
                l_diag.append((x-k, y-k))
                

    for k in range(1, cote):  # bas gauche
        if x+k < cote and y-k >= 0:
            if my_map[x+k][y-k] == 'empty':  
                break
            if my_map[x+k][y-k] == player_and_colr_table[i][1]:  
                for m in range(1, k): 
                    my_map[x+m][y-m] = player_and_colr_table[i][1]
                    cercle(AD/2 + ((y - m)*2 + 1)*TAILLE_CASE/2, AD + ((x+m)*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3) 

                l_diag.append((x+k, y-k))
                

    for k in range(1, cote):  # haut droite
        if y+k < cote and x-k >= 0:
            if my_map[x-k][y+k] == 'empty':  
                break
            if my_map[x-k][y+k] == player_and_colr_table[i][1]:  
                for m in range(1, k):  
                    my_map[x-m][y+m] = player_and_colr_table[i][1]
                    cercle(AD/2 + ((y + m)*2 + 1)*TAILLE_CASE/2, AD + ((x-m)*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3) 

                l_diag.append((x-k, y+k))
                

    for k in range(1, cote):  # bas droite
        if y+k < cote and x+k < cote:
            if my_map[x+k][y+k] == 'empty': 
                break
            if my_map[x+k][y+k] == player_and_colr_table[i][1]:  
                for m in range(1, k):  
                    my_map[x+m][y+m] = player_and_colr_table[i][1]
                    cercle(AD/2 + ((y + m)*2 + 1)*TAILLE_CASE/2, AD + ((x + m)*2 + 1)*TAILLE_CASE/2,13,player_and_colr_table[i][1],player_and_colr_table[i][1],3) 

                l_diag.append((x+k, y+k))
    return l_diag
