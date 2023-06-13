import turtle

win = turtle.Screen()
win.title("Ping-Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# racket_left
racket_left = turtle.Turtle()
racket_left.speed(0)
racket_left.shape("square")
racket_left.color("blue")
racket_left.shapesize(stretch_len=1, stretch_wid=5)
racket_left.penup()
racket_left.goto(-350, 0)

# racket_right
racket_right = turtle.Turtle()
racket_right.speed(0)
racket_right.shape("square")
racket_right.color("orange")
racket_right.shapesize(stretch_len=1, stretch_wid=5)
racket_right.penup()
racket_right.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# score
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("red")
score.penup()
score.hideturtle()
score.goto(0, 265)
score.write("Player A: 0 || Player B: 0", align="center", font=("Verdana", 15, "normal"))
score_A = 0
score_B = 0
# function_move_racket_left
def racket_left_up():
    y = racket_left.ycor()
    y += 20
    racket_left.sety(y)

def racket_left_down():
    y = racket_left.ycor()
    y -= 20
    racket_left.sety(y)

# keyboard_racket_left
win.listen()
win.onkeypress(racket_left_up, "w",)
win.onkeypress(racket_left_down, "s")

# function_move_racket_right
def racket_right_up():
    y = racket_right.ycor()
    y += 20
    racket_right.sety(y)


def racket_right_down():
    y = racket_right.ycor()
    y -= 20
    racket_right.sety(y)

# keyboard_racket_right
win.listen()
win.onkeypress(racket_right_up, "Up")
win.onkeypress(racket_right_down, "Down")

while True:
    win.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A +=1
        score.clear()
        score.write("Player A: {} || Player B: {}".format(score_A, score_B), align="center",
                    font=("Verdana", 15, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        score.clear()
        score.write("Player A: {} || Player B: {}".format(score_A, score_B), align="center",
                    font=("Verdana", 15, "normal"))


    if (ball.xcor() > 340) and (ball.ycor() < racket_right.ycor() + 50) and (ball.ycor() > racket_right.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() < -340) and (ball.ycor() < racket_left.ycor() + 50) and (ball.ycor() > racket_left.ycor() - 50):
        ball.dx *= -1

    # rocket_limit
    if racket_left.ycor() > 260:
        racket_left.goto(-350, 260)

    if racket_left.ycor() < -240:
        racket_left.goto(-350, -240)

    if racket_right.ycor() > 260:
        racket_right.goto(350, 260)

    if racket_right.ycor() < -240:
        racket_right.goto(350, -240)

