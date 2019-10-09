import turtle
from screens import game, options, score


def menu():
    def selection_sound():
        pass

    menu_win = turtle.Screen()
    menu_win.title("The Space Turtles")
    menu_win.bgpic("files/spc_turt.png")
    menu_win.setup(600, 600)
    menu_win.tracer(0)

    # Menu
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
        selection_sound()

    def selection_down():
        if selection.ycor() <= -55:
            selection.sety(65)
        selection.sety(selection.ycor() - 40)
        selection_sound()

    def selection_mode():
        if (selection.ycor() == 25):
            menu_win.clear()
            menu_win.setup(1080, 720)
            game.on_game()
            menu_win.bye()

        if (selection.ycor() == -15):
            menu_win.clear()
            score.on_score()

        if (selection.ycor() == -55):
            menu_win.clear()
            options.on_options()

    # Esperando que o usuário aperte uma tecla
    menu_win.onkeypress(selection_mode, 'Return')
    menu_win.onkeypress(selection_up, 'Up')
    menu_win.onkeypress(selection_down, 'Down')
    menu_win.listen()

    while True:
        menu_win.update()
