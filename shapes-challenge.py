from turtle import Turtle, Screen
import random

# Goal make the turtle draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon using a loop

# Make  new object named Billy using turtle.Turtle
billy = Turtle()

colors = ["LimeGreen", "Green", "ForestGreen", "DarkGreen", "GreenYellow00", "Chartreuse", 	"OliveDrab",
          "DarkKhaki", "Olive", "Beige", "DarkOliveGreen"]

# Sides of the triangle start.
num_sides = 3

def draw_shape(num_sides):
    """draw_shape takes the number of slides as input, 360 / num_sides to make the angle.
    num_sides is being replaced by the for shape_side_n variable in loop range """
    angle = 360 / num_sides
    for _ in range(num_sides):
        # loop through num_sides and draw the shapes
        billy.forward(100)
        # angle variable changes by the increase in num_sides caused by the for shape_side_n loop range
        billy.right(angle)


# This is a loop to start with triangle (3) and end with decagon (10+1)
# this shape_side_n is put in as draw_shape(input)
for shape_side_n in range(3, 11):
    billy.color(random.choice(colors))
    # range is 10 + 1 because it skips the last 11 not including 11.
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()


# ------wrong try-------
# triangle = 3 "-----I had better used a loop in range to 3-10 for the sides as shown above----"
# sides = 360 / triangle
# stop = False
#
# # Repeat the code 4 times to create a square. Use '_' for emoty variable
#
# -----Adding a new range input during a for loop didn't work -----
# for _ in range(triangle):
#     turt.forward(100)
#     turt.right(sides)
#     for _ in range(triangle + 1):
#         turt.forward(100)
#         turt.right(sides)
