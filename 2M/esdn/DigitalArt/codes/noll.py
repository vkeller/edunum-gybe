# ------------------------------------------------------------------------------
# Programme pour recomposer l'oeuvre "Gaussian Quadratic", 1963 de Michael Noll
#
# Utilise les compétences en programmation des élèves de 2M
#
# Licence BSD, Vincent Keller, 2024
# ------------------------------------------------------------------------------
from turtle import Turtle, Screen
from random import *
from PIL import Image
from datetime import datetime

def rectangle(tortue,l1,l2):
    for i in range(2):
        tortue.forward(l1)
        tortue.left(90)
        tortue.forward(l2)
        tortue.left(90)

t = Turtle()
t.speed(100)

xmin = -300
xmax = 100
ymin = -300
ymax = 300

t.pensize(3)
t.penup()
t.goto(xmin,ymin)
t.pendown()
rectangle(t,xmax-xmin,ymax-ymin)
t.pensize(1)
t.pencolor('blue')

for i in range(60):
    x = randint(1,(xmax-xmin))+xmin
    y = randint(1,(ymax-ymin))+ymin
    if x >= xmin-1 and x <= xmax+1 and y >= ymin-1 and y <= ymax+1 :
        t.goto(x,y)
    else:
        i -= 1
        
        
# Sauvegarde de la fenêtre dans une image jpg
screen = Screen()
canvas = screen.getcanvas()
fileName = "noll_2024"
canvas.postscript(file=fileName+'.eps', width=(xmax-xmin)*1.4, height=(ymax-ymin)*1.2)
img = Image.open(fileName + '.eps') 
img.save(fileName + '.jpg')  