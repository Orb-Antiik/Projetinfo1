from fltk import*
from constants import LARGEUR_FEN,HAUTEUR_FEN,AD,TAILLE_CASE,LIGNE,COLONNE


cree_fenetre(LARGEUR_FEN,HAUTEUR_FEN)

#on cree le background de la fenêtre puis on cree le background du plateau
rectangle(0,0,LARGEUR_FEN,HAUTEUR_FEN,"","white")
rectangle(AD/2,AD,AD/2 + LIGNE*TAILLE_CASE,AD + COLONNE*TAILLE_CASE ,'#18191a','#18191a')

#on affiche "Score :" avec son encadré 
rectangle(LARGEUR_FEN - 4* TAILLE_CASE,AD,LARGEUR_FEN - 20,AD + 150,"black","",4,"recScore")
texte(LARGEUR_FEN - 4*TAILLE_CASE + (LARGEUR_FEN - 20 - (LARGEUR_FEN - 4*TAILLE_CASE))/2 ,AD + 20,"Score :",'black',"center")

#on affiche les coordonnées sur le coté du plateau
for i in range(8):
    texte(AD/2 - 25,AD + (i * 2 + 1)*TAILLE_CASE/2,f"{chr(65 + i)}","black","center")
for i in range(8):
    texte(AD/2 + (i * 2 + 1)*TAILLE_CASE/2,AD - 25,f"{ i + 1}","black","center")


# cette fonction cree le tableau et le plateau avec tkinter
def make_map(cote):
    table = []

    for i in range(cote):
        sub_table = []
        for k in range(cote):
            sub_table.append(i*k)
            sub_table[k] = 'empty'
            rectangle( AD/2 + i*TAILLE_CASE,AD + k * TAILLE_CASE, AD/2 + (i + 1)*TAILLE_CASE,AD + (k + 1) * (TAILLE_CASE) ,'#343638','',3)
        table.append(sub_table)
       
    
    #on place les points centraux du plateau sur le tableau et le plateau
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

