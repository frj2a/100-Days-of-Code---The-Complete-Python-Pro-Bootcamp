#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        self.move_speed = 0.1
        self.testing = False
        self.screen.update()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        if self.testing:
            if not self.is_at_finish_line():
                self.forward(MOVE_DISTANCE)
        else:
            self.forward(MOVE_DISTANCE)
        self.screen.update()

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.go_to_start()
            return True
        else:
            return False


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600, startx=100, starty=100)
    screen.bgcolor("white")
    screen.title("Turtle Cross' Turtle")
    screen.tracer(0)

    player = Player()
    player.testing = True

    screen.listen()
    screen.onkey(key="Up", fun=player.go_up)

    screen.exitonclick()

