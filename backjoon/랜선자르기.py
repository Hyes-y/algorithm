# 1654 랜선 자르기
# 언어: python3 / 메모리 : 30840KB   /   시간 : 140ms   / 코드 길이 : 452B
'''
이분탐색
k: 기존 랜선의 개수
n: 필요한 랜선의 개수
lines: 기존 랜선 길이 리스트

이분 탐색할 변수 : 랜선의 최대 길이(=answer)
범위 : 1 <= answer <= max(lines)
'''
from sys import stdin
input = stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

start = 1
end = max(lines)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        if line >= mid:
            total += line // mid
        if total >= n:
            break
    if total >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)

'''
전 문제와 동일하게 start = 0으로 지정했으나
mid = 0 이 되는 경우가 발생하여 zerodivisionerror 발생
=> 랜선의 최솟값이 1이므로 start 또한 1로 지정해서 위 경우 해결 
'''