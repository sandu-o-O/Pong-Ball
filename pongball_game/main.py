from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Ball Game')
screen.tracer(0)

dashed_line = Turtle()
dashed_line.hideturtle()
dashed_line.penup()
dashed_line.goto(0, -300)
dashed_line.setheading(90)
'''while dashed_line.position() == (0, 300):'''
for _ in range(20):
    dashed_line.pencolor('white')
    dashed_line.pendown()
    dashed_line.forward(15)
    dashed_line.penup()
    dashed_line.forward(15)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()
score_board.scores()

screen.listen()
screen.onkey(fun=paddle_left.up, key="q")
screen.onkey(fun=paddle_left.down, key='a')
screen.onkey(fun=paddle_right.up, key="p")
screen.onkey(fun=paddle_right.down, key='l')


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50:
        ball.hit_the_paddle()
    elif ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.hit_the_paddle()

    if ball.xcor() > 400:
        score_board.hit_a_l_score()
        ball.refresh()
    elif ball.xcor() < -400:
        score_board.hit_a_r_score()
        ball.refresh()

    if score_board.game_end():
        game_is_on = False

ball.move()


