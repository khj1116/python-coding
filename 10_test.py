#for i in range(1,6):
#    for k in range(i):
#        print("*", end = '')
#    print()
#for i in range(5,0,-1):
#    for j in range(i):
#        print("*", end = '')
#    print()

numbers = [1,2,3,4,5]
sum = 0
for num in numbers:
    if num == 3:
        break
    sum += num
print("리스트 요소의 합:", sum)


