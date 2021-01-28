import turtle
wn= turtle.Screen() #creates a screen
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600) #properties of the screen
wn.tracer(0) #we dont want the game to be manually refreshed



#now we have to create 2 paddles and a ball
paddle_a= turtle.Turtle()
paddle_a.speed(0) #speed of the animation, that we set to maximum
paddle_a.shape("circle")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b= turtle.Turtle()
paddle_b.speed(0) #speed of the animation, that we set to maximum
paddle_b.shape("circle")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

ball= turtle.Turtle()
ball.speed(0) #speed of the animation, that we set to maximum
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx= 1 #to move the ball i need a x and w movement unlike the paddles. The numbers indicate the ball speed
ball.dy= 1

#now we need to move the elements of the game using our keyword by creating a function
def paddle_a_up():
    y=paddle_a.ycor () #it takes the y coordinate
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor () #it takes the y coordinate
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor () #it takes the y coordinate
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor () #it takes the y coordinate
    y -=20
    paddle_b.sety(y)

#we need to call the function so that our inputs will match the elements movement
wn.listen() #this method allows our window to take inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




#every game needs a main game loop
while True:
    wn.update() #while the loop runs, the game will update itself

    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # movement when the ball hits something
    if ball.ycor() > 290: #why 290? cause the height of the screen is 600 px. Since it starts from 0, it will be +300 and -300
        ball.sety(290)
        ball.dy *=-1 #this inverts the direction of the ball

    if ball.ycor() < -290: #why 290? cause the height of the screen is 600 px. Since it starts from 0, it will be +300 and -300
        ball.sety(-290)
        ball.dy *=-1 #this inverts the direction of the ball

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *=-1

    #paddle and ball collisione
    if (ball.xcor()>340 and ball.xcor() <350)and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor() >-350)and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1




