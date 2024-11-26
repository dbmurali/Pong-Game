from turtle import Turtle


ALIGN="CENTER"
FONT=("Arial",20,"normal")
COLOR="White"

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.player_1 =0
        self.player_2=0

    def score_board(self):
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0,260)

        self.write(f"SCORE : {self.player_1}              SCORE : {self.player_2}", align=ALIGN, font=FONT)

    def add_score_pl_1(self):
        self.clear()
        self.player_1+=1
        self.write(f"SCORE : {self.player_1}              SCORE : {self.player_2}", align=ALIGN, font=FONT)

    def add_score_pl_2(self):
        self.clear()
        self.player_2+=1
        self.write(f"SCORE : {self.player_1}              SCORE : {self.player_2}", align=ALIGN, font=FONT)

