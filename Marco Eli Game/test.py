import turtle 
pen =  turtle.Turtle()
screen = turtle.Screen()


pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(-250, 250)
pen.pendown()
pen.pencolor("green")

pen.write("I", font=("arial", 24, "bold italic"))

turtle.done()