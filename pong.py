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

while True:
    window.update()