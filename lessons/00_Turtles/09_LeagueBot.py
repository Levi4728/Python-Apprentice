""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle
import random

# Set up the screen
scr = turtle.Screen()
scr.setup(width=6000, height=6000)
scr.bgcolor('white')

# Create Tina the Turtle
tina = turtle.Turtle()
tina.speed(0)

# Define possible values
angles = [30, 45, 60, 90, 120, 135, 150]
distances = [10, 20, 30, 40, 50, 60, 70]
directions = ["right", "left"]
colors = ['green', 'black', 'red', 'blue', 'pink', 'orange', 'indigo', 'violet']

# Define the path function
def path_long(steps):
    for _ in range(steps):
        angle = random.choice(angles)
        distance = random.choice(distances)
        direction = random.choice(directions)
        color = random.choice(colors)

        tina.color(color)
        tina.forward(distance)

        if direction == "right":
            tina.right(angle)
        else:
            tina.left(angle)

# Call the function
path_long(50)  # Do 50 random steps

turtle.done()
