from random import randint
import turtle

star = turtle.Turtle()


def moveToRandomLocation():
    star.penup()
    star.setpos( randint(-360,360) , randint(-360,360) )
    star.pendown()

# Desenha uma estrela
def drawStar(starSize, starColour):
    star.color(starColour)
    star.pendown()
    star.begin_fill()
    for _ in range(5):
        star.left(144)
        star.forward(starSize)
    star.end_fill()
    star.penup()

# Galáxia
def drawGalaxy(numberOfStars):
    starColours = ["#058396","#0275A6","#827E01"]
    moveToRandomLocation()
    # Aglomerado de pontos coloridos
    for _ in range(numberOfStars):
        star.penup()
        star.left( randint(-180,180) )
        star.forward( randint(5,20) )
        star.pendown()
        drawStar( 2, starColours[randint(0, 2)])

# Constelação
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    for _ in range(numberOfStars-1):
        drawStar( randint(7,15) , "white")
        star.pendown()
        star.left( randint(-90,90) )
        star.forward( randint(30,70) )
    drawStar( randint(7,15) , "White")

def draw_backgroung():
    star.speed(11)

    # desenha 60 estrelas brancas (tamanhos/posições aleatórias)
    for _ in range(60):
        moveToRandomLocation()
        drawStar( randint(2,8) , "White")

    # desenha 4 galáxias
    for __ in range(4):
        drawGalaxy(40)

    # desenha 2 constelações
    for ___ in range(2):
        drawConstellation(randint(4,7))

    star.hideturtle()
