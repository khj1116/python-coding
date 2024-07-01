#lotto number를 생성하는 프로그램
#1 ~ 46사이의 숫자 중 6개의 숫자가 필요합니다.

import random
def lot_num():
    num = random.randint(1,45)
    return num
lotto_number = []
cnt = 0

while True:
    if cnt > 5: #0,1,2,3,4,5까지 6개 숫자
        break #6개의 중복 없는 숫자가 나오면 탈출
    random_number = lot_num()
    if random_number not in lotto_number: #뽑은 숫자가 중복이 아니면
        lotto_number.append(random_number) #리스트에 추가
        cnt += 1 #탈출해야 하니까 조건을 다 충족했을 때 count 하나 높임
    
print(lotto_number)    



'''
def cal1(x, y):
    num1 = int(input("첫번째 숫자는?"))
    num2 = int(input("두번째 숫자는?"))
    result1 = x + y
    print(f"{x} + {y} = {result1}")
    
   
    
def cal2 (x,y):  
    result2 = x - y
    print(f"{x} - {y} = {result2}")
    
    
def cal3(x,y):
    result3 = x * y    
    print(f"{x} * {y} = {result3}")
    
    
def cal4(x,y):
    result4 = x / y
    if num2 == 0:
        print("0으로 나눌 수 없습니다. ")
    else:
        print(f"{x} / {y} = {result4}")
    
for i in range(5):
    cal1(num1,num2)
    cal2(num1,num2)
    cal3(num1,num2)
    cal4(num1,num2)
 '''
 
 #def hello(name):
 #    """이 함수는 주어진 이름으로 인사 메시지를 출력합니다."""   
 #    print(f"안녕하세요, {name}님!")
    
#hello("Alice")
#hello("Jack")
'''
def sub(a, b):
    result1 = a - b
    print(f"{a} - {b} = {result1}")
for x in range(5):
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    sub(num1, num2)
'''
'''    
def mul(x, y):
    result2 = x * y
    print(f"{x} * {y} = {result2}")
for i in range(5):
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    mul(num1, num2)
'''
'''
numbers = [1,2,3,4,5]
def sum(numbers) :
    numbers = [1,2,3,4,5]
    tot = 0

    for num in numbers:
        tot += num
    print("합계:",tot)
sum(numbers)
'''

'''
def up(upper_text):
    for char in text:
        upper_text += char.upper()
    return upper_text

text = "hello python"
upper_text = ""
print("대문자 변환:" , up(upper_text))
'''



'''
def square(n): 
    return n ** 2

num = int(input("입력 값 : "))
result = square(num)
print("제곱값 : ", result)
'''
'''
def get_max(a,b):

    if n1 > n2 :
        return n1
    elif n1 < n2 : 
        return n2
    else:
        print("두 수는 같습니다.")
    
 
n1 = int(input("값1 : "))
n2 = int(input("값2 : "))
result = get_max(n1,n2)    
print(result)
'''   
        

