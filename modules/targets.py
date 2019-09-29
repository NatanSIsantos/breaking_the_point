import turtle
import time
'''Este é o arquivo onde é configurado os parâmetros das gerações de fases,
pontuações, vida e afins'''

heart = turtle.Turtle()


def game_over():  # condição de derrota
    loser = turtle.Turtle("square")
    loser.speed(0)
    loser.color("lightred")
    loser.shapesize(stretch_wid=10, stretch_len=5)
    loser.penup()
    loser.hideturtle()
    loser.goto(0, 0)

    if life == 0:
        loser.write(
            "GAME\n" +
            "OVER\n", align="center", font=("Press Start 2P", 30, "normal"))
        life = 3
        loser.clear()
        heart.clear()
        heart.write("{} lifes".format(life), align="center", font=(
            "Press Start 2P", 24, "normal"))

def counter():
    counter = turtle.Turtle("square")
    counter.speed(0)
    counter.color("lightgreen")
    counter.penup()
    counter.hideturtle()
    counter.goto(0, 0)
    for i in range(0, 3):
        counter.write("\r{}".format(-1*(i-3)), align="center", font=(
            "Press Start 2P", 18, "normal"))
        time.sleep(1)
        counter.clear()
        counter._update()
