from turtle import Turtle

START_POSITION = (350, 0)
SIDES = {'paddle_left': 50, 'paddle_right': -50}


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.setpos(position)

    def up(self):
        new_ycor = self.ycor() + 50
        self.setpos(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 50
        self.goto(self.xcor(), new_ycor)




