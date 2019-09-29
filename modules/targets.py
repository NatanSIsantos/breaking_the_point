import turtle
import time
from random import randint
'''Este é o arquivo onde é configurado os parâmetros das gerações de fases,
pontuações, vida e afins'''

screen = turtle.Screen()


def matrix_generator():
    blocks = open('files/blocks_matrix.txt', 'w')
    lin = 5  # núúmero de linhas
    col = 8  # núúmero de colunas
    for _ in range(lin):
        for _ in range(col):
            number = randint(0, 4)
            blocks.write(str(number))
        blocks.write('\n')
    blocks.close()


def block_printer():
    line = 0
    collum = 0
    blocks = open('files/blocks_matrix.txt', 'r')

    for _ in blocks:

        block = turtle.Turtle()
        block.shape("square")
        block.shapesize(4, 1)
        block.speed(10)
        line_list = list(_)

        for __ in line_list:
            if __ == '\n':
                block.write("\n")
            elif __ == '0':
                block.color()
                block.penup()
                block.hideturtle()
            elif __ == '1':
                block.color("green")
                block.penup()
                block.hideturtle()
            elif __ == '2':
                block.color("blue")
                block.penup()
                block.hideturtle()
            elif __ == '3':
                block.color("yellow")
                block.penup()
                block.hideturtle()
            elif __ == '4':
                block.color("red")
                block.penup()
                block.hideturtle()

            block.goto(collum, line)
            collum += 90
            if collum >= 720:
                collum = 0
                line += 90
    blocks.close()

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
