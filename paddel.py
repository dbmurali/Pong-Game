from turtle import Turtle

class Paddel(Turtle):
    def __init__(self):
        super().__init__()
        
    def create(self,x,y):

        self.shape("square")
        self.color("white")
        self.shapesize(3,1)
        self.penup()
        self.goto(x,y)

    def up(self):
        if self.ycor()<255:
         self.goto(self.xcor(),self.ycor()+50)

    def down(self):
        if self.ycor() > -255:
         self.goto(self.xcor(),self.ycor()-50)




