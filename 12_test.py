scores = [85,72,90,60,45,77,80,95,50,88]
passing_score = 60
failing_score = 50

for score in scores:
    if score < failing_score:
        print(f"학생이 탈락했습니다. 점수 : {score}")
        break
    if score < passing_score:
        print(f"학생이 추가 보충 수업이 필요합니다. 점수 : {score}")
        continue
    print(f"학생이 합격했습니다. 점수 : {score}")