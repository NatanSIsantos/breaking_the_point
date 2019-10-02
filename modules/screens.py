import turtle
from modules import game, score
'''Este é o arquivo onde são feitas as configurações envolvendo as transições
de telas, navegação de menu e derivados'''

screen = turtle.Screen()

def create_screen():  # função que cria a tela
    screen = turtle.Screen()
    screen.title("ST - Breaking the Point")
    screen.bgpic("files/spc_turt.png")
    screen.setup(600, 600)
    screen.tracer(0)
    menu()
    while True:
        screen.update()


def on_game():  # tela chamada quando usuário escolher jogar
    game.draw_objects()


def on_score():  # tela chamada quando usuário escolher ver placar
    score.show_score()


def menu():  # função que cria o menu principal

    # Tela de seleção

    mode = turtle.Turtle("square")
    mode.speed(0)
    mode.color("white")
    mode.penup()
    mode.hideturtle()
    mode.goto(0, 10)
    mode.write("JOGAR", align="center", font=(
        "Press Start 2P", 18, "bold"))

    mode = turtle.Turtle("square")
    mode.speed(0)
    mode.color("white")
    mode.penup()
    mode.hideturtle()
    mode.goto(0, -30)
    mode.write("PLACAR", align="center", font=(
        "Press Start 2P", 18, "bold"))

    mode = turtle.Turtle("square")
    mode.speed(0)
    mode.color("white")
    mode.penup()
    mode.hideturtle()
    mode.goto(0, -70)
    mode.write("OPÇÕES", align="center", font=(
        "Press Start 2P", 18, "bold"))


    # Parâmetros da seleção
    selection = turtle.Turtle("square")
    selection.speed(0)
    selection.turtlesize(1.5, 6)
    selection.color('#9bbc0f')
    selection.fillcolor('')
    selection.penup()
    selection.sety(25)

    # Configurando seleção por teclado
    def selection_up():
        if selection.ycor() >= 25:
            selection.sety(-95)
        selection.sety(selection.ycor() + 40)
        # selection_sound()

    def selection_down():
        if selection.ycor() <= -55:
            selection.sety(65)
        selection.sety(selection.ycor() - 40)
        # selection_sound()

    def selection_mode():
        if (selection.ycor() == 25):
            screen.clear()
            on_game()

        if (selection.ycor() == -15):
            screen.clear()
            on_score()

        if (selection.ycor() == -55):
            screen.clear()

    # Esperando que o usuário aperte uma tecla
    screen.onkeypress(selection_mode, 'Return')
    screen.onkeypress(selection_up, 'Up')
    screen.onkeypress(selection_down, 'Down')
    screen.listen()
