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
        self.food_area_width = self.screen.window_width() - 20
        self.food_area_height = self.screen.window_height() - 20
        self.refresh()

    def refresh(self):
        random_x = random.randint(-int(self.food_area_width / 2), int(self.food_area_width / 2))
        random_y = random.randint(-int(self.food_area_height / 2), int(self.food_area_height / 2))
        self.goto(random_x, random_y)


SCREEN_WIDTH = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=int(SCREEN_WIDTH / 2), height=int(SCREEN_WIDTH / 2))
    screen.bgcolor("black")
    screen.title("My Snake Game")

    tims_food = Food()
    for _ in range(5):
        tims_food.refresh()
        time.sleep(1)

    screen.exitonclick()