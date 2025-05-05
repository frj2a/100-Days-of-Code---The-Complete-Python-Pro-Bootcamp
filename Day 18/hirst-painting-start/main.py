import turtle
import random
import colorgram
# https://pypi.org/project/colorgram.py/

SPACING = 50
DIAMETER = 20
colors = colorgram.extract("image.jpg",32)

rgb_colors=[]
for color in colors:
    if color.hsl.l < 200:
        rgb_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb_colors.append(rgb_color)

tim = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)
orig_pos = tim.pos()
tim.up()
tim.hideturtle()

for y in range(10):
    for x in range(10):
        tim.setpos(orig_pos[0] + SPACING * (x - 5), orig_pos[1] + SPACING * (y - 5))
        tim.dot(20, random.choice(rgb_colors))



screen.exitonclick()