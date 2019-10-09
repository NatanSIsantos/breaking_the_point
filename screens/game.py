import turtle
from screens import objects
import menu


def on_game():
    game_win = turtle.Screen()
    game_win.screensize(1080, 720)
    game_win.bgpic("files/painel.png")
    ball = objects.draw_ball()
    ball.dx = -1.0
    ball.dy = -1.0
    player = objects.draw_player()
    (life, points, score, heart) = objects.draw_game_states()

    # Recebendo a entrada de movimentos dos pjs
    p_speed = 10

    def p_right():
        x = player.xcor()
        x += p_speed
        player.setx(x)

    def p_left():
        x = player.xcor()
        x -= p_speed
        player.setx(x)

    game_win.onkeypress(p_right, 'd')
    game_win.onkeypress(p_left, 'a')
    # game_win.onkeypress(restart, 'space')
    game_win.listen()

    collided = False
    # desenhando blocos
    objects.matrix_generator(collided, -1)
    nulls = 0
    lines = list()
    collum = list()
    (lines, collum, nulls) = objects.block_printer(collided)

    while True:
        collided = False
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)

        # colisão da bola com parede superior
        if (ball.ycor() > 350):
            ball.sety(350)
            ball.dy *= -1
            ball.left(180)
            # pong_sound()

        # colisão da bola com parede inferior
        if (ball.ycor() <= -360):
            ball.sety(-45)
            ball.setx(0)
            life -= 1
            heart.clear()
            heart.write("{} ".format(life), align="left", font=(
                "Press Start 2P", 24, "italic"))
            if life == 0:
                objects.game_over()
                life = 3
                menu.menu()
            else:
                objects.counter()
                # pong_sound()

        # colisão da bola com parede direita
        if (ball.xcor() > 350):
            ball.setx(350)
            ball.dx *= -1
            # pong_sound()

        # colisão da bola com parede esquerda
        if (ball.xcor() < -350):
            ball.setx(-350)
            ball.dx *= -1
            # pong_sound()

        # colisão da bola com o player
        if (ball.ycor() <= -310 and ball.xcor() < player.xcor() - 48.75 and
                ball.xcor() >= player.xcor() - 65 and
                ball.ycor() > -322):
            ball.dx = -1
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() > player.xcor() + 48.75 and
                ball.xcor() <= player.xcor() + 65 and
                ball.ycor() > -322):
            ball.dx = 1
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() < player.xcor() - 32.5 and
                ball.xcor() >= player.xcor() - 48.75 and
                ball.ycor() > -322):
            ball.dx = -0.75
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() > player.xcor() + 32.5 and
                ball.xcor() <= player.xcor() + 48.75 and
                ball.ycor() > -322):
            ball.dx = 0.75
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() < player.xcor() - 16.25 and
                ball.xcor() >= player.xcor() - 32.5 and
                ball.ycor() > -322):
            ball.dx = -0.5
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() > player.xcor() + 16.25 and
                ball.xcor() <= player.xcor() + 32.5 and
                ball.ycor() > -322):
            ball.dx = 0.5
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() < player.xcor() and
                ball.xcor() >= player.xcor() - 16.25 and
                ball.ycor() > -322):
            ball.dx = -0.25
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() > player.xcor() and
                ball.xcor() <= player.xcor() + 16.25 and
                ball.ycor() > -322):
            ball.dx = 0.25
            ball.dy *= -1
            ball.left(180)
            # pong_sound()
        elif (ball.ycor() <= -310 and ball.xcor() == player.xcor() and
                ball.ycor() > -322):
            ball.dx = 0
            ball.dy *= -1
            ball.left(180)
            # pong_sound()

        # colisão da bola com os blocos
        if (ball.ycor() >= 0):
            j = 0
            while j < (60-nulls):
                if(lines[j] >= ball.ycor() - 7) and (lines[j] <= ball.ycor() + 7):
                    if(collum[j] >= ball.xcor() - 15) and (collum[j] <= (
                            ball.xcor() + 15)):
                        points += 20
                        score.clear()
                        score.write("{} ".format(points), align="right", font=(
                            "Press Start 2P", 24, "bold"))
                        if (ball.dy > 0):
                            ball.sety(ball.ycor()-7)
                        else:
                            ball.sety(ball.ycor()+7)
                        ball.dy *= -1
                        ball.left(180)
                        ball.dy *= 1.01
                        ball.dx *= 1.01
                        # pong_sound()
                        '''collided = True
                        objects.matrix_generator(collided, j)
                        (lines, collum, nulls) = objects.block_printer(collided)'''
                j += 1

        if (player.xcor() >= 300):
            player.setx(300)
        if (player.xcor() <= -300):
            player.setx(-300)

        game_win.update()
