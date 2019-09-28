import turtle
'''Este é o arquivo onde são configurados os objetos diretamente interagíveis
pelo player, como bola e raquete, além de suas colisões e parâmetros'''

screen = turtle.Screen()


def draw_objects():
    screen.bgcolor('black')
    player_height = 1
    player_width = 5

    # parâmetros do p1
    player1 = turtle.Turtle("square")
    player1.speed(0)
    player1.turtlesize(player_height, player_width)
    player1.color("cyan")
    player1.penup()
    player1.sety(-350)

    # desenhando a bola
    ball = turtle.Turtle("circle")
    ball.speed(0)
    ball.color("orange")
    ball.penup()
    ball.goto(0, 0)
