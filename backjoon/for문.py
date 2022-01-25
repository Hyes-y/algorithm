# # 2739 입력받은 수 의 구구단을 출력
# # 메모리 : 30864KB   /   시간 : 72ms   / 코드 길이 : 73B

n = int(input())

for i in range(1, 10):
    print(f'{n} * {i} = {n*i}')


# # 10950 입력받은 여러 쌍의 두 정수의 합을 출력
# # 메모리 : 30864KB   /   시간 : 76ms   / 코드 길이 : 148B

n = int(input())
answer = []
for _ in range(n):
    a, b = map(int, input().split())
    answer.append(a+b)

for _ in range(n):
    print(answer[_])




# # 15552 입력받은 n 쌍의 두 정수의 합을 출력(n이 큰 경우)
# # 메모리 : 68804KB   /   시간 : 1536ms   / 코드 길이 : 187B


import sys

n = int(sys.stdin.readline())

answer = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    answer.append(a+b)

for _ in range(n):
    print(answer[_])




