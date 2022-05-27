# 2805 나무자르기
# 언어: pypy3 / 메모리 : 260064KB   /   시간 : 504ms   / 코드 길이 : 435B
# 언어: python3 / 메모리 : 148396KB   /   시간 : 3564ms   / 코드 길이 : 492B

'''
이분탐색으로 풀 예정
n: 나무의 수
m: 집에 가져갈 최소 길이
trees: 나무 길이 리스트

이분 탐색할 변수 : 절단기의 높이(=answer)
범위 : 0 <= answer <= max(trees)
'''
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        # pypy3
        # total += max(tree - mid, 0)
        
        # python3
        if tree > mid:
            total += tree - mid
        if total >= m:
            break
    
    if total >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)

'''
pypy3에서는 for문 안에 
total += max(tree - mid, 0)
로 해도 시간 초과 없이 성공

python3에서는 for문 안에
tree > mid 인 경우만 계산하도록 제한하고
total >= m 인 경우 break 걸어주는 조건이 필요
'''