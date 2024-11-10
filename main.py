#librairies importees 
import random
import sys

#fonctions utilitaires

def config(myMap,configNb):
    #pasSur de garder
    return 0


def isPlacable(myMap, coord):
    i = -1
    verifvar = 0
    while i < 2:
        k = - 1
        while k < 2:
            
            if k == 0 and i == 0:
                k += 1
            verifX,verifY = coord[0] + i,coord[1] + k
            
            if verifX < 0:
                i += 1
            elif verifX == len(myMap):
                break
            if verifY == len(myMap[0]):
                break
            elif verifY < 0:
                k += 1
            
            print(coord[1])
            if myMap[coord[0] + i][coord[1] + k] != '⬜':
                return True
            k += 1
        i += 1
    return False

def verif(myMap):
    return 0

 
def verifCase(myMap, coord):
    if myMap[coord[0]][coord[1]] != '⬜':
        print("Veuillez entrer des valeurs valide \n")
        return False
    return True


def verifDiagonal(myMap, playerColr, coord):
    
    return 0


"""def verifLineColumn(myMap, coord):
    playerColr = myMap[coord[0]][coord[1]] 
    #verif de ligne en premier
    i = 0
    while i != coord[1]:
        if playerColr == myMap[coord[0]][i]:
            for i in range(coord[1] - i):
                if myMap[coord[0]][i] == '':
                    return False
        
        i += 1
    
    
    
    #verif de colonne en secon
    return 0"""


def replaceColor(playerColr):
    
    return 0
    
def playerColor():
    
    return 0


# Cette fonction permet de creer une carte 
def Makemap(long,hauteur):

    table = []

    for i in range(long):
        subTable = []
        for j in range(hauteur):
            subTable.append(i*j)
            subTable[j] = '⬜'
            
        table.append(subTable)
     #Temporaire
    table[3][3] = '🟨'
    table[3][4] = '🟩'
    table[4][3] = '🟦'
    table[4][4] = '🟥'
    return table


def convertCoordinate(choice):
    if not (1 <= len(choice) <= 2):
        return None
    alphab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    coordx = alphab.index(choice[0])
    coordy = int(choice[1]) - 1
    coord = [coordx,coordy]
    return coord

# Cette fonction permet de placer une boule sur la carte
def placeBall(liste, playerColr:str, coordx,coordy):
    
    liste[coordx][coordy] = playerColr
    
    return liste


# Cette fonction affiche la carte
def affMap(lst):
    # temporaire
    print("   1  2  3  4  5  6  7  8")
    
    for i in range(len(lst)):
       print(f"{chr(65 + i)} " + " ".join(x for x in lst[i]))
    
    return None


userName = []
nbPlayer = int(input("Quelle est le nombre de joueur \n"))

for i in range(nbPlayer):
    print("Quel est le nom du joueur \n",i)
    Name = input("")
    userName.append(Name)

# on laisse l'utilisateur choisir la taille du tableau
print("Quelles sont les longueurs des cotes souhaites \n")

long = int(input("longueur du plateau"))
hauteur = int(input("largeur du plateau"))
playerColorTable = ["🟨","🟩","🟦","🟥"]
random.shuffle(playerColorTable)

print("l'ordre des joueur est", playerColorTable)


myMap = Makemap(long, hauteur)
affMap(myMap)
play = True
verification = False
#fonction principale de jeu

while play:
    
    for i in range(len(playerColorTable)):
        verification = False
        while not verification:
            
            choice = input("coord (allant de A a maxIndex et de 1 a maxIndex) \n")
            coord = convertCoordinate(choice)
            verification = verifCase(myMap, coord) and isPlacable(myMap,coord)
            
        myMap = placeBall(myMap,playerColorTable[i],coord[0],coord[1])
        
        
        
        affMap(myMap)
    #verif(myMap)