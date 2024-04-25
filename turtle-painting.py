import colorgram

# rgb_colors = []
# colors = colorgram.extract('images.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle as turtle_module
import random
# change color scheme
turtle_module.colormode(255)
billy = turtle_module.Turtle()
billy.speed("fastest")

# used the colorgram class to get 30 colors from images.jpeg file
color_list = [(212, 223, 213), (213, 221, 227), (228, 217, 221), (200, 166, 114), (216, 201, 141), (152, 81, 55), (27, 111, 141), (158, 55, 67), (194, 156, 30), (140, 180, 172), (134, 178, 189), (31, 52, 70), (58, 108, 77), (63, 45, 38), (136, 37, 48), (200, 142, 150), (37, 56, 43), (196, 82, 96), (190, 90, 78), (16, 96, 71), (173, 202, 194), (70, 166, 153), (220, 179, 171), (17, 90, 100), (58, 162, 176), (37, 62, 97), (73, 41, 47), (96, 50, 47), (167, 201, 208)]


# hide turtle from the beginning and keep pen up because no needed for the .dot attribute
billy.hideturtle()
billy.penup()
billy.setheading(225)
billy.forward(350)
billy.setheading(0)
number_of_dots = 100

# for a painting by 10 x 10 = 100 dots. So 100 + 1 for range
for dot_count in range(1, number_of_dots + 1):
    billy.dot(20, random.choice(color_list))
    billy.forward(50)

    # if every 10, 10, 30 etc. change heading of turtle. This if statement will run 10 times
    if dot_count % 10 == 0:
        billy.setheading(90)
        billy.forward(50)
        billy.setheading(180)
        billy.forward(500)
        billy.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
