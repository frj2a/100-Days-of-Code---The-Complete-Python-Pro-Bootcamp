#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("white")
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.screen.update()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.testing = False

    def move(self):
        if self.testing:
            if self.xcor() > 380 or self.xcor() < -380:
                self.bounce_x()
            if self.ycor() > 280 or self.ycor() < -280:
                self.bounce_y()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.screen.update()

    def bounce_y(self):
        self.y_move = -self.y_move
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_position(self):
        self.setpos(0,0)
        self.move_speed = 0.1
        self.bounce_x()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=100, starty=100)
    screen.bgcolor("black")
    screen.title("Pong Ball")

    ball = Ball()
    ball.testing = True

    for _ in range(256):
        ball.move()
        # time.sleep(0.1)

    screen.exitonclick()
