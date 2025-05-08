#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time

class Paddle(Turtle):

    def __init__(self, posit):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posit)
        self.screen.update()

    def go_up(self):
        if self.ycor() < int(self.screen.window_height()/2 - self.shapesize()[0] * 10 ):
            self.goto(self.xcor(), self.ycor() + 20)
            self.screen.update()

    def go_down(self):
        if self.ycor() > -int(self.screen.window_height()/2 - self.shapesize()[0] * 15 ):
            self.goto(self.xcor(), self.ycor() - 20)
            self.screen.update()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=100, starty=100)
    screen.bgcolor("black")
    screen.title("Pong Paddle")
    screen.listen()
    paddle = Paddle((int(SCREEN_WIDTH / 2) - 50, 0))
    screen.onkey(key="Up", fun=paddle.go_up)
    screen.onkey(key="Down", fun=paddle.go_down)


    screen.exitonclick()
