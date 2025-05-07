#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, int(self.screen.window_height() / 2) - 30)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

SCREEN_WIDTH = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=int(SCREEN_WIDTH / 2), height=int(SCREEN_WIDTH / 2))
    screen.bgcolor("black")
    screen.title("My Snake Game")

    tims_score = ScoreBoard()
    for i in range(5):
        tims_score.increase_score()
        time.sleep(1)
    tims_score.game_over()

    screen.exitonclick()