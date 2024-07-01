#num_list = [1,2,3,4,5,6,7,8,9,10]
#for a in num_list:
#    if a % 2 == 0:
#        print(a)

#list의 요소 중 "cherry"가 들어간 문자열만 출력하는 프로그램

#list = ["apple", "banana", "cherry", "date", "elderberry"]
#for i in list:
#    if i == "cherry":
#        print(i)
        
#list의 요소 중 음수만 출력하는 프로그램
list = [10,-5,0,3,-2,8,-7]
for i in list:
    if i < 0 :
        print(i)





#list의 요소 중 문자열 길이가 5이하인 문자열만 출력하는 프로그램(집에서 스스로 학습한 후 디스코드에서 월요일 제출)
list = ["apple", "banana", "cherry", "date", "elderberry"]
for i in list: 
    if len(i) <= 5 :
        print(i)    