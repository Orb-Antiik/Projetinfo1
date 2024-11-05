#librairies importees 
import random
import keyboard
import sys

#fonctions utilitaires

def verif(myMap):

    return 0


def verifCase(myMap, coord):
    if myMap[coord[0]][coord[1]] != None:
        return False
    return True

def verifDiagonal(myMap, playerColr, coord):
    
    return 0


def verifLineColumn(myMap, playerColr, coord):
    
    return 0


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
            subTable[j] = None
            
        table.append(subTable)
        
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


#Cette fonction affiche la carte
def affMap(lst):
    for i in range(len(lst)):
        print(lst[i])
    return None


userName = []
nbPlayer = 0

print("Quelles sont les longueurs des cotes souhaites")


# on laisse l'utilisateur choisir la taille du tableau
long = int(input("longueur du plateau"))
hauteur = int(input("largeur du plateau"))
playerColorTable = ["Jaune","Vert","Bleu","Rouge"]
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
            
            choice = input("coord (allant de A a maxIndex et de 1 a maxIndex)")
            coord = convertCoordinate(choice)
            verification = verifCase(myMap, coord)
        #faut faire mettre fonction de verif just lo
        myMap = placeBall(myMap,playerColorTable[i],coord[0],coord[1])
        
        affMap(myMap)
    #verif(myMap)
