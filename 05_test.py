#integer = float(input("정수를 입력하세요 : "))
#multi = 1.0
#for i in range(1,integer+1):
    #multi = multi * i
#print(f"{integer}!은 {multi}이다")

fruit_list = []

for fruit in range(1,6):
    fruit_plus = input("과일이름 : ")
    fruit_list.append(fruit_plus)

print(fruit_list)