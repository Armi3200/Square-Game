import turtle
import random

screen = turtle.Screen()
screen.title('DENEME')
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.tracer(0)

square = turtle.Turtle()
square.speed(0)
square.color('lime')
square.shape('square')
square.penup()
square.goto(0, 0)



fruit = turtle.Turtle()
fruit.speed(0)
fruit.color('red')
fruit.shape('circle')
fruit.penup()

point = 0

writing = turtle.Turtle()
writing.speed(0)
writing.color('white')
writing.penup()
writing.hideturtle()
writing.goto(0, 200)
writing.write('Point : {}'.format(point), align="center")



def go_up():
    y = square.ycor()
    y = y + 15
    square.sety(y)
def go_down():
    y = square.ycor()
    y = y - 15
    square.sety(y)
def go_left():
    x = square.xcor()
    x = x - 15
    square.setx(x)
def go_rigt():
    x = square.xcor()
    x = x + 15
    square.setx(x)

screen.listen()
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_rigt, 'Right')




while True:
    screen.update()
    if square.xcor()>240 or square.xcor()<-240:
       square.goto(0, 0)

       point = 0
       writing.clear()
       writing.write('Point : {}'.format(point), align="center")
 
       

    if square.ycor()>240 or square.ycor()<-240:
        square.goto(0, 0)

        point = 0
        writing.clear()
        writing.write('Point : {}'.format(point), align="center")
 
        
    
    if square.distance(fruit) < 20:
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        point = point + 10
        writing.clear()
        writing.write('Point : {}'.format(point), align="center")

 
    
    
        
    
    
        



    









