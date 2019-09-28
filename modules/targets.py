import turtle
'''Este é o arquivo onde é configurado os parâmetros das gerações de fases,
pontuações, vida e afins'''

#display de vidas
def life():
    heart = turtle.Turtle()
    heart.speed(0)
    heart.shape("square")
    heart.color("red")
    heart.penup()
    heart.hideturtle()
    heart.goto(-300, 310)
    heart.write("3 lifes", align="center", font=("Press Start 2P", 24, "normal"))

    