#librairies importees 
import random
import sys

#fonctions utilitaires





def is_placable(map, coord):
    i = -1
    while i < 2:
        k = - 1
        while k < 2:
            
            if k == 0 and i == 0:
                k += 1
            verifX,verifY = coord[0] + i,coord[1] + k
            
            if verifX < 0:
                i += 1
            elif verifX == len(map):
                break
            if verifY == len(map[0]):
                break
            elif verifY < 0:
                k += 1
            
            if map[coord[0] + i][coord[1] + k] != '⬜':
                return True
            k += 1
        i += 1
    print("Veuillez entrer des valeur valide")
    return False



 
def verif_case(map, coord):
    
    if map[coord[0]][coord[1]] != '⬜':
        print("Veuillez entrer des valeurs valide \n")
        return False
    return True




def player_c(color_table,user_name):
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


# Cette fonction permet de creer une carte 
def make_map(long):

    table = []

    for i in range(long):
        sub_table = []
        for j in range(long):
            sub_table.append(i*j)
            sub_table[j] = '⬜'
            
        table.append(sub_table)
        
    middle = int(long/2)
    if long % 2 == 0:
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


def convert_coordinate(choice):
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


user_name = []
nb_player = int(input("Quelle est le nombre de joueur \n"))
assert nb_player <= 4

for i in range(nb_player):
    print("Quel est le nom du joueur  ",i + 1)
    name = input("")
    user_name.append(name)

# on laisse l'utilisateur choisir la taille du tableau
print("Quelles sont les longueurs des cotes souhaites")

long = int(input("taille du plateau ? \n"))

player_color_table = ["🟨","🟩","🟦","🟥"]

map = map(long)
player_and_colr_table = player_c(player_color_table,user_name)

aff_map(map)
play = True
verification = False
#fonction principale de jeu

while play:
    
    for i in range(len(player_and_colr_table)):
        verification = False
        turn(player_and_colr_table,i)
        while not verification:
            print("coord allant de A a "f'{chr(65 + long - 1)}' " et de 1 a",long)
            choice = input("")
            coord = convert_coordinate(choice)
            verification = verif_case(map, coord) and is_placable(map,coord)
            
        map = place_ball(map,player_and_colr_table[i][1],coord[0],coord[1])
             
        aff_map(map)
    #verif(map)