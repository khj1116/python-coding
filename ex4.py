# import turtle as t       

# t.shape('turtle')

# while True:
#     n1 = int(input("입력 값 : "))
#     n2 = input("색깔 : ")
#     t.clear()
#     for j in range(2):   
#         t.color(n2)
#         t.begin_fill() 
#         for i in range(4):  #0,1,2,3
#             t.forward(n1)
#             t.right(90)
#         t.end_fill()
#         t.goto(-(n1+100),0)
        
        
#t.mainloop()

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

#사각형 색 채우기
# import turtle as t 
# t.shape('turtle')
# while True:
#     x = int(input("값을 입력해주세요 : "))
#     y = input("색깔을 입력해주세요 : ")
#     t.clear()
#     for i in range(2):
#         t.color(y)
#         t.begin_fill()
#         for j in range(4):
#             t.forward(x)
#             t.right(90)
#         t.end_fill()
#         t.goto(-(x+100), 0)
        
# t.mainloop()

'''
import turtle as t 
t.shape('turtle')
color = ['red', 'blue', 'green', 'pink', 'silver', 'purple', 'black', 'brown']
while True:
    for i in range(8):
        if i % 2 == 0:
            t.color(color[i])
            t.begin_fill()
            for j in range(4):
                t.forward(100)
                t.left(90)
            t.end_fill()
            t.left(45)
        else:
            t.color(color[i])
            t.begin_fill()
            for j in range(4):
                t.forward(100)
                t.left(90)
            t.end_fill()
            t.left(45)
        
        
t.mainloop()
'''


#실습하기: 라이언 만들기
import turtle

s = turtle.Screen()
s.setup(650, 800)

