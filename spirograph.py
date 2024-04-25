import turtle as t
import random

screen = t.Screen()

# Change the attribute and colorscheme of the turtle programme
t.colormode(255)

billy = t.Turtle()
billy.speed("fastest")


def random_color():
    """This function creates a random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # it puts the random color inside a tuple and returns the tuple
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        # The turtle moves randomly every
        billy.color(random_color())
        billy.circle(100)
        billy.setheading(billy.heading() + 10)


draw_spirograph(5)

screen.exitonclick()