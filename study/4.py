import turtle


def coch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            coch(size / 3, n - 1)


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.bgcolor("white")
    turtle.pensize(2)
    turtle.goto(-200, 100)
    turtle.pendown()
    level = 3
    coch(400, level)
    turtle.right(120)
    coch(400, level)
    turtle.right(120)
    coch(400, level)
    turtle.hideturtle()
    turtle.done()


main()
