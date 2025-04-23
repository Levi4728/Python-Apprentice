
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(6)                           # Make the turtle move as fast, but not too fast. 

#for i in range(4):
    #tina.backward(150)
    #tina.left(90)
#for i in range(90):
#   tina.forward(i*3)
   # tina.left(i)
for i in range(10):
    tina.begin_fill()
    tina.penup()
    tina.goto(0,i+30)
    tina.pendown()
    tina.circle(40)
    tina.pensize(10)
    tina.pencolor('red')
    tina.fillcolor('green')
    tina.end_fill()
tina.penup()
tina.goto(40,100)
tina.pendown()
tina.circle(20)
turtle.exitonclick()                    # Close the window when we click on it
