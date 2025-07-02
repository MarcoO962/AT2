import turtle

pen =  turtle.Turtle()
screen = turtle.Screen()
screen.screensize(640, 480)
screen.bgcolor("black")
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.shape("square")
pen.pensize(5)
pen.pencolor("lime")

pen.goto(60, -80)
pen.pendown()
pen.write("CLICK SCREEN TO WRITE", font=("fixedsys", 20, "bold"))
pen.penup()
pen.goto(50, -100)
pen.pendown()
pen.forward(400)
pen.penup()







pen.goto(-450, 350)
pen.pendown()


pen.write("TEST /n ", font=("fixedsys", 30, "bold"))

turtle.done()