import turtle as t
import random as r

t1 = t.Turtle()
t1.color('red')
t1.shape('turtle')
t1.shapesize(1)
t1.pensize(5)
t1.up()
t1.goto(-300,100)
t1.pendown()
t1.speed(1)

t2 = t.Turtle()
t2.color('purple')
t2.shape('turtle')
t2.shapesize(1)
t2.pensize(5)
t2.up()
t2.goto(-300,-100)
t2.pendown()
t2.speed(1)


for i in range(20):
    t1.forward(r.randint(1,50))
    t2.forward(r.randint(1,50))
t.mainloop()




    
    

