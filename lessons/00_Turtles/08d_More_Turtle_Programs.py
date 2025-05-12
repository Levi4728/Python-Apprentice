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
t = turtle.Turtle()                  # Create a turtle named tina

t.shape('turtle')                    # Set the shape of the turtle to a turtle
t.speed(2)  
scr = turtle.Screen()
scr.setup(width=600, height=326)

def rt():
    t.right(15)
def lft():
    t.left(15)
def fd():
    t.forward(10) 
def bd():
    t.back(10)

scr.onkeypress(rt, "Right")
scr.onkeypress(lft, "Left")
scr.onkeypress(bd, "Down")
scr.onkeypress(fd, "Up")
scr.listen()
turtle.done()
