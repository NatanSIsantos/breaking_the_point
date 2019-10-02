import turtle
import time
import wave
import simpleaudio as sa
from random import randint
from modules import targets, screens, arts
'''Este é o arquivo onde são configurados os objetos diretamente interagíveis
pelo player, como bola e raquete, além de suas colisões e parâmetros'''

def draw_objects():
    life = 3

    heart = turtle.Turtle()
    heart.speed(0)
    heart.shape("square")
    heart.color("pink")
    heart.penup()
    heart.hideturtle()
    heart.goto(-300, 310)
    heart.write("3 lifes", align="left", font=(
        "Press Start 2P", 24, "normal"))

    def pong_sound():
        wave_obj = sa.WaveObject.from_wave_file("files/pong.wav")
        wave_obj.play()

    # tocando música
    music_obj = sa.WaveObject.from_wave_file("files/breaking_the_silence.wav")
    musica = music_obj.play()

    screen = turtle.Screen()
    screen.title("breaking_the_point")
    screen.bgcolor("MidnightBlue")
    screen.setup(720, 720)
    screen.tracer(0)

    # colocando estrelas de fundo
    arts.draw_backgroung()

    # desenhando a bola
    ball = turtle.Turtle("circle")
    ball.speed(0)
    ball.color("orange")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = -1
    ball.dy = -1

    # variáveis utilizadas no player
    player_height = 0.5
    player_width = 5

    # parâmetros do p1ayer
    player1 = turtle.Turtle("square")
    player1.speed(0)
    player1.turtlesize(player_height, player_width)
    player1.color("white")
    player1.penup()
    player1.sety(-330)

    # Variáveis de movimentação do player
    p_speed = 40

    # reiniciar o jogo
    def restart():
        player1.sety(-330)
        ball.goto(0, 0)
        ball.dy = -1
        heart.clear()
        global life
        life = 3
        heart.write("{} lifes".format(life), align="left", font=(
            "Press Start 2P", 24, "normal"))

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
    screen.onkeypress(restart, 'space')
    screen.listen()

    # desenhando blocos
    targets.matrix_generator()
    lines = list()
    collum = list()
    (lines, collum) = targets.block_printer()

    while True:
        if musica.is_playing() is False:
            musica = music_obj.play()

        # movimentação da bola
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # colisão da bola com blocos
        if (ball.ycor() >= 30):
            for _ in lines:
                if(ball.ycor() == _):
                    for __ in collum:
                        if (ball.xcor() <= __+5)or(ball.xcor() >= __-5):
                            ball.dy *= -1

        # colisão da bola com parede superior
        if (ball.ycor() >= 360):
            ball.sety(360)
            ball.dy *= -1
            pong_sound()

        # colisão da bola com parede inferior
        if (ball.ycor() <= -360):
            ball.sety(-45)
            ball.setx(0)
            life -= 1
            heart.clear()
            heart.write("{} lifes".format(life), align="left", font=(
                "Press Start 2P", 24, "normal"))
            if life == 0:
                targets.game_over()
                time.sleep(1)
                heart.clear()
                life = 3
                heart.write("{} lifes".format(life), align="left", font=(
                    "Press Start 2P", 24, "normal"))
                # screens.menu()
            else:
                targets.counter()
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
        if (ball.ycor() <= -320 and ball.xcor() <= player1.xcor() + 65 and
                ball.xcor() > player1.xcor() - 65 and
                ball.ycor() > -321):
            ball.dy *= -1

            # divisão de setores
            if (ball.ycor() <= player1.ycor() + 5 and
                    ball.ycor() >= player1.ycor() - 5):
                if (ball.dy > 0):
                    ball.dy = -ball.dy
                elif (ball.dy < 0):
                    ball.dy = -ball.dy

            elif (ball.ycor() > player1.ycor() + 5 and
                  ball.ycor() <= player1.ycor() + 20):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.08
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.08

            elif (ball.ycor() < player1.ycor() - 5 and
                  ball.ycor() >= player1.ycor() - 20):
                if (ball.dy > 0):
                    ball.dy = -ball.dx - 0.08
                elif (ball.dy < 0):
                    ball.dy = -ball.dx + 0.08

            elif (ball.xcor() > player1.xcor() + 20 and
                  ball.xcor() <= player1.xcor() + 35):
                if (ball.dx > 0):
                    ball.dx = -ball.dy + 0.12
                elif (ball.dx < 0):
                    ball.dx = -ball.dy - 0.12

            elif (ball.xcor() < player1.xcor() - 20 and
                  ball.xcor() >= player1.xcor() - 35):
                if (ball.dx > 0):
                    ball.dx = -ball.dy - 0.12
                elif (ball.dx < 0):
                    ball.dx = -ball.dy + 0.12

            elif (ball.xcor() > player1.xcor() + 35 and
                  ball.xcor() <= player1.xcor() + 50):
                if (ball.dx > 0):
                    ball.dx = ball.dy + 0.16
                elif (ball.dx < 0):
                    ball.dx = -ball.dy - 0.16

            elif (ball.xcor() < player1.xcor() - 35 and
                  ball.xcor() >= player1.xcor() - 50):
                if (ball.dx > 0):
                    ball.dx = ball.dy - 0.16
                elif (ball.dx < 0):
                    ball.dx = -ball.dy + 0.16

            elif (ball.xcor() > player1.xcor() + 50 and
                  ball.xcor() <= player1.xcor() + 65):
                if (ball.dx > 0):
                    ball.dx = ball.dy + 0.20
                elif (ball.dx < 0):
                    ball.dx = -ball.dy - 0.20

            elif (ball.xcor() < player1.xcor() - 50 and
                  ball.xcor() >= player1.xcor() - 65):
                if (ball.dx > 0):
                    ball.dx = ball.dy + 0.20
                elif (ball.dx < 0):
                    ball.dx = -ball.dy - 0.20
            pong_sound()

        # colisão da bola com os blocos

        # colisão do player com as paredes
        if (player1.xcor() > 300):
            player1.setx(300)
        if (player1.xcor() < -300):
            player1.setx(-300)

        # atualização da tela
        screen.update()
