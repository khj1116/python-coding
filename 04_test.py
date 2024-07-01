#2차원 리스트를 정의합니다.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#찾을 값을 정의 합니다.
goal = 8
#값이 발견되었는지 여부를 추적
found = False

#2차원 리스트 탐색
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == goal:
            print(f"값 {goal}을(를) 찾았습니다! 위치 : ({i}, {j})")
            found = True
            break
        
    