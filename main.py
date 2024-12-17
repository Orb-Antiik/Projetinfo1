#librairies importees 
import random
import sys
from fltk import*

LIGNE = 8
COLONNE = 8
TAILLE_CASE = 70
LARGEUR_FEN = 1000
HAUTEUR_FEN = 1000
AD = int(LARGEUR_FEN/2 - (TAILLE_CASE * (LIGNE/2)))         #Centrer le plateau 
X_OFFSET = AD/2      
Y_OFFSET = AD

cree_fenetre(LARGEUR_FEN,HAUTEUR_FEN)

rectangle(0,0,LARGEUR_FEN,HAUTEUR_FEN,"","white")
rectangle(AD/2,AD,AD/2 + LIGNE*TAILLE_CASE,AD + COLONNE*TAILLE_CASE ,'#18191a','#18191a')

rectangle(LARGEUR_FEN - 4* TAILLE_CASE,AD,LARGEUR_FEN - 20,AD + 150,"black","",4,"recScore")
texte(LARGEUR_FEN - 4*TAILLE_CASE + (LARGEUR_FEN - 20 - (LARGEUR_FEN - 4*TAILLE_CASE))/2 ,AD + 20,"Score :",'black',"center")
for i in range(8):
    texte(AD/2 - 25,AD + (i * 2 + 1)*TAILLE_CASE/2,f"{chr(65 + i)}","black","center")
for i in range(8):
    texte(AD/2 + (i * 2 + 1)*TAILLE_CASE/2,AD - 25,f"{ i + 1}","black","center")

#fonctions utilitaires--------------------------------------------------------------------
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

def clic():
    cl = []
    ev = attend_ev()
    typeEv = type_ev(ev)
    if typeEv == "ClicGauche" :
        x, y = abscisse(ev), ordonnee(ev)
        cl.append(x)
        cl.append(y)
    return cl

def pix_vers_cel(x, y, taille, taille_cel, X_OFFSET, Y_OFFSET) :
    """
    Calcule les références de la cellule dans laquelle le point (x, y) se situe.
    Les bords Ouest et Nord appartiennent à la cellule.
    """
    col = int((x - X_OFFSET)//taille_cel)
    li = int((y - Y_OFFSET)//taille_cel)
    return li, col

def game_continue(my_map):      #Détermine quand la partie finie !!!

    for elt in my_map:
        for case in elt:
            if case == 'empty':
                return True
    print('La partie est finie')
    return False
            

 
def verif_case(my_map, corner):
    
    if my_map[corner[0]][corner[1]] != 'empty':
        print("Veuillez entrer des valeurs valides \n")
        return False
    return True




def player_c(color_table,user_name):        #Associe une couleur choisie par le joueur au joueur 
    player_and_color_table = []
    color_dict = {"jaune":"yellow","rouge":"red","bleu":"blue","vert":"green"}
    for i in range(len(user_name)):

        print("couleur dispo"," ".join([x for x in color_dict]))
        print(user_name[i],"Quelle couleur choisissez vous")
        pl_ans = input("")
        pl_ans = pl_ans.lower()
        player_and_color_table.append([user_name[i],color_dict[pl_ans]])
        del color_dict[pl_ans] 
        
    return player_and_color_table

def turn(player_and_colr_table,i):
    print("c'est au tour de ",player_and_colr_table[i][0],"avec la couleur",player_and_colr_table[i][1] )
    return 0


# Cette fonction permet de creer un plateau
 
def make_map(cote,TAILLE_CASE,AD):
    table = []

    for i in range(cote):
        sub_table = []
        for k in range(cote):
            sub_table.append(i*k)
            sub_table[k] = 'empty'
            rectangle( AD/2 + i*TAILLE_CASE,AD + k * TAILLE_CASE, AD/2 + (i + 1)*TAILLE_CASE,AD + (k + 1) * (TAILLE_CASE) ,'#343638','',3)
        table.append(sub_table)
        
    middle = int(cote/2)
    table[middle - 1][middle - 1] = 'yellow'
    table[middle - 1][middle] = 'green'
    table[middle ][middle - 1] ='blue'
    table[middle][middle] = 'red'
    cercle(AD/2 + ((middle - 1)*2 + 1)*TAILLE_CASE/2,AD + ((middle - 1) * 2 + 1)*TAILLE_CASE/2,13,"yellow","yellow",3)
    cercle(AD/2 + ((middle)*2 + 1)*TAILLE_CASE/2,AD + ((middle - 1) * 2 + 1)*TAILLE_CASE/2,13,"green","green",3)
    cercle(AD/2 + ((middle - 1)*2 + 1)*TAILLE_CASE/2,AD + (middle * 2 + 1)*TAILLE_CASE/2,13,"blue","blue",3)
    cercle(AD/2 + (middle *2 + 1)*TAILLE_CASE/2,AD + (middle * 2 + 1)*TAILLE_CASE/2,13,"red","red",3)

    return table


def convert_cornerinate(choice):                 #transforme corneronnees lettre chiffre en corneronnees de liste
    if not (1 <= len(choice) <= 3):
        return None
    if len(choice) == 3:
        nb_choice = choice[1] + choice[2]
    else:
        nb_choice = choice[1]
    alphab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cornerx = alphab.index(choice[0])
    cornery = int(nb_choice) - 1
    corner = [cornerx,cornery]
    return corner

# Cette fonction permet de placer une boule sur la carte
def place_ball(liste, player_colr, cornerx,cornery,TAILLE_CASE):
    
    liste[cornerx][cornery] = player_colr
    cercle(AD/2 + (cornery*2 + 1)*TAILLE_CASE/2,AD + (cornerx*2 + 1)*TAILLE_CASE/2,13,player_colr,player_colr,3) 
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
        if elt == 'yellow':
            j += 1
        elif elt == 'green':
            v += 1
        elif elt == 'blue':
            b += 1
        elif elt == 'red':
            r += 1

    dico_point = {"yellow":j,"green":v,"blue":b,"red":r}
    return dico_point
cote = 8
my_map = make_map(cote,TAILLE_CASE,AD)
user_name = []
nb_player = int(input("Quelle est le nombre de joueur entre 2 et 4 \n"))
assert 2 <= nb_player <= 4

efface('recScore')
rectangle(LARGEUR_FEN - 4* TAILLE_CASE,AD,LARGEUR_FEN - 20,AD + 150 + (nb_player - 2)*50,"black","",4)


for i in range(nb_player):
    print("Quel est le nom du joueur  ",i + 1)
    name = input("")
    user_name.append(name)

player_color_table = ["yellow","green","blue","red"]


player_and_colr_table = player_c(player_color_table,user_name)

scoregame = score(my_map)
play = True
verification = False
shuffled_table = random.shuffle(player_and_colr_table)

#Main du jeu------------------------------------------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    while play:
        
        for i in range(len(player_and_colr_table)):
            verification = False
            turn(player_and_colr_table,i)
            while not verification:
                

                play = game_continue(my_map)
                lst = clic()
                corner = pix_vers_cel(lst[0],lst[1],COLONNE,TAILLE_CASE,X_OFFSET,Y_OFFSET)

                verification = verif_case(my_map, corner) and is_placable(my_map,corner)

            
                

            diag = voisin_diag(my_map,corner,cote,player_and_colr_table,i)
            axe = voisin_axe(my_map,corner,cote,player_and_colr_table,i)

            my_map = place_ball(my_map,player_and_colr_table[i][1],corner[0],corner[1],TAILLE_CASE)

            scoregame = score(my_map)
            efface("points")
            for i in range(nb_player):
                cercle(LARGEUR_FEN - 4* TAILLE_CASE + 30,AD + 60*(i + 1),13,"",player_and_colr_table[i][1],4)
                name_size = len(player_and_colr_table[i][0])
                texte(LARGEUR_FEN - 4* TAILLE_CASE + 90 + 5*name_size,AD + 60*(i + 1),player_and_colr_table[i][0] + f"  {scoregame[player_and_colr_table[i][1]]}","black",'center',"",18,"points")

            #print("Les corneronnes axiales voisines sont",axe)
            #print("Les corneronnes diag voisines sont",diag)
    ferme_fenetre()
