'''
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print('1부터 10까지의 합 : ', total)
'''
'''
total = 0
for num in range(11):
    total += num
print('1부터 10까지의 합 : ',total)
'''
'''
num = int(input('숫자를 입력하세요 :  : '))
while num != 4:
    print('1. Add \n2. Del\n3. list\n4. Quit')
   
    
    num = int(input('숫자를 입력하세요 :  : '))
'''
'''
sum = 0
num = 3
while num <= 100:
    if num % 3 == 0:
        sum += num
    num += 3  
print('3의 배수의 합 : ', sum)
'''
'''
i = 3
j = 0
while i :
    while j <= 8 :
        j += 1
        print(i, "x", j, "=",  i * j)
'''

'''
num = 0
while num < 9:
    num += 1
    print("3 *", num, "=", 3*num)        
'''
'''
i = 0
num = [1,2,3,4,5,6,7,8,9,10]
while i < 10:
    if num[i] % 2 == 0:
        print(num[i])
    i += 1
'''
'''
sum = 0
num = int(input('어디까지 계산할까요 : '))
i = 1
while i < num + 1: 
    sum += i
    i += 1
print("1부터", num, "까지 정수의 합 : ", sum)
'''

user_input = ""
while True:
    user_input = input("문자를 입력하세요 ('exit'입력 시 종료): ")
    print(f"입력한 문자 : {user_input}")
    if user_input != "exit":
        break
    
        
         

