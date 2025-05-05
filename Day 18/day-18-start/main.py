import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("classic")
tim.color("green", "red")
screen.colormode(255)
turtle.colormode(255)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# REPEATS = 50
# LINE_LEN = 10
# GAP_LEN = 10
#
# tp = tim.pos()
# tim.penup()
# tim.setx(tp[0] - 500)
#
# for _ in range(REPEATS):
#     tim.pendown()
#     tim.forward(LINE_LEN)
#     tim.penup()
#     tim.forward(GAP_LEN)




# import random
#
# SHAPES = 8
# SIDE_LEN = 100
#
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "slateGray", "SeaGreen"]
#
# def draw_shape(sides):
#     angle = 360 / (shape + 3)   # the triangle is the first one
#     for _ in range(shape + 3):
#         tim.forward(SIDE_LEN)
#         tim.right(angle)
#     # tim.pencolor(random.randint(0,155)+100, random.randint(0,155)+100, random.randint(0,155)+100)
#     tim.pencolor(random.choice(colors))
#
# for shape in range(SHAPES + 1):
#     draw_shape(shape)
# tim.forward(SIDE_LEN)


import random
#
# angles = [0, 90, 180, 270]
# tim.pen(pensize=15, speed=10)
#
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r, g, b)
    return rand_color
#
# for _ in range(200):
#     tim.setheading(random.choice(angles))
#     # tim.pencolor(random.choice(colors))
#     tim.pencolor(random_color())
#     tim.forward(32)



ANGLE = 10
RADIUS = 100

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.pencolor(random_color())
        tim.circle(RADIUS)
        tim.setheading(tim.heading() + gap_size)


tim.pen(pensize=1, speed=10)
draw_spirograph(ANGLE)


screen.exitonclick()