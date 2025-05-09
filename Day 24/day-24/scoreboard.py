#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time
import random

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 260)
        self.testing = False
        with open(".high_score", mode="r") as file:
            contents = file.read()
        self.highest_score = int(contents)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highest: {self.highest_score}", align=ALIGNMENT, font=FONT)
        self.screen.update()

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(".high_score", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

SCREEN_WIDTH = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_WIDTH, startx=100, starty=100)
    screen.bgcolor("black")
    screen.title("My Snake Game's Scoreboard")
    screen.tracer(0)

    tims_score = Scoreboard()
    tims_score.testing = True
    for _ in range(3):
        for i in range(random.randint(2,6)):
            time.sleep(1)
            tims_score.increase_score()
        time.sleep(1)
        tims_score.reset_scoreboard()

    screen.exitonclick()
