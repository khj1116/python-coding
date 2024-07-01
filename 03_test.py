#count = int(input("입력 횟수 : "))
#for num in range(count):
    
    #print("good") 
    
 
#for i in range(100,0,-1):
    #print(i)
#numbers = [1,2,3,4,5]
#sum = 0
#for num in numbers:
#    if num == 3:
#        continue
#    sum += num
#print("리스트 요소의 합 : ", sum)
'''
sum = 0
count = 0
for i in range(10):
    num = int(input("사용자 입력 : "))
    if num == 0:
        break
    sum += num
    count += 1
average = sum / count
print(average)
'''



sum = 0
avg = 0
def tot(numbers):
    tot = sum(numbers)
    avg = tot / len(numbers)
    return avg


numbers = [10,20,30,40,50]
avg = tot(numbers)
print("평균:", avg)

