from fltk import*

HAUTEUR_FEN = 1080
LARGEUR_FEN = 1920
PIPI = LARGEUR_FEN/2
CACA = HAUTEUR_FEN/2
FONT_SIZE = 18

cree_fenetre(LARGEUR_FEN,HAUTEUR_FEN)

rectangle(0,0,LARGEUR_FEN,HAUTEUR_FEN,"","Black")
image(PIPI,130,"Rolit Logo.png",600,300,"center")
#Boutton Jouer
rectangle(PIPI - 120,PIPI/2 + 20,PIPI + 120,PIPI/2 + 95,"blue",'',3)
texte(PIPI,PIPI/2 + 57.5,"Jouer","white","center","",FONT_SIZE + 2)

#Boutton mode daltonien
rectangle(PIPI - 140,PIPI/2 + 125,PIPI + 140,PIPI/2 + 200,"blue",'',3)
texte(PIPI,PIPI/2 + 160,f"Mode Daltonien : OFF",'white',"center","",FONT_SIZE)
#Boutton Nombre de Joueurs
rectangle(PIPI - 200,PIPI/2 + 230,PIPI + 200,PIPI/2 + 305,"blue",'',3)
texte(PIPI,PIPI/2 + 267.5,"Nombre de Joueur : 1   2   3   4","white","center","",FONT_SIZE)
#Boutton Quitter 
rectangle(PIPI - 110,PIPI/2 + 335,PIPI + 110,PIPI/2 + 410,"blue",'',3)
texte(PIPI,PIPI/2 + 372.5,"Quitter","white","center","",FONT_SIZE)
#Cadre des High Score
rectangle(LARGEUR_FEN - 400,90,LARGEUR_FEN - 40,500,"blue","",3)
texte(LARGEUR_FEN - 210, 120,"Meilleurs Score","white","center")

#Cadre des règles
rectangle(90,90,500,800,"blue","",3)

#Texte d'entête 
texte(295,120,"Règle de Rolit",'white',"center","")
#Règle
def game_button():
    rectangle(PIPI - 120,PIPI/2 + 20,PIPI + 120,PIPI/2 + 95,"blue",'',3)
    texte(PIPI,)

attend_fermeture()

