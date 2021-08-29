from turtle import Turtle, Screen
from puddle import Puddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_puddle = Puddle((350, 0))
l_puddle = Puddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_puddle.go_up, "Up")
screen.onkeypress(r_puddle.go_down, "Down")

screen.onkeypress(l_puddle.go_up, "w")
screen.onkeypress(l_puddle.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    # Detect collision with a puddle
    if ball.xcor() > 320 and ball.distance(r_puddle) < 50 or ball.xcor() < -320 and ball.distance(l_puddle) < 50:
        ball.bounce_x()

    # when r_puddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # when l_puddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()












screen.exitonclick()