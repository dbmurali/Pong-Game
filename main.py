from turtle import Screen
from score import Board
from ball import  Ball
import  time
from paddel import Paddel
from turtle import  Turtle



screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

# CENTER LINE
center_line=Turtle()
center_line.hideturtle()
center_line.color("white")
center_line.penup()
center_line.goto(0,-290)
center_line.setheading(90)
center_line.pendown()

for i in range(30):
    center_line.pendown()
    center_line.fd(10)
    center_line.penup()
    center_line.fd(10)


pd=Paddel()
pd2=Paddel()
ball=Ball()

#ADD KEY CONTROLS
screen.listen()
screen.onkey(pd2.up,"Up")
screen.onkey(pd2.down,"Down")
screen.onkey(pd.up,"w")
screen.onkey(pd.down,"s")


pd.create(-350,0)
pd2.create(350,0)
score=Board()
score.score_board()
ball.create()


ball_sleep=0.1
game_on=True
while game_on:
     time.sleep(ball_sleep)
     screen.update()
     ball.move()
     if ball.ycor()>280 or ball.ycor()<-280:
       ball.bounce_y()

     # DETECT COLLISION WITH PADDEL
     if ball.distance(pd2)<50 and ball.xcor() >320:
         ball.bounce_x()
         ball_sleep*=0.9
     if ball.distance(pd)<50 and ball.xcor() < -320:
         ball.bounce_x()
         ball_sleep *= 0.9

     # CHECK BOUNDARY AND ADD SCORE
     if ball.xcor()>500:
        score.add_score_pl_1()
        ball.reset()
        ball_sleep=0.1

     if ball.xcor()<-500:
         score.add_score_pl_2()
         ball.reset()
         ball_sleep = 0.1


screen.exitonclick()