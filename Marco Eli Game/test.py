import turtle 

pen =  turtle.Turtle()
screen = turtle.Screen()
screen.screensize(640, 480)
screen.setup(width=1280, height=960)
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

def activate_textbox():
    user_text = screen.textinput("Input", "Enter text for display:")
    pen.clear()
    pen.goto(50, -100)
    pen.pendown()
    pen.forward(400)
    pen.penup()
    if len(user_text) > 21:
        pen.penup()
        pen.goto(60, -80)
        pen.pendown()
        pen.pencolor("red")
        pen.write("Too many characters!", font=("fixedsys", 20, "bold"))
        pen.penup()
        pen.pencolor("lime")
    elif user_text is not None:
        # Clear old text if needed and display new one
        pen.penup()
        pen.goto(60, -80)
        pen.pendown()
        pen.write(">"+str(user_text.upper()), font=("fixedsys", 20, "bold"))
        pen.penup()
    screen.listen()

def update_details():
    pen.penup()
    pen.goto(-450, 270)
    pen.pendown()
    pen.pencolor("red")
    pen.write("Too many characters!", font=("fixedsys", 20, "bold"))
    pen.penup()
    pen.pencolor("lime")
# Key binding to simulate text box interaction
screen.listen()
screen.onkey(activate_textbox, "t")  # Press spacebar to trigger input
screen.onscreenclick(lambda x, y: activate_textbox())

turtle.done()
