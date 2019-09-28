import turtle
'''Este é o arquivo onde são feitas as configurações envolvendo as transições
de telas, navegação de menu e derivados'''

screen = turtle.Screen()


def create_screen():  # função que cria a tela
    screen = turtle.Screen()
    screen.title("Breaking the Point")
    screen.bgcolor("black")
    screen.setup(720, 1080)
    screen.tracer(0)
    menu()
    while True:
        screen.update()


def menu():

    # Parâmetros da seleção
    selection = turtle.Turtle("square")
    selection.speed(0)
    selection.turtlesize(1.5, 6)
    selection.color('pink')
    selection.fillcolor('')
    selection.penup()
    selection.sety(25)

    # Configurando seleção por teclado
    def selection_up():
        selection.sety(25)
        # selection_sound()

    def selection_down():
        selection.sety(-15)
        # selection_sound()

    def selection_mode():
        if (selection.ycor() == 25):
            screen.clear()
            # Aqui colocaremos a tela para qual ele vai ex: Tela()

        if (selection.ycor() == -15):
            screen.clear()
            # Aqui colocaremos a tela para qual ele vai ex: Tela()

    # Esperando que o usuário aperte uma tecla
    screen.onkeypress(selection_mode, 'Return')
    screen.onkeypress(selection_up, 'Up')
    screen.onkeypress(selection_down, 'Down')
    screen.listen()

    # Título do jogo
    game_title = turtle.Turtle("square")
    game_title.speed(0)
    game_title.color("white")
    game_title.penup()
    game_title.hideturtle()
    game_title.goto(0, 180)
    game_title.write(
        "BREAKING\n" +
        "     THE\n" +
        " >POINT<\n", align="center", font=("Press Start 2P", 24, "normal"))

    # Tela de seleção
    mode = turtle.Turtle("square")
    mode.speed(0)
    mode.color("white")
    mode.penup()
    mode.hideturtle()
    mode.goto(0, 50)
    mode.write("Opções", align="center", font=(
        "Press Start 2P", 8, "normal"))

    mode = turtle.Turtle("square")
    mode.speed(0)
    mode.color("gray")
    mode.penup()
    mode.hideturtle()
    mode.goto(0, 10)
    mode.write("JOGAR", align="center", font=(
        "Press Start 2P", 16, "normal"))

    mode = turtle.Turtle("square")
    mode.speed(0)
    mode.color("gray")
    mode.penup()
    mode.hideturtle()
    mode.goto(0, -30)
    mode.write("PLACAR", align="center", font=(
        "Press Start 2P", 16, "normal"))
