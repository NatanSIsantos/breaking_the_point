import turtle
import modules.targets
'''Este é o arquivo onde são configurados os objetos diretamente interagíveis
pelo player, como bola e raquete, além de suas colisões e parâmetros'''


def draw_objects():
    modules.targets.life()

    def pong_sound():
        pass

    screen = turtle.Screen()
    screen.title("breaking_the_point")
    screen.bgcolor("black")
    screen.setup(720, 720)
    screen.tracer(0)

    # desenhando a bola
    ball = turtle.Turtle("circle")
    ball.speed(0)
    ball.color("orange")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

    # variáveis utilizadas no player
    player_height = 1
    player_width = 5

    # parâmetros do p1ayer
    player1 = turtle.Turtle("square")
    player1.speed(0)
    player1.turtlesize(player_height, player_width)
    player1.color("gray")
    player1.penup()
    player1.sety(-330)

    # Variáveis de movimentação do player
    p_speed = 42

    # Movimentação do player

    def p_right():
        x = player1.xcor()
        x += p_speed
        player1.setx(x)

    def p_left():
        x = player1.xcor()
        x -= p_speed
        player1.setx(x)

    # Recebendo a entrada de movimentos dos pjs
    screen.onkeypress(p_right, 'd')
    screen.onkeypress(p_left, 'a')
    screen.listen()

    while True:

        # movimentação da bola
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # colisão da bola com parede superior
        if (ball.ycor() >= 360):
            ball.sety(360)
            ball.dy *= -1
            pong_sound()

        # colisão da bola com parede inferior
        if (ball.ycor() <= -360):
            ball.sety(-360)
            ball.dy *= -1
            pong_sound()

        # colisão da bola com parede direita
        if (ball.xcor() > 360):
            ball.setx(360)
            ball.dx *= -1
            pong_sound()

        # colisão da bola com parede esquerda
        if (ball.xcor() < -360):
            ball.setx(-360)
            ball.dx *= -1
            pong_sound()

        # colisão da bola com o player
        if (ball.ycor() < -330 and ball.ycor() < player1.xcor() - 65 and
                ball.xcor() > player1.xcor() - 65 and
                ball.ycor() > -331):
            ball.dy *= -1
            if (ball.dy > 0):
                ball.dy += 0.01
            elif (ball.dy < 0):
                ball.dy -= 0.01

            # divisão de setores
            if (ball.xcor() <= player1.xcor() + 5 and
                    ball.xcor() >= player1.xcor() - 5):
                if (ball.dx > 0):
                    ball.dx = ball.dy
                elif (ball.dx < 0):
                    ball.dx = -ball.dy

            elif (ball.xcor() > player1.xcor() + 5 and
                  ball.xcor() <= player1.xcor() + 20):
                if (ball.dx > 0):
                    ball.dx = ball.dy + 0.02
                elif (ball.dx < 0):
                    ball.dx = -ball.dy - 0.02

            elif (ball.xcor() < player1.xcor() - 5 and
                  ball.xcor() >= player1.xcor() - 20):
                if (ball.dx > 0):
                    ball.dx = ball.dy - 0.02
                elif (ball.dx < 0):
                    ball.dx = -ball.dy + 0.02

            elif (ball.ycor() > player1.ycor() + 20 and
                  ball.ycor() <= player1.ycor() + 35):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.03

            elif (ball.ycor() < player1.ycor() - 20 and
                  ball.ycor() >= player1.ycor() - 35):
                if (ball.dy > 0):
                    ball.dy = ball.dx - 0.03
                elif (ball.dy < 0):
                    ball.dy = -ball.dx + 0.03

            elif (ball.ycor() > player1.ycor() + 35 and
                  ball.ycor() <= player1.ycor() + 50):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.04

            elif (ball.ycor() < player1.ycor() - 35 and
                  ball.ycor() >= player1.ycor() - 50):
                if (ball.dy > 0):
                    ball.dy = ball.dx - 0.04
                elif (ball.dy < 0):
                    ball.dy = -ball.dx + 0.04

            elif (ball.ycor() > player1.ycor() + 50 and
                  ball.ycor() <= player1.ycor() + 65):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.05

            elif (ball.ycor() < player1.ycor() - 50 and
                  ball.ycor() >= player1.ycor() - 65):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.05
            pong_sound()

        # colisão do player com as paredes
        if (player1.xcor() > 360):
            player1.setx(360)
        if (player1.xcor() < -3680):
            player1.setx(-360)

        # atualização da tela
        screen.update()
