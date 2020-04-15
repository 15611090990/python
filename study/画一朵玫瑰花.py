import turtle
import time

turtle.setup(1000, 800, 0, 0)
turtle.speed(0)
turtle.penup()
turtle.seth(90)
turtle.fd(340)
turtle.seth(0)
turtle.pendown()

turtle.speed(5)
turtle.begin_fill()
turtle.fillcolor('red')
turtle.circle(50, 30)

for i in range(10):
    turtle.fd(1)
    turtle.left(10)

turtle.circle(40, 40)

for i in range(6):
    turtle.fd(1)
    turtle.left(3)

turtle.circle(80, 40)

for i in range(20):
    turtle.fd(0.5)
    turtle.left(5)

turtle.circle(80, 45)

for i in range(10):
    turtle.fd(2)
    turtle.left(1)

turtle.circle(80, 25)

for i in range(20):
    turtle.fd(1)
    turtle.left(4)

turtle.circle(50, 50)

time.sleep(0.1)

turtle.circle(120, 55)

turtle.speed(0)

turtle.seth(-90)
turtle.fd(70)

turtle.right(150)
turtle.fd(20)

turtle.left(140)
turtle.circle(140, 90)

turtle.left(30)
turtle.circle(160, 100)

turtle.left(130)
turtle.fd(25)

turtle.penup()
turtle.right(150)
turtle.circle(40, 80)
turtle.pendown()

turtle.left(115)
turtle.fd(60)

turtle.penup()
turtle.left(180)
turtle.fd(60)
turtle.pendown()

turtle.end_fill()

turtle.right(120)
turtle.circle(-50, 50)
turtle.circle(-20, 90)

turtle.speed(1)
turtle.fd(75)

turtle.speed(0)
turtle.circle(90, 110)

turtle.penup()
turtle.left(162)
turtle.fd(185)
turtle.left(170)
turtle.pendown()
turtle.circle(200, 10)
turtle.circle(100, 40)
turtle.circle(-52, 115)
turtle.left(20)
turtle.circle(100, 20)
turtle.circle(300, 20)
turtle.speed(1)
turtle.fd(250)

turtle.penup()
turtle.speed(0)
turtle.left(180)
turtle.fd(250)
turtle.circle(-300, 7)
turtle.right(80)
turtle.circle(200, 5)
turtle.pendown()

turtle.left(60)
turtle.begin_fill()
turtle.fillcolor('green')
turtle.circle(-80, 100)
turtle.right(90)
turtle.fd(10)
turtle.left(20)
turtle.circle(-63, 127)
turtle.end_fill()

turtle.penup()
turtle.left(50)
turtle.fd(20)
turtle.left(180)

turtle.pendown()
turtle.circle(200, 25)

turtle.penup()
turtle.right(150)

turtle.fd(180)

turtle.right(40)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('green')
turtle.circle(-100, 80)
turtle.right(150)
turtle.fd(10)
turtle.left(60)
turtle.circle(-80, 98)
turtle.end_fill()

turtle.penup()
turtle.left(60)
turtle.fd(13)
turtle.left(180)

turtle.pendown()
turtle.speed(1)
turtle.circle(-200, 23)

turtle.exitonclick()
