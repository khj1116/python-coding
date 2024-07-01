#for name in ['철수', '영희', '길동', '민수'] :
#print("안녕!", name)

#sum = 0
#for i in range(1,5) :

    #sum = sum + i
    #print("i = ", i, "sum = ", sum)
#print(sum)

#for i in range(0,10):
    #result = i ** 2
    #print(result)
#list = [0,1,2,3,4,5,6,7,8,9]
#result = [a ** 2 for a in list]
#print(result)


#result_list = []
#for i in [0,1,2,3,4,5,6,7,8,9]:
    #result = i ** 2
    #result_list.append(result)
#print(result_list)

#코테 문제
start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money = money + before
    month += 1
while money < 100:
    money = money + after
    month += 1

print(month)