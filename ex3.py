#별 그리기
import turtle as x
import random as y
screen = x.Screen()
screen.setup(width=800, height=600)

t1 = x.Turtle()
x.color('yellow')
x.shapesize(1)
x.speed(0)
x.pensize(1)
x.bgcolor('black')


def fall():
    a = y.randint(-200,200)
    b = y.randint(-200,200)
    x.up()
    x.goto(a,b)
    x.down()
    x.begin_fill()
    for i in range(5):
        x.forward(7)
        x.right((360/5)*2)
        x.forward(7)
        x.left(360/5)
    x.end_fill()
    
j = int(input())     #input으로 개수를 할당 받기
for i in range(j):
    x.fillcolor("yellow")
    fall()
    
    
        
x.mainloop()   
    
    