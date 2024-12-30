from math import cos, pi, sin
from fltk import*
from time import sleep as sl
from random import randint


HAUTEUR_FEN= 1080
LARGEUR_FEN= 1920
rayon = 200
cree_fenetre(LARGEUR_FEN,HAUTEUR_FEN)
mid_largeur = LARGEUR_FEN/2
mid_hauteur = HAUTEUR_FEN/2
ball_pos = (rayon + 30)/2
marche = 16
rotation = pi/marche
tour = 2*marche
nbr = randint(2,4)
cercle(mid_largeur,mid_hauteur,rayon,"","",3)
cercle(mid_largeur,mid_hauteur,rayon + 30,"black","",4)
ligne(mid_largeur ,mid_hauteur - 250 ,mid_largeur,mid_hauteur - 200,"black",5)
fleche(mid_largeur ,mid_hauteur - 250 ,mid_largeur,mid_hauteur - 200,"black",5)
def four_player_wheel():
    for i in range(tour*nbr):
        cercle(mid_largeur + ball_pos*cos(pi/2 + (i + 1)*pi/16),mid_hauteur + ball_pos*sin(pi/2 + (i + 1)*rotation),20,"blue","blue",3,"colorCircle")
        cercle(mid_largeur + ball_pos*cos(pi + (i + 1)*pi/16),mid_hauteur + ball_pos*sin(pi + (i + 1)*rotation),20,"red","red",3,"colorCircle")
        cercle(mid_largeur + ball_pos*cos(-pi/2 + (i + 1)*pi/16),mid_hauteur + ball_pos*sin(-pi/2 + (i + 1)*rotation),20,"green","green",3,"colorCircle") 
        cercle(mid_largeur + ball_pos*cos((i + 1)*pi/16),mid_hauteur + ball_pos*sin((i + 1)*rotation),20,"yellow","yellow",3,"colorCircle") 
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(pi/4 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(pi/4 + (i + 1)*rotation),"black",3,"trait")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(3*pi/4 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(3*pi/4 + (i + 1)*rotation),"black",3,"trait")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(-pi/4 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(-pi/4 + (i + 1)*rotation),"black",3,"trait")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(-3*pi/4 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(-3*pi/4 + (i + 1)*rotation),"black",3,"trait")
        mise_a_jour()
        sl(0.005*(i+ 1))
        if i != tour*nbr - 1:
            efface("colorCircle")
            efface("trait")

    return 0
def two_player_wheel():
    for i in range(tour*nbr):
        cercle(mid_largeur + ball_pos*cos(pi/2 + (i + 1)*pi/16),mid_hauteur + ball_pos*sin(pi/2 + (i + 1)*rotation),20,"blue","blue",3,"colorCircle")
        cercle(mid_largeur + ball_pos*cos(-pi/2+(i + 1)*pi/16),mid_hauteur + ball_pos*sin(-pi/2 +(i + 1)*rotation),20,"red","red",3,"colorCircle")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos((i + 1)*rotation),mid_hauteur + (rayon + 30)*sin((i + 1)*rotation),"black",3,"trait")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(pi + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(pi + (i + 1)*rotation),"black",3,"trait")
        mise_a_jour()
        sl(0.0025*(i+ 1))
        if i != tour*nbr - 1:
            efface("colorCircle")
            efface("trait")



    return 0

def three_player_wheel():

     for i in range(tour*nbr):
        cercle(mid_largeur + ball_pos*cos(-pi/2 + (i + 1)*pi/16),mid_hauteur + ball_pos*sin(- pi/2 + (i + 1)*rotation),20,"blue","blue",3,"colorCircle")
        cercle(mid_largeur + ball_pos*cos(-pi/2 + 2.09 + (i + 1)*pi/16),mid_hauteur + ball_pos*sin( -pi/2 +2.09 + (i + 1)*rotation),20,"red","red",3,"colorCircle")
        cercle(mid_largeur + ball_pos*cos(-pi/2 + 4.18 + (i + 1)*pi/16),mid_hauteur + ball_pos*sin(-pi/2 + 4.18 + (i + 1)*rotation),20,"green","green",3,"colorCircle") 
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(-pi/2 +1.045 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(-pi/2 +1.045 + (i + 1)*rotation),"black",3,"trait")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(-pi/2 +3.135 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(-pi/2+3.135 + (i + 1)*rotation),"black",3,"trait")
        ligne(mid_largeur,mid_hauteur,mid_largeur + (rayon +30) *cos(-pi/2 +5.225 + (i + 1)*rotation),mid_hauteur + (rayon + 30)*sin(-pi/2+5.255 + (i + 1)*rotation),"black",3,"trait")
        mise_a_jour()
        sl(0.0025*(i + 1))
        if i != tour*nbr - 1:
            efface("colorCircle")
            efface("trait") 


four_player_wheel()
attend_ev()

