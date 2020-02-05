# keyboard version

import turtle
from math import *
from vector_class import Vector
import time


screen = turtle.Screen()
screen.title("Squares")
screen.screensize(4500, 600)
screen.bgcolor("black")
screen.tracer(0)

# [15, 16, 18, 20, 24, 30, 32, 36, 40, 45, 48, 60, 72, 80, 90, 96, 120, 144, 160, 180, 240, 288, 360, 480, 720, 1440]

dimension = 2880
factor = 36



# number line
line = turtle.Turtle()
line.speed(0)
line.color("white")
line.penup()
line.goto(-dimension, -200)
line.pendown()
line.forward(dimension*2)


line2= turtle.Turtle()
line2.penup()
line2.speed(0)
line2.color("green")
line2.shape("square")
line2.shapesize(4, 0.01)
line2.penup()
# line2.goto(0, -1000)
line2.goto(factor, -200)
line2.pendown()
line2.dx = 0

dot = turtle.Turtle()
dot.penup()
dot.speed(0)
dot.color("green")
dot.shape("circle")
dot.shapesize(0.23)
dot.penup()
# line2.goto(0, -1000)
dot.goto(factor, -200)
dot.pendown()
dot.penup()
dot.dx = 0


a = turtle.Turtle()
a.penup()
a.hideturtle()
a.goto(line2.xcor() - 15, line2.ycor() + 50)
a.hideturtle()
a.color("green")
a.write("{0:.2f}".format(line2.xcor()/factor), False, "left", ("Ariel", 14, "normal"))


# create number positions

sl = turtle.Turtle()
sl.hideturtle()
sl.speed(0)
sl.color("white")


# power vectors
powVec = turtle.Turtle()
# powVec.hideturtle()
powVec.speed(0)
powVec.color("red")
powVec.penup()
powVec.goto(0, -200)


powVec2 = turtle.Turtle()
powVec2.hideturtle()
powVec2.speed(0)
powVec2.color("red")
powVec2.penup()
powVec2.goto(powVec.xcor(), -200)


powVec3 = turtle.Turtle()
powVec3.hideturtle()
powVec3.speed(0)
powVec3.color("red")
powVec3.penup()
powVec3.goto(powVec2.xcor(), -200)


powVec4 = turtle.Turtle()
powVec4.hideturtle()
powVec4.speed(0)
powVec4.color("red")
powVec4.turtlesize(1.3)
powVec4.penup()
powVec4.goto(powVec3.xcor(), -200)



def create_line(x, y):
    sl.penup()
    sl.goto(x, y - 5)
    sl.pendown()
    sl.goto(x, y + 5)
    sl.penup()


num_list = [x for x in range(-dimension, dimension+1, factor)]

for pow, num in enumerate(num_list):
    create_line(num, -200)
    if num == 0:
        sl.write('{0}'.format(int(num / factor)), font=('ariel', 18, 'normal'))
    else:
        sl.write('{0}'.format(int(num / factor)), font=('ariel', 12, 'normal'))

def powers(x):
    x = x/factor
    check = x
    for n in range(4):
        yield check
        check *= check


line2.dx = factor/100


def moveR():
    a.clear()
    line2.setx(line2.xcor() + line2.dx)
    a.goto(line2.xcor() - 15, line2.ycor() + 50)
    a.write("{0:.2f}".format(line2.xcor() / factor), False, "left", ("Ariel", 14, "normal"))


def moveL():
    a.clear()
    line2.setx(line2.xcor() - line2.dx)
    a.goto(line2.xcor() - 15, line2.ycor() + 50)
    a.write("{0:.2f}".format(line2.xcor() / factor), False, "left", ("Ariel", 14, "normal"))


def moveRbig():
    a.clear()
    line2.setx(line2.xcor() + line2.dx*factor)
    a.goto(line2.xcor() - 15, line2.ycor() + 50)
    a.write("{0:.2f}".format(line2.xcor() / factor), False, "left", ("Ariel", 14, "normal"))


def moveLbig():
    a.clear()
    line2.setx(line2.xcor() - line2.dx*factor)
    a.goto(line2.xcor() - 15, line2.ycor() + 50)
    a.write("{0:.2f}".format(line2.xcor() / factor), False, "left", ("Ariel", 14, "normal"))


def moveRsmall():
    a.clear()
    line2.setx(line2.xcor() + 5*line2.dx)
    a.goto(line2.xcor() - 15, line2.ycor() + 50)
    a.write("{0:.2f}".format(line2.xcor() / factor), False, "left", ("Ariel", 14, "normal"))


def moveLsmall():
    a.clear()
    line2.setx(line2.xcor() - 5*line2.dx)
    a.goto(line2.xcor() - 15, line2.ycor() + 50)
    a.write("{0:.2f}".format(line2.xcor() / factor), False, "left", ("Ariel", 14, "normal"))



screen.listen()
screen.onkeypress(moveR, 'Right')
screen.onkeypress(moveL, 'Left')
screen.onkeypress(moveRbig, 'd')
screen.onkeypress(moveLbig, 'a')
screen.onkeypress(moveRsmall, '.')
screen.onkeypress(moveLsmall, ',')

is_new_click = False
def show_powVec():
    global powVec
    x = line2.xcor()
    powVec.clear()
    powVec2.clear()
    powVec3.clear()
    powVec4.clear()
    pow_list = [xPow for xPow in powers(x)]
    if abs(x) >= factor:
        # for xPow in pow_list[0:2]:
        powVec.showturtle()
        powVec.turtlesize(0.95)
        powVec.goto(x, -200)
        powVec.setheading(0)
        powVec.pendown()
        powVec.goto(((x/factor)**2)*factor, -200)

        powVec2.showturtle()
        powVec2.turtlesize(1.1)
        powVec2.goto(x, -200)
        powVec2.setheading(0)
        powVec2.pendown()
        powVec2.goto(((x / factor) ** 4) * factor, -200)

        powVec3.showturtle()
        powVec3.turtlesize(1.2)
        powVec3.goto(x, -200)
        powVec3.setheading(0)
        powVec3.pendown()
        powVec3.goto(((x / factor) ** 8) * factor, -200)

        powVec4.showturtle()
        powVec4.turtlesize(1.3)
        powVec4.goto(x, -200)
        powVec4.setheading(0)
        powVec4.pendown()
        powVec4.goto(((x / factor) ** 16) * factor, -200)
    elif abs(x) < factor:

        powVec.showturtle()
        powVec.goto(x, -200)
        powVec.setheading(180)
        powVec.pendown()
        powVec.turtlesize(0.65)
        powVec.goto(((x/factor)**2)*factor, -200)

        powVec2.showturtle()
        powVec2.goto(x, -200)
        powVec2.setheading(180)
        powVec2.pendown()
        powVec2.turtlesize(0.7)
        powVec2.goto(((x / factor) ** 4) * factor, -200)

        powVec3.showturtle()
        powVec3.goto(x, -200)
        powVec3.setheading(180)
        powVec3.pendown()
        powVec3.turtlesize(0.75)
        powVec3.goto(((x / factor) ** 8) * factor, -200)

        powVec4.showturtle()
        powVec4.goto(x, -200)
        powVec4.setheading(180)
        powVec4.pendown()
        powVec4.turtlesize(0.8)
        powVec4.goto(((x / factor) ** 16) * factor, -200)
    # is_new_click = False





while True:
    screen.update()
    dot.goto(line2.pos())
    line2.penup()
    show_powVec()



# mouse version


# import turtle
# from math import sqrt
# from vector_class import Vector
# import time
#
#
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.tracer(0)
#
#
#
# # number line
# line = turtle.Turtle()
# line.speed(0)
# line.color("white")
# line.penup()
# line.goto(-720, -200)
# line.pendown()
# line.forward(1440)
#
#
# # create number positions
#
# sl = turtle.Turtle()
# sl.hideturtle()
# sl.speed(0)
# sl.color("white")
#
#
# # power vectors
#
# def create_line(x, y):
#     sl.penup()
#     sl.goto(x, y - 5)
#     sl.pendown()
#     sl.goto(x, y + 5)
#     sl.penup()
#
#
# factor = 50
# num_list = [x for x in range(-1000, 1001, factor)]
#
# for pow, num in enumerate(num_list):
#     create_line(num, -200)
#     if num == 0:
#         sl.write('{0}'.format(num / factor), font=('ariel', 10, 'normal'))
#     else:
#         sl.write('{0}'.format(num / factor), font=('ariel', 7, 'normal'))
#
#
# def create_powvec(x):
#     powVec = turtle.Turtle()
#     powVec.speed(0)
#     powVec.color("red")
#     powVec.turtlesize(1.5)
#     powVec.penup()
#     powVec.goto(x, -200)
#     return powVec
#
#
# def powers(x):
#     x = x/factor
#     check = x
#     for n in range(4):
#         yield check
#         check *= check
#
#
# pow_list = []
#
#
# def show_powVec(x, y):
#     global pow_list
#     pow_list = [xPow for xPow in powers(x)]
#     if abs(x) > factor:
#         for xPow in pow_list:
#             powVec = create_powvec(x)
#             powVec.pendown()
#             powVec.goto(xPow*factor, -200)
#     elif abs(x) <= factor:
#         for xPow in pow_list:
#             powVec = create_powvec(x)
#             powVec.pendown()
#             powVec.turtlesize(0.7)
#             powVec.setheading(180)
#             powVec.goto(xPow*factor, -200)
#
#     return powVec
#
#
# vec = show_powVec
#
# def show_powVec2(x):
#     # global factor
#      # x *= factor
#     pow_list = [xPow for xPow in powers(x)]
#     if abs(x) > factor:
#         for xPow in pow_list:
#             powVec = create_powvec(x)
#             powVec.pendown()
#             powVec.goto(xPow*factor, -200)
#     elif abs(x) <= factor:
#         for xPow in pow_list:
#             powVec = create_powvec(x)
#             powVec.pendown()
#             powVec.turtlesize(0.7)
#             powVec.setheading(180)
#             powVec.goto(xPow*factor, -200)
#
#     return powVec
#
#
#
# while True:
#     screen.update()
#     screen.onclick(show_powVec)
#     # show_powVec(200)
