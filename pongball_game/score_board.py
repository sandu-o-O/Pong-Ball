from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')
FINAL_SCORE = 10


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()

    def scores(self):
        self.clear()
        self.setpos(0, 275)
        self.write('Score', align=ALIGNMENT, font=('Courier', 20, 'normal'))
        self.setpos(2, 200)
        self.write(f"{self.l_score}   :   {self.r_score}", align=ALIGNMENT, font=FONT)

    def hit_a_r_score(self):
        self.r_score += 1
        self.scores()

    def hit_a_l_score(self):
        self.l_score += 1
        self.scores()

    def game_end(self):
        if self.r_score == FINAL_SCORE:
            self.setpos(0, 0)
            self.write("Right player wins!", align=ALIGNMENT, font=FONT)
            return True

        if self.l_score == FINAL_SCORE:
            self.setpos(0, 0)
            self.write("Left player wins!", align=ALIGNMENT, font=FONT)
            return True
