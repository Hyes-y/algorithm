# # 11728 배열 합치기
# # 메모리 : 185016KB   /   시간 : 2112ms   / 코드 길이 : 248B
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# answer = a + b
# answer.sort()

# for i in range(n+m):
#     if i == n+m-1:
#         print(answer[i])
#     else:    
#         print(answer[i], end=' ')



# # 2167 2차원 배열의 합
# # 메모리 : 128428KB   /   시간 : 3520ms   / 코드 길이 : 422B / 언어 : PyPy3

# import sys

# n, m = map(int, input().split())

# arr = []
# answer_list = []

# for _ in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))

# k = int(input())

# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     total = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             total += arr[i][j]
#     answer_list.append(total)

# for answer in answer_list:
#     print(answer)



# # 17140 2차원 배열과 연산
# # 메모리 : 128428KB   /   시간 : 3520ms   / 코드 길이 : 422B / 언어 : PyPy3