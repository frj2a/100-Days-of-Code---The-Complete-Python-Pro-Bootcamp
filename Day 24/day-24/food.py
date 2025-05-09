#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import random
import time

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(random_x, random_y)
        self.screen.update()

SCREEN_WIDTH = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_WIDTH, startx=100, starty=100)
    screen.bgcolor("black")
    screen.title("My Snake Game's food")
    screen.tracer(0)

    tims_food = Food()
    for _ in range(5):
        tims_food.refresh()
        time.sleep(1)

    screen.exitonclick()