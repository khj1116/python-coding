import random

secret_num = random.randint(1,100)
cnt = 0
guess = int(input("1부터 100 사이의 숫자를 추측해보세요 : "))
while True:
    guess = int(input("1부터 100 사이의 숫자를 추측해보세요 : ")) 
    cnt += 1
    if cnt < 10:
        if guess == secret_num:
            break
        elif guess < secret_num:
            print("너무 낮아요! 다시 시도해주세요.")
        else:
            print("너무 높아요! 다시 시도해주세요. ")
    else:
        print("횟수를 모두 소모하였습니다. ")

print("축하합니다! 정답입니다!")