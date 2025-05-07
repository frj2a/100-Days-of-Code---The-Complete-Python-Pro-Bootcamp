from turtle import Screen, Turtle
import time
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-MOVE_DISTANCE, 0), (-2 * MOVE_DISTANCE, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.screen = Screen()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(fun=self.move_up,key="Up")
        self.screen.onkey(fun=self.move_down,key="Down")
        self.screen.onkey(fun=self.move_left,key="Left")
        self.screen.onkey(fun=self.move_right,key="Right")

        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            # new_segment.resizemode("user")
            # new_segment.shapesize(1)
            new_segment.color("white")
            # new_segment.pencolor("white")
            # new_segment.pensize(UNIT)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.screen.update()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)
        self.screen.update()
        time.sleep(0.1)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def finish(self):
        self.screen.exitonclick()

