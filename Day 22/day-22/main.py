#! /usr/bin/python3
# -*- coding: utf-8 -*-

from turtle import Screen
from paddle import Paddle
from ball import Ball
# from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600, startx=100, starty=100)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    # l_paddle.sety(ball.ycor())    # computer moves left paddle

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle:
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect ball leaving the game area:
    if ball.xcor() > 400:
        game_is_on = False
    elif ball.xcor() < -400:
        game_is_on = False

screen.exitonclick()