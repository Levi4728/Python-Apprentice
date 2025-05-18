"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""

import turtle
import math
t = turtle.Turtle()                  # Create a turtle named tina

t.shape('turtle')                    # Set the shape of the turtle to a turtle
t.speed(2)  
scr = turtle.Screen()
scr.setup(width=600, height=600)

def rt():
    t.right(30)
def lft():
    t.left(30)
def fd():
    t.forward(10) 
def bd():
    t.back(10)
def orange():
    t.pencolor('orange')
def blue():
    t.pencolor('blue')
def green():
    t.pencolor('green')
#def black():
    #t.pencolor('black')
def purple():
    t.pencolor('purple')
def pen_on():
    t.pendown()
def pen_off():
    t.penup()
def red():
    t.pencolor('red')
scr.onkeypress(red, "r")
scr.onkeypress(pen_on, "-")
scr.onkeypress(pen_off, "0")
scr.onkeypress(blue, "b")
scr.onkeypress(green, "g")
#scr.onkeypress(black, "b")
scr.onkeypress(purple, "p")
scr.onkeypress(orange, "o")
scr.onkeypress(rt, "Right")
scr.onkeypress(lft, "Left")
scr.onkeypress(bd, "Down")
scr.onkeypress(fd, "Up")


import math

t = turtle.Turtle()
t.shape('turtle')
t.speed(2)

scr = turtle.Screen()
scr.setup(width=600, height=600)

# Ask the user for input
points = int(input("How many points should the star have? "))
outer = int(input("Length of outer spikes? "))
inner = int(input("Length of inner spikes? "))

# Define the drawing function
def draw_star(points, outer_size, inner_size):
    angle = 360 / (points * 2)
    for i in range(points * 2):
        if i % 2 == 0:
            t.forward(outer_size)
        else:
            t.forward(inner_size)
        t.right(angle)

# 🟢 Actually call the function to draw the star!
draw_star(points, outer, inner)

turtle.done()


scr.listen()
turtle.done()
