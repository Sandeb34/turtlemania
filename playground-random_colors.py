from turtle import Turtle, Screen
import random
# turd = Turtle()

screen = Screen()
screen.colormode()
# add screen attribute to enable RGB hex triplet color coding.
screen.colormode(255)
# the color code it accepts is until 255 from each RGB hex triplet category.
screen.colormode()

random_color_list = []
def random_color_generator():
    """generator random color and adds them to a list fill in how many colors you want at range"""
    for _ in range(4):
        # creates a random number for Green(g) Blue(b) and Red(r)
        # and makes a new color with three numerical numbers RGB hex triplet.
        list_r = random.randint(0, 255)
        list_b = random.randint(0, 255)
        list_g = random.randint(0, 255)
        new_color = list_r, list_b, list_g
        random_color_list.append(new_color)


random_color_generator()\

print(random_color_list)


def change_color_every_line():
    """changes color every line drawn in a quare"""
    for _ in range(1):
        r = random.randint(0, 256)
        b = random.randint(0, 256)
        g = random.randint(0, 256)
        turd.pencolor(r, b, g)
        turd.forward(100)
        turd.right(90)



screen.exitonclick()
