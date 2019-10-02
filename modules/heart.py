import turtle


def create_screen():  # função que cria a tela
    screen = turtle.Screen()
    screen.title("Breaking the Point")
    screen.bgcolor("black")
    screen.setup(720, 720)
    screen.tracer(0)
    desenho(0, 0)
    desenho(4, 4)
    desenho(-4, 4)
    desenho(8, 8)
    desenho(-8, 8)
    desenho(12, 12)
    desenho(-12, 12)
    desenho(8, 16)
    desenho(-8, 16)
    desenho(0, 12)

    while True:
        screen.update()


def desenho(x, y):
    size = 1.2
    selection = turtle.Turtle("square")
    selection.speed(0)
    selection.turtlesize(size*0.4, size*0.4)
    selection.color('pink')
    selection.penup()
    selection.sety(size*y)
    selection.setx(size*x)


create_screen()
