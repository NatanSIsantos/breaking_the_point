import turtle


def on_score():
    win_score = turtle.Screen()
    win_score.screensize(720,720)
    win_score.bgcolor("black")
    scorew = open("files/score.txt", "w")
    score = open("files/score.txt", "r")
    for _ in range(10):
        f = score.readline()
        if f == "":
            scorew.write("0\n")
    linhas = score.readlines()
    pontos = turtle.Turtle()
    pontos.shape("square")
    pontos._color("white")
    pontos.penup()
    
    j = 0
    for _ in linhas:
        j += 1
        pontos.goto(0, j*5)
        pontos.write(linhas[_], align="center", font=(
            "Press Start 2P", 18, "normal"))



