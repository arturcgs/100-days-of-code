from turtle import Turtle


def draw_background():
    # set up the pen
    pen = Turtle()
    pen.speed(0)
    pen.width(2)
    pen.hideturtle()

    # Border lines
    # fill options
    pen.fillcolor('gray')
    pen.begin_fill()
    # lower line
    pen.penup()
    pen.setposition(-300, -220)
    pen.pendown()
    pen.forward(600)
    # upper line
    pen.penup()
    pen.setposition(300, 220)
    pen.pendown()
    pen.backward(600)
    pen.setposition(-300, -220)
    # end fill
    pen.end_fill()

    # Dashed lines
    pen.color('yellow')
    pen.width(6)
    x = -300
    y = -170

    for _ in range(8):
        # set up line
        pen.penup()
        pen.setposition(x, y)
        pen.pendown()
        y += 50
        # draw dashed line
        for _ in range(50):
            pen.forward(30)
            pen.penup()
            pen.forward(30)
            pen.pendown()
