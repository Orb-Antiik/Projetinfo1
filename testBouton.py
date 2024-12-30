from fltk import*
from time import sleep

def ButtonAppearance(x,y,color,width,text):

    ax,ay = x
    bx,by = y
     
    rectangle(ax,ay,bx,by,color,"white",width)
    texte(ax + abs(bx - ax)/2,ay + abs(ay - by)/2,text,color,"center","",18)

def ButtonHover(x,y,color,width,text,cl):
    ax,ay = x
    bx,by = y
    if ax <= cl[0] <= bx or ay <= cl[1] <= by:
        rectangle(ax,ay,bx,by,color,"#606160",width)
        texte(ax + abs(bx - ax)/2,ay + abs(ay - by)/2,text,color,"center","",18)


def ButtonOnClick():
    return 0

def ButtonAction():
    return 0

def clic():
    cl = []
    ev = attend_ev()
    typeEv = type_ev(ev)
    if typeEv == "ClicGauche" :
        x, y = abscisse(ev), ordonnee(ev)
        cl.append(x)
        cl.append(y)
    print(cl)
    return cl


cree_fenetre(1000,1000)



play = True
while play:
    pointA = (100,200)
    pointB = (300,400)
    text = "Test"
    ButtonAppearance(pointA,pointB,"blue",5,text)
    cl = clic()
    ButtonHover(pointA,pointB,"gray",5,text,cl)
    mise_a_jour()
    sleep(0.3)
attend_fermeture()
