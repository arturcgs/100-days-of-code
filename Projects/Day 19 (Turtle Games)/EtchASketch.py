import turtle as t


def etchsketch():
    def home():
        timmy.penup()
        timmy.home()
        timmy.pendown()

    # creating turtle
    timmy = t.Turtle()
    timmy.speed(0)

    # creating screen
    screen = t.Screen()

    # keyboard commands
    screen.onkeypress(key='w', fun=lambda: timmy.forward(10))
    screen.onkeypress(key='s', fun=lambda: timmy.backward(10))
    screen.onkeypress(key='a', fun=lambda: timmy.left(10))
    screen.onkeypress(key='d', fun=lambda: timmy.right(10))
    screen.onkeypress(key='c', fun=lambda: timmy.clear())
    screen.onkeypress(key='h', fun=home)

    # screen rules
    screen.listen()
    screen.exitonclick()


if __name__ == '__main__':
    etchsketch()
