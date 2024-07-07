#문제 1
'''
max_number = 10
def func_a(gloves):   #중복되는 원소의 개수를 세기 위해 func_a함수 정의
    cnt = [0 for i in range(max_number+1)] #0부터 10까지 중복되는 수 찾기
    for a in gloves:
        cnt[a] = cnt[a] + 1
    return cnt


def solution(left_gloves, right_gloves):    #왼쪽 장갑과 오른쪽 장갑의 리스트를 함수로 정의
    left_cnt = func_a(left_gloves)
    right_cnt = func_a(right_gloves)

    tot = 0
    for n in range(1,max_number+1):
        tot += min(left_cnt[n], right_cnt[n]) #
    return tot

left_gloves=[2,1,2,2,4]
right_gloves=[1,2,2,4,4,7]
result = solution(left_gloves,right_gloves)

print("함수의 반환값은 ", result, "입니다.")
'''
#문제2(arr의 길이는 1이상 100이하, arr에 들어있는 숫자는 1이상 1000이하의 자연수)
'''
def func_a(arr):   #3의 배수 세는 함수 정으
    cnt = 0
    for i in arr:
        if i % 3 == 0:
            cnt += 1
    return cnt
def func_b(arr): #5의 배수 세는 함수 정의
    cnt = 0
    for j in arr:
        if j % 5 == 0:
            cnt += 1
    return cnt
def func_c(three, five): #3의 배수개수와 5의배수 개수 비교
    if five > three:
        return "five"
    elif five < three:
        return "three"
    else:
        return "same"

def solution(arr):  
    cnt_three = func_a(arr)   #func_a 함수를 cnt_three 저장
    cnt_five = func_b(arr)      #func_b 함수를 cnt_five 저장
    result = func_c(cnt_three,cnt_five)  #func_c 함수를 result저장
    return result
arr = [2,12,15,10,20,22,25,30,45,5]
ret = solution(arr)

print("함수의 반환값은",ret,"입니다.")
'''
#리스트 평탄화 문제
'''
def flatten(date):   #평탄화 함수 정의
    result = []             #결과값 저장할 빈 리스트 
    for item in date:       #for문으로 반복 
        if type(item) == list:      #item의 타입이 리스트이면
            result += flatten(item)  #빈 리스트에 item을 평탄화 해서 저장
        else :                      #타입이 리스트가 아니면
           # result.append(i)
           result += [item]     #빈 리스트에 item만 저장
    return result           #함수 반환

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:",example)
print("변환:",flatten(example))
'''
#문제3 (n과 m은 1이상 1000이하의 자연수, n < m을 항상 만족)
'''
import math

def solution(n,m):
    result = 0
    n,m >= 1 and n,m <= 1000 and n > m
    for i in range(n,m+1):
       if i % 2 == 0:
           result += (i ** 2)
    return result

n=6
m=15
ret = solution(n,m)
print("solution 함수의 반환 값은", ret, "입니다.")
'''

#문제4
#단어들이 들어있는 리스트에서 길이가 5이상인 단어를 리스트에 들어있는 순서대로 이어붙이기
#["my","favorite","color","is","violet"]
#"favoritecolorviolet"
#조건 : 단어들이 들어있는 리스트 words의 길이는 1이상 100이하
#words에 들어있는 각 단어의 길이는 1이상 10이하, 알파벳 소문자로만 이루어짐
#만약 return 할 문자열이 빈 문자열이면 "empty"를 return
def solution(words):





    result = ''
    return result
    


    