from  turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_add=10
        self.y_add=10

    def create(self):
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.goto(0,0)

    def move(self):
        x=self.xcor()+ self.x_add
        y=self.ycor()+ self.y_add
        self.goto(x=x,y=y)

    def bounce_y(self):
        self.y_add *= -1

    def bounce_x(self):
        self.x_add *= -1
        
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move()