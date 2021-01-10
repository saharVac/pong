import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #stops window from updating, has to be manually updted (speeds things up)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # max possible speed of animation
paddle_a.shape("square") # by default 20px x 20px 
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # max possible speed of animation
paddle_b.shape("square") # by default 20px x 20px 
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # max possible speed of animation
ball.shape("square") # by default 20px x 20px 
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# FUNCTIONS

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


window.listen() # listen for keyboard input
window.onkey(paddle_a_up, "w")
window.onkey(paddle_a_down, "s")
window.onkey(paddle_b_up, "Up")
window.onkey(paddle_b_down, "Down")

while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290) # to avoid problem
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290) # to avoid problem
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -2
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 2

    # COLLISION

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1