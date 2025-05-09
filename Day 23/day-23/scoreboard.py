#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-280, int(self.screen.window_height() / 2) - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align="center", font=FONT)

SCREEN_WIDTH = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600, startx=100, starty=100)
    screen.bgcolor("white")
    screen.title("Turtle Cross's Scoreboard")

    tims_score = Scoreboard()
    for i in range(5):
        tims_score.increase_score()
        time.sleep(1)
    tims_score.game_over()

    screen.exitonclick()