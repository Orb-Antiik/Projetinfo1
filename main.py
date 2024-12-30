#librairies importees 
import random
from fltk import*
import verification
import board
from constants import LIGNE,COLONNE,TAILLE_CASE,LARGEUR_FEN,AD,X_OFFSET,Y_OFFSET 

#fonctions utilitaires--------------------------------------------------------------------

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
    li = -1 
    col = -1
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
def place_ball(liste, player_colr, cornerx,cornery):
    
    liste[cornerx][cornery] = player_colr
    cercle(AD/2 + (cornery*2 + 1)*TAILLE_CASE/2,AD + (cornerx*2 + 1)*TAILLE_CASE/2,13,player_colr,player_colr,3) 
    return liste





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


my_map = board.make_map(LIGNE)
user_name = []
nb_player = int(input("Quelle est le nombre de joueur entre 2 et 4 \n"))
assert 2 <= nb_player <= 4

efface('recScore')
rectangle(LARGEUR_FEN - 4* TAILLE_CASE,AD,LARGEUR_FEN - 20,AD + 150 + (nb_player - 2)*60,"black","",4)


for i in range(nb_player):
    print("Quel est le nom du joueur  ",i + 1)
    name = input("")
    user_name.append(name)

player_color_table = ["yellow","green","blue","red"]


player_and_colr_table = player_c(player_color_table,user_name)

scoregame = score(my_map)
play = True
verif_var = False
shuffled_table = random.shuffle(player_and_colr_table)

#Main du jeu------------------------------------------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    while play:
        
        for i in range(len(player_and_colr_table)):
            verif_var = False
            turn(player_and_colr_table,i)
            while not verif_var:
                

                play = game_continue(my_map)
                lst = clic()
                print(lst) 
                corner = pix_vers_cel(lst[0],lst[1],COLONNE,TAILLE_CASE,X_OFFSET,Y_OFFSET)
                while not (0 <= corner[0] <= 7 and 0 <= corner[1] <= 7) :
                    lst = clic()
                    corner = pix_vers_cel(lst[0],lst[1],COLONNE,TAILLE_CASE,X_OFFSET,Y_OFFSET)

                verif_var = verification.verif_case(my_map, corner) and verification.is_placable(my_map,corner)

            
                

            diag = verification.voisin_diag(my_map,corner,LIGNE,player_and_colr_table,i)
            axe = verification.voisin_axe(my_map,corner,LIGNE,player_and_colr_table,i)

            my_map = place_ball(my_map,player_and_colr_table[i][1],corner[0],corner[1])

            scoregame = score(my_map)
            efface("points")
            for i in range(nb_player):
                cercle(LARGEUR_FEN - 4* TAILLE_CASE + 30,AD + 60*(i + 1),13,"",player_and_colr_table[i][1],4)
                name_size = len(player_and_colr_table[i][0])
                texte(LARGEUR_FEN - 4* TAILLE_CASE + 90 + 5*name_size,AD + 60*(i + 1),player_and_colr_table[i][0] + f"  {scoregame[player_and_colr_table[i][1]]}","black",'center',"",18,"points")

            #print("Les corneronnes axiales voisines sont",axe)
            #print("Les corneronnes diag voisines sont",diag)
    ferme_fenetre()
