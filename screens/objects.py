import turtle
import time
from random import randint

def draw_game_states():
    life = 3
    points = 0

    heart = turtle.Turtle()
    heart.speed(0)
    heart.shape("square")
    heart.color("red")
    heart.penup()
    heart.hideturtle()
    heart.goto(-480, 175)
    heart.write("{} ".format(life), align="left", font=(
        "Press Start 2P", 24, "italic"))

    score = turtle.Turtle()
    score.speed(0)
    score.shape("square")
    score.color("black")
    score.penup()
    score.hideturtle()
    score.goto(500,-280)
    score.write("0", align="right", font=(
        "Press Start 2P", 24, "bold"))
    return (life, points, score, heart)


def draw_ball():
    ball = turtle.Turtle("turtle")
    ball.speed(0)
    ball.color("#8bac0f")
    ball.left(270)
    ball.penup()
    ball.goto(0, 0)
    return ball


def draw_player():
    player1 = turtle.Turtle("square")
    player1.speed(0)
    player1.turtlesize(2, 5)
    player1.color("#9bbc0f")
    player1.penup()
    player1.sety(-330)
    return player1


def game_over():
    loser = turtle.Turtle()
    loser.shape("square")
    loser.shapesize(stretch_wid=10, stretch_len=5)
    loser.speed(0)
    loser.color("red")
    loser.penup()
    loser.hideturtle()
    loser.goto(120, -220)
    loser.fillcolor("black")

    loser.write(
        "SEE YOU,\n" +
        "SPACE TURTLE...\n" +
        "\n\nGAME OVER.", align="right", font=("Press Start 2P", 24, "bold"))
    loser.clear()
    time.sleep(3)
    turtle.Screen().clear()

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

def matrix_generator(collided, number):
    blocks = open('files/blocks_matrix.txt', 'w')
    blockr = open('files/blocks_matrix.txt')
    lin = 60  # núúmero de linhas
    col = 1  # núúmero de colunas

    if collided is True:
        linhas = [linhas.strip() for _ in blockr]  # cada linha é um elemento da lista linhas
        print(linhas)
        linhas[number] = '0\n'
        blocks.write(linhas[::])
    elif collided is False:
        for _ in range(lin):
            for _ in range(col):
                number = randint(0, 6)
                blocks.write(str(number))
            blocks.write('\n')
    blocks.close()
    blockr.close()


def block_printer(collided):
    line = 300
    collum = -330
    blocks = open('files/blocks_matrix.txt', 'r')
    collum_list = []
    lines_list = []
    counter_null = 0
    block_color = "#"

    for _ in blocks:
        block = turtle.Turtle()
        block.shape("square")
        if collided is True:
            block.clear()
        block.shapesize(1, 2)
        block._tracer(0)
        block.speed(0)
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
                block_color = "#"
                for _ in range(6):
                    block_color += str(randint(0, 9))
                block.color(block_color)
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '2':
                block_color = "#"
                for _ in range(6):
                    block_color += str(randint(0, 9))
                block.color(block_color)
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '3':
                block_color = "#"
                for _ in range(6):
                    block_color += str(randint(0, 9))
                block.color(block_color)
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '4':
                block_color = "#"
                for _ in range(6):
                    block_color += str(randint(0, 9))
                block.color(block_color)
                block.penup()
                lines_list.append(line)
                collum_list.append(collum)
            elif __ == '5':
                block_color = "#"
                for _ in range(6):
                    block_color += str(randint(0, 9))
                block.color(block_color)
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
