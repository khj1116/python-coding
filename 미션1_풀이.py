#문제 2
'''
c1 = input()
c2 = input()
print(c2)
print(c1)
'''
'''
#문제3
n = int(input("정수를 입력하세요 : "))
if n < 0:
    if n % 2 == 0:
        print("A")
    else:
        print("B")
else :
     if n % 2 == 0:
        print("C")
     else:
        print("D")
'''
#문제4
a, b = map(int,input().strip().split(' '))  #map(a,b)함수 : b를 a형식으로 맵핑할 때 사용
                                            #strip() : 좌우 공백 제거
                                            #spli() : 따옴표 안을 기준으로 문자열을 분리
result = a != b
print(result)

#문제5
first = ord('a')
a = ord(input())
while first <= a:
    print(chr(first), end = ' ')
    first = first + 1


        
    
