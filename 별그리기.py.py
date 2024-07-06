#별 그리기
import turtle as t
import random as r
import time
screen = t.Screen()

screen.setup(width=800, height=600)
screen.tracer(0)

t1 = t.Turtle()
t.color('yellow')
t.hideturtle()
t.shapesize(1)
t.speed(0)
t.pensize(1)
t.bgcolor('black')


def fall(a,b):
    
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(7)
        t.right((360/5)*2)
        t.forward(7)
        t.left(360/5)
    t.end_fill()
if __name__ == "__main__" :
    lt = []
    for i in range(50):
        x = r.randint(-200,200)
        y = r.randint(50,200)
        lt.append([x,y])
while True :
    t.clear()
    for i in range(len(lt)):
        fall(lt[i][0],lt[i][1])
        screen.update()

        lt[i][1] -= 15
        if lt[i][1] < -200 :
            x=r.randint(-300,300)
            y=r.randint(50,300)
            lt[i][0]=x
            lt[i][1]=y
    time.sleep(0.1)        
# j = int(input())     #input으로 개수를 할당 받기
# for i in range(j):
#     x.fillcolor("yellow")
#     fall()
    
    
        
x.mainloop()   
    
    