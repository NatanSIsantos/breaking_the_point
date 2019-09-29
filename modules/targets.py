import turtle
'''Este é o arquivo onde é configurado os parâmetros das gerações de fases,
pontuações, vida e afins'''

heart = turtle.Turtle()

#condição de derrota
def game_over():
    loser = turtle.Turtle("square")
    loser.speed(0)
    loser.color("lightred")
    loser.shapesize(stretch_wid=10, stretch_len=5)
    loser.penup()
    loser.hideturtle()
    loser.goto(0,0)

    if life == 0:
        loser.write(
            "GAME\n" + 
            "OVER\n", align="center", font=("Press Start 2P", 30, "normal"))
        life = 3
        loser.clear()
        heart.clear()
        heart.write("{} lifes".format(life), align="center", font=("Press Start 2P", 24, "normal"))
