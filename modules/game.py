import turtle
import time
import wave
import simpleaudio as sa
from random import randint
from modules import targets, screens
'''Este é o arquivo onde são configurados os objetos diretamente interagíveis
pelo player, como bola e raquete, além de suas colisões e parâmetros'''

def draw_objects():
    life = 3

    heart = turtle.Turtle()
    heart.speed(0)
    heart.shape("square")
    heart.color("red")
    heart.penup()
    heart.hideturtle()
    heart.goto(-480, 175)
    heart.write("3 ", align="left", font=(
        "Press Start 2P", 24, "italic"))

    def pong_sound():
        wave_obj = sa.WaveObject.from_wave_file("files/pong.wav")
        wave_obj.play()

    # tocando música
    music_obj = sa.WaveObject.from_wave_file("files/breaking_the_silence.wav")
    musica = music_obj.play()

    screen = turtle.Screen()
    screen.title("breaking_the_point")
    screen.bgpic("files/painel.png")
    screen.setup(1080, 720)
    screen.tracer(0)

    # desenhando a bola
    ball = turtle.Turtle("turtle")
    ball.speed(0)
    ball.color("#8bac0f")
    ball.left(270)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = -1
    ball.dy = -1

    # variáveis utilizadas no player
    player_height = 1
    player_width = 5

    # parâmetros do p1ayer
    player1 = turtle.Turtle("square")
    player1.speed(0)
    player1.turtlesize(player_height, player_width)
    player1.color("#9bbc0f")
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
        heart.write("{} ".format(life), align="left", font=(
            "Press Start 2P", 24, "italic"))

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
    nulls = 0
    lines = list()
    collum = list()
    (lines, collum, nulls) = targets.block_printer()
    print(collum)
    print(lines)
    print(nulls)
    while True:
        if musica.is_playing() is False:
            musica = music_obj.play()

        # movimentação da bola
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # colisão da bola com parede superior
        if (ball.ycor() >= 360):
            ball.sety(360)
            ball.dy *= -1
            ball.left(180)
            pong_sound()

        # colisão da bola com parede inferior
        if (ball.ycor() <= -360):
            ball.sety(-45)
            ball.setx(0)
            life -= 1
            heart.clear()
            heart.write("{} ".format(life), align="left", font=(
                "Press Start 2P", 24, "italic"))
            if life == 0:
                targets.game_over()
                heart.clear()
                life = 3
                screens.create_screen()
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
        if (ball.ycor() <= -318 and ball.xcor() <= player1.xcor() + 65 and
                ball.xcor() >= player1.xcor() - 65 and
                ball.ycor() > -322):
            ball.dy *= -1
            ball.left(180)
            pong_sound()

        # colisão da bola com os blocos
        if (ball.ycor() >= 0):
            j = 0
            while j < (60-nulls):
                if(lines[j] >= ball.ycor() - 7) and (lines[j] <= ball.ycor() + 7):
                    if(collum [j] >= ball.xcor() -15) and (collum [j] <= (
                        ball.xcor() + 15)):
                        if (ball.dy > 0):
                            ball.sety(ball.ycor()-7)
                        else:
                            ball.sety(ball.ycor()+7)
                        ball.dy *= -1
                        ball.left(180)
                        ball.dy *= 1.01
                        ball.dx *= 1.01
                        pong_sound()
                j += 1


        # colisão do player com as paredes
        if (player1.xcor() > 300):
            player1.setx(300)
        if (player1.xcor() < -300):
            player1.setx(-300)

        # atualização da tela
        screen.update()
