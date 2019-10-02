import turtle
import time
from random import randint
'''Este é o arquivo onde é configurado os parâmetros das gerações de fases,
pontuações, vida e afins'''

screen = turtle.Screen()


def matrix_generator():
    blocks = open('files/blocks_matrix.txt', 'w')
    lin = 60  # núúmero de linhas
    col = 1  # núúmero de colunas
    for _ in range(lin):
        for _ in range(col):
            number = randint(0, 6)
            blocks.write(str(number))
        blocks.write('\n')
    blocks.close()

def block_printer():
    line = 300
    collum = -330
    blocks = open('files/blocks_matrix.txt', 'r')
    collum_list = []
    lines_list = []
    counter_null = 0
    for _ in blocks:

        block = turtle.Turtle()
        block.shape("square")
        block.shapesize(1, 2)
        block.speed(10)
        line_list = list(_)
        for __ in line_list:
            if __ == '\n':
                block.write("\n")
            elif __ == '0':
                block.color()
                block.penup()
                block.hideturtle()
                counter_null += 1
            elif __ == '1':
                block.color("#669933")  # Dark Green Block
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '2':
                block.color("#ccff99")  # Light Green Block
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '3':
                block.color("#ffcc99")  # Orange Block
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '4':
                block.color("#ff9999")  # Red Block
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '5':
                block.color("#999999")  # Gray Block
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '6':
                block.color()
                block.penup()
                block.hideturtle()
                counter_null += 1

            block.goto(collum, line)
            collum += 22
            if collum >= 330:
                collum = -330
                line -= 90

    blocks.close()
    return (lines_list[::], collum_list[::], counter_null)

loser = turtle.Turtle()
loser.shape("square")
loser.shapesize(stretch_wid=10, stretch_len=5)
loser.speed(0)
loser.color("white")
loser.penup()
loser.hideturtle()
loser.goto(-85, -200)
loser.fillcolor("black")


def game_over():
    loser.write(
        "SEE YOU,\n" +
        "SPACE TURTLE...\n" +
        "\n\nGAME OVER.", align="right", font=("Press Start 2P", 24, "normal"))
    loser.clear()
    time.sleep(3)
    screen.clear()


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
        time.sleep(0.5)
        counter.clear()
        counter._update()

'''def marker():
        t = turtle.Turtle()
        t.color("pink")
        t.hideturtle()
        t.goto(-280,310)
        t.left(140)
        t.forward(12)
        t.circle(-6,15)
        t.setheading(60)
        t.circle(-6,15)
        t.forward(12)'''
