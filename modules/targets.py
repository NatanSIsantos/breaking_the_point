import turtle
import time
'''Este é o arquivo onde é configurado os parâmetros das gerações de fases,
pontuações, vida e afins'''

screen = turtle.Screen()

def game_over():
    loser = turtle.Turtle()
    loser.shape("square")
    loser.shapesize(stretch_wid=10, stretch_len=5)
    loser.speed(0)
    loser.color("red")
    loser.penup()
    loser.hideturtle()
    loser.goto(0, 0)

    loser.write(
        "GAME\n" + 
        "OVER\n", align="center", font=("Press Start 2P", 24, "normal"))
    screen.textinput("GAME OVER","Press [SPACE] to restart")
    screen.listen()


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
