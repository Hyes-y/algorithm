# 2021 dev-matching 상반기 : 웹 백엔드 개발자 
# 행렬 테두리 회전하기
# 최소값 저장을 위한 min_value 설정을 100(지맘대로ㅠ) 으로 해서 테스트 통과 못함
# 최소값은 행렬이 가질 수 있는 최댓값 (rows * columns) + 1 로 설정 

def solution(rows, columns, queries):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i*columns + j + 1)
        matrix.append(row)

    min_values = []
    for query in queries:
        x1, y1, x2, y2 = [x-1 for x in query]
        temp = matrix[x1][y1]
        min_value = rows * columns + 1
        for j in range(y1+1, y2+1):
            cur = matrix[x1][j]
            matrix[x1][j] = temp
            temp = cur
            min_value = min(min_value, temp)

        for i in range(x1+1, x2+1):
            cur = matrix[i][y2]
            matrix[i][y2] = temp
            temp = cur
            min_value = min(min_value, temp)

        for j in range(y2-1, y1-1, -1):
            cur = matrix[x2][j]
            matrix[x2][j] = temp
            temp = cur
            min_value = min(min_value, temp)

        for i in range(x2-1, x1-1, -1):
            cur = matrix[i][y1]
            matrix[i][y1] = temp
            temp = cur
            min_value = min(min_value, temp)

        min_values.append(min_value)
    return min_values
