#librairies importees 
import random
import sys
print("ha")
#fonctions utilitaires--------------------------------------------------------------------

def is_placable(my_map, coord):
    i = -1
    while i < 2:
        k = - 1
        while k < 2:
            
            if k == 0 and i == 0:
                k += 1
            verifX,verifY = coord[0] + i,coord[1] + k
            
            if verifX < 0:              #Permet de vérifier si il y a dépassement en haut
                i += 1
            elif verifX == len(my_map): #Permet de vérifier si il y a dépassement en bas
                break
            if verifY == len(my_map[0]): #Permet de vérifier si il y a dépassement à droite 
                break
            elif verifY < 0:            #Permet de vérifier si il y a dépassement à gauche
                k += 1
            
            if my_map[coord[0] + i][coord[1] + k] != '⬜':
                return True
            k += 1
        i += 1
    print("Veuillez entrer des valeurs valides")
    return False


def game_continue(my_map):      #Détermine quand la partie finie !!!
    lost_lst = []
    for elt in my_map:
        for sous_liste in elt:
            lost_lst.append(sous_liste)
    for elt in lost_lst:
        if elt == '⬜':
            return True
        print("La partie est terminée !")
        return False

 
def verif_case(my_map, coord):
    
    if my_map[coord[0]][coord[1]] != '⬜':
        print("Veuillez entrer des valeurs valides \n")
        return False
    return True




def player_c(color_table,user_name):        #Associe une couleur choisie par le joueur au joueur 
    player_and_color_table = []
    for i in range(len(user_name)):
        print(user_name[i],"choisissez une couleur")
        for k in range(len(color_table)):
            print(k + 1,'-',color_table[k])
        pl_response = int(input("Numero de la couleur ")) - 1
        player_and_color_table.append([user_name[i],color_table[pl_response]])
        if len(color_table) > 1:
            print(pl_response)
            color_table.pop(pl_response)
    print(player_and_color_table) 
        
    return player_and_color_table

def turn(player_and_colr_table,i):
    print("c'est au tour de ",player_and_colr_table[i][0],"avec la couleur",player_and_colr_table[i][1] )
    return 0


# Cette fonction permet de creer un plateau
 
def make_map(cote):

    table = []

    for i in range(cote):
        sub_table = []
        for j in range(cote):
            sub_table.append(i*j)
            sub_table[j] = '⬜'
        table.append(sub_table)
        
    middle = int(cote/2)
    if cote % 2 == 0:
        table[middle - 1][middle - 1] = '🟨'
        table[middle - 1][middle] = '🟩'
        table[middle ][middle - 1] ='🟦'
        table[middle][middle] = '🟥'
    else:
        table[middle - 1][middle - 1] = '🟨'
        table[middle - 1][middle + 1] = '🟩'
        table[middle + 1][middle - 1] = '🟦'
        table[middle + 1][middle + 1] = '🟥'
  
    return table


def convert_coordinate(choice):                 #transforme coordonnees lettre chiffre en coordonnees de liste
    if not (1 <= len(choice) <= 3):
        return None
    if len(choice) == 3:
        nb_choice = choice[1] + choice[2]
    else:
        nb_choice = choice[1]
    alphab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    coordx = alphab.index(choice[0])
    coordy = int(nb_choice) - 1
    coord = [coordx,coordy]
    return coord

# Cette fonction permet de placer une boule sur la carte
def place_ball(liste, player_colr, coordx,coordy):
    
    liste[coordx][coordy] = player_colr
    
    return liste


# Cette fonction affiche la carte
def aff_map(lst):

    for i in range(len(lst)):
        if i == 0:
            print("   " ,end ='')
        print(i + 1,end='  ')

    
    for i in range(len(lst)):
       if i == 0:
           print("")
       print(f"{chr(65 + i)} " + " ".join(x for x in lst[i]))
       
    
    return None



def voisin_axe(my_map,coord,cote,player_and_color_table,i):
    """
    Capture en axiale les coordonnes voisines au point place par le joueur
    x = ligne du plateau
    y = colonne du plateau
    cote = longueur et largeur du plateau 

    """
    lst_voisin = []
    x,y = coord
    for k in range(1,cote):                                             #haut     
        if x-k>= 0 and my_map[x-k][y] == player_and_colr_table[i][1]:
            lst_voisin.append((x-k,y))
            for m in range(1,k):
                my_map[x-m][y] = player_and_colr_table[i][1]


    for k in range(1,cote):                                             #bas
        if x+k < cote and my_map[x+k][y] == player_and_colr_table[i][1]:
            lst_voisin.append((x+k,y))
            for m in range(1,k):
                my_map[x+m][y] = player_and_colr_table[i][1]


    for k in range(1,cote):                                             #gauche 
        if y-k >= 0 and my_map[x][y-k] == player_and_colr_table[i][1]:         
            lst_voisin.append((x,y-i))
            for m in range(1,k):
                my_map[x][y-m] = player_and_colr_table[i][1]


    for k in range(1,cote):                                             #droite
        if y+k<cote and my_map[x][y+k] == player_and_colr_table[i][1]:
            lst_voisin.append((x,y+i))
            for m in range(1,k):
                my_map[x][y+m] = player_and_colr_table[i][1]


    return lst_voisin

#PROBLEME AVEC LES CASES BLANCHES DONC CONDITION A REVOIR


def voisin_diag(my_map,coord,cote,player_and_colr_table,i):
    """Capture en diagonale les cordoonees voisines au point place par le joueur
    x = ligne du plateau
    y = colonne du plateau
    cote = longueur et largeur du plateau 


    """

    l_diag = []
    x,y = coord
    for k in range(1,cote):                 #haut gauche
        if x-k >= 0 and y-k >= 0 and my_map[x-k][y-k] == player_and_colr_table[i][1] :
            l_diag.append((x-k,y-k))
            for m in range(1,k):
                my_map[x-m][y-m] = player_and_colr_table[i][1]

        
    for k in range(1,cote):                 #bas gauche
        if x +k < cote and y-k >= 0 and my_map[x+k][y-k] == player_and_colr_table[i][1]:
            l_diag.append((x+k,y-k))
            for m in range(1,k):
                 my_map[x+m][y-m] = player_and_colr_table[i][1]

    
    for k in range(1,cote):                 #haut droite
        if y+k < cote and x-k >= 0 and my_map[x-k][y+k] == player_and_colr_table[i][1]:
            l_diag.append((x-k,y+k))
            for m in range(1,k):
                 my_map[x-m][y+m] = player_and_colr_table[i][1]

    
    for k in range(1,cote):
        if y+k< cote and x+k < cote and my_map[x+k][y+k] == player_and_colr_table[i][1]:       #bas droite
            l_diag.append((x+k,y+k))
            for m in range(1,k):
                 my_map[x+m][y+m] = player_and_colr_table[i][1]

    return l_diag



def score(my_map):      #Détermine le score !!! je dois ajouter player color et i pour le print 
    score_lst = []
    r = 0
    j = 0
    v = 0
    b = 0
    for elt in my_map:
        for sous_liste in elt:
            score_lst.append(sous_liste)
    for elt in score_lst:
        if elt == '🟨':
            j += 1
        elif elt == '🟩':
            v += 1
        elif elt == '🟦':
            b += 1
        elif elt == '🟥':
            r += 1

    print("Le score est :" "-rouge =",r,"-jaune =",j,"-bleu =",b,"-vert = ",v)
    
    return j,v,b,j

            
    











user_name = []
nb_player = int(input("Quelle est le nombre de joueur entre 2 et 4 \n"))
assert 2 <= nb_player <= 4

for i in range(nb_player):
    print("Quel est le nom du joueur  ",i + 1)
    name = input("")
    user_name.append(name)

# on laisse l'utilisateur choisir la taille du tableau
print("Quelles sont les longueurs des cotes souhaites")

cote = int(input("taille du plateau ? \n"))

player_color_table = ["🟨","🟩","🟦","🟥"]

my_map = make_map(cote)
player_and_colr_table = player_c(player_color_table,user_name)

scoregame = score(my_map)

aff_map(my_map)
play = True
verification = False


#Main du jeu------------------------------------------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    while play:
        
        for i in range(len(player_and_colr_table)):
            verification = False
            turn(player_and_colr_table,i)
            while not verification:
                print("coord allant de A a "f'{chr(65 + cote - 1)}' " et de 1 a",cote) #chr tu vas chercher un caractère avec son indice dans la table ascii
                choice = input("")

                coord = convert_coordinate(choice)

                verification = verif_case(my_map, coord) and is_placable(my_map,coord)

                play = game_continue(my_map)

            diag = voisin_diag(my_map,coord,cote,player_and_colr_table,i)
            axe = voisin_axe(my_map,coord,cote,player_and_colr_table,i)
                

            my_map = place_ball(my_map,player_and_colr_table[i][1],coord[0],coord[1])
            scoregame = score(my_map)
            #print("Les coordonnes axiales voisines sont",axe)
            #print("Les coordonnes diag voisines sont",diag)
            aff_map(my_map)



#Interface graphique---------------------------------------------------------------------------------------------------------------------------------------------------
cree_fenetre(600,600)
