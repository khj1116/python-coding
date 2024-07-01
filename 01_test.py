#univ_score = float(input("점수를 입력해주세요. : "))
#if univ_score >= 90:
    #print("A")
#elif univ_score >= 80:
    #print("B")
#elif univ_score >= 70:
    #print("C")
#elif univ_score >= 60:
    #print("D학점이하는 재수강이 필요합니다. ")
#else:
   # print("F")
   
year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2024 - year +1
elif age_type == "Year":
    answer = 2024 - year
print(answer)