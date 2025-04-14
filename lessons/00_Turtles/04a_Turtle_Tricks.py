"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(1)
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

                   # Close the window when we click on it
tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 100)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a Triangle

tina.pencolor('black')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(120)                          # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continuie the last two steps three more times
tina.right(120)                           # to draw a square

tina.pencolor('blue')
tina.forward(200)
tina.left(120)

turtle.exitonclick() 