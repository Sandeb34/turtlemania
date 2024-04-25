import turtle as t
import random

# Change the attribute and colorscheme of the turtle programme
t.colormode(255)


billy = t.Turtle()


def random_color():
    """This function creates a random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # it puts the random color inside a tuple and returns the tuple
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
# optional directions for left, straight, right, left
billy.pensize(15)
# change the width of the pen
billy.speed("fastest")
# changes the speed at which the pen draws

for _ in range(200):
    # The turtle moves randomly every
    billy.color(random_color())
    # the color changes randomly according to the random_color() function. every loop changes the color
    billy.forward(30)
    billy.setheading(random.choice(directions))
#     chooses a random direction from the directions list


screen = t.Screen()
screen.exitonclick()