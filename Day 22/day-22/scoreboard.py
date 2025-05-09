#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, int(self.screen.window_height() / 2) - 60)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score}  X  {self.r_score}", align=ALIGNMENT, font=FONT)
        self.screen.update()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
        if self.l_score > 5:
            return False
        else:
            return True

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
        if self.r_score > 5:
            return False
        else:
            return True

    def game_over(self, text):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER: {text}", align=ALIGNMENT, font=FONT)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=100, starty=100)
    screen.bgcolor("black")
    screen.title("Pong Score")
    screen.tracer(0)

    scoreboard = ScoreBoard()

    for _ in range(4):
        time.sleep(1)
        scoreboard.increase_l_score()
        time.sleep(1)
        scoreboard.increase_r_score()


    screen.exitonclick()
