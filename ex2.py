#정삼각형 그리기
'''
import turtle as x
t1 = x.Turtle()
x.shape("turtle") #turtle 설정

x.forward(100) #x축 방향으로 이동
x.left(120) #왼쪽으로 120도 방향이동
x.forward(100) #그 방향으로 100만큼 이동
x.left(120) #왼쪽으로 120도 방향이동
x.forward(100) #그 방향으로 100만큼 이동
x.left(120) #왼쪽으로 120도 방향이동

for i in range(5): #반복문
    x.forward(100)
    x.left(120)
x.mainloop()
'''
#원 그리기
'''
import turtle as x
t1 = x.Turtle()
x.shape("turtle") #turtle 설정



for i in range(5): #반복문
    x.forward(100)
    x.left(120)
x.mainloop()
'''
#다각형 그리기
import turtle as x
import time
n = int(input("정n각형의 n을 입력 해 주세요 : "))

x.shape("turtle") #turtle 설정
x.speed(3)
count = 0
while count<n:
    x.forward(100) 
    time.sleep(6)  
    x.right(360/n) 
    count += 1
x.mainloop()

#가장 빠른 0 
#가장 느린 1
#느린 2
#기본 6
#빠른 10

