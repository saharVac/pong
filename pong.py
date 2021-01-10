import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #stops window from updating, has to be manually updted (speeds things up)



while True:
    window.update()