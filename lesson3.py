import turtle
import sys

jimmy = turtle.Turtle()

# #draw a circle
def circle(size, color):
    jimmy.fillcolor(color)
    jimmy.begin_fill()
    jimmy.circle(size)
    jimmy.end_fill()

# #draw a triangle
def triangle(size, color):
    jimmy.fillcolor(color)
    jimmy.begin_fill()
    x = 0
    while x < 3:
        jimmy.forward(size)
        jimmy.left(120)
        x += 1
    jimmy.end_fill()
# draw a star
def star(size, color):
    jimmy.fillcolor(color)
    jimmy.begin_fill()
    x = 0
    while x < 5:
        jimmy.forward(size)
        jimmy.right(144)
        jimmy.forward(size)
        x += 1
    jimmy.end_fill()
# get the users choice for shape and color
# call the appropriate function with the correct patterns

shape = raw_input("What shape? >>")
color = raw_input("What color? >>")
size = raw_input("what size? >>")

if shape == "circle":
    circle(int(size), color)
if shape == "triangle":
    triangle(int(size), color)
if shape == "star":
    star(int(size), color)

turtle.done()
