"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.pensize(20)
tina.pencolor('green')
tina.forward(90)
tina.right(72)
tina.begin_fill()
tina.pencolor('green')
tina.forward(90)
tina.right(72)
tina.pencolor('green')
tina.forward(90)
tina.right(72)
tina.pencolor('green')
tina.forward(90)
tina.right(72)
tina.pencolor('green')
tina.forward(90)
tina.right(72)
tina.pencolor('green')
tina.forward(90)
tina.right(72)
tina.end_fill()
turtle.exitonclick()                    # Close the window when we click on it
