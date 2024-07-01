'''
def greet_with_message(name, message="만나서 반가워요!"):
    print(f"안녕하세요, {name}님! {message}")
    
greet_with_message("alice")
greet_with_message("Bob", "잘 지내시죠?")
greet_with_message("Tom", "오늘 하루 어땠나요?")
greet_with_message("Jack", "반갑습니다!")
'''


def happy_birthday(name, age=20):
    print(f"{name}님! {age}번째 생일을 축하합니다!")

name1 = input()
age1 = input()  

#나이가 숫자로 입력되었는지 판단하여 
#숫자로 나이가 입력되었다면 숫자로 변환
#나이가 제대로 입력되지 않았다면 기본값으로 20 설정
if age1.isdigit():
    ageint = int(age1)
else:
    ageint = 20
    
happy_birthday(name1,ageint)


    
    

