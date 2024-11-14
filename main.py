#librairies importees 
import random
import sys

#fonctions utilitaires

def config(myMap,configNb):
    #pasSur de garder
    return 0


def isPlacable(myMap, coord):
    i = -1
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
            
            if myMap[coord[0] + i][coord[1] + k] != '⬜':
                return True
            k += 1
        i += 1
    print("Veuillez entrer des valeur valide")
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
    
    
    
    #verif de colonne en second
    return 0"""
def player(colorTable,userName):
    playerAndColorTable = []
    for i in range(len(userName)):
        print(userName[i],"choisissez une couleur \n 1-",colorTable[0],' \n 2-',colorTable[1],"\n 3-",colorTable[2],' \n 4-',colorTable[3])
        plResponse = int(input("Numero de la couleur ")) - 1
        playerAndColorTable.append([userName[i],colorTable[plResponse]])
    print(playerAndColorTable) 
        
    return playerAndColorTable

def replaceColor(playerColr,myMap,caseLst):
    return None
    
def playerColor(userName,playerColorTable):

    return None

# Cette fonction permet de creer une carte 
def Makemap(long,hauteur):

    table = []

    for i in range(long):
        subTable = []
        for j in range(hauteur):
            subTable.append(i*j)
            subTable[j] = '⬜'
            
        table.append(subTable)
        
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


def convertCoordinate(choice):
    if not (1 <= len(choice) <= 3):
        return None
    if len(choice) == 3:
        nbChoice = choice[1] + choice[2]
    else:
        nbChoice = choice[1]
    alphab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    coordx = alphab.index(choice[0])
    coordy = int(nbChoice) - 1
    coord = [coordx,coordy]
    return coord

# Cette fonction permet de placer une boule sur la carte
def placeBall(liste, playerColr, coordx,coordy):
    
    liste[coordx][coordy] = playerColr
    
    return liste


# Cette fonction affiche la carte
def affMap(lst):

    for i in range(len(lst)):
        if i == 0:
            print("   " ,end ='')
        print(i + 1,end='  ')

    
    for i in range(len(lst)):
       if i == 0:
           print("")
       print(f"{chr(65 + i)} " + " ".join(x for x in lst[i]))
    
    return None


userName = []
nbPlayer = int(input("Quelle est le nombre de joueur \n"))
assert nbPlayer <= 4

for i in range(nbPlayer):
    print("Quel est le nom du joueur \n",i)
    Name = input("")
    userName.append(Name)

# on laisse l'utilisateur choisir la taille du tableau
print("Quelles sont les longueurs des cotes souhaites")

long = int(input("longueur du plateau \n"))
hauteur = int(input("largeur du plateau \n"))
playerColorTable = ["🟨","🟩","🟦","🟥"]
random.shuffle(playerColorTable)

print("l'ordre des joueur est", playerColorTable)

player(playerColorTable,userName)
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