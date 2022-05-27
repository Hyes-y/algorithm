# 18111 마인크래프트
# 언어: pypy3 / 메모리 : 117484KB   /   시간 : 908ms   / 코드 길이 : 822B
'''
땅고르기를 해야함
n: row
m: col
b: 잉여 블록

출력: 최소시간, 그때 땅의 높이(여러개일 경우 최댓값)

1> 실패
높이 = 
전체 합 // 칸 수
or
전체 합 // 칸 수 + 1  (전체 합 % 칸 수 만큼 inventory에 있을때) 
=> 문제에 나와있는 케이스만 가능, 너무 짧은 생각 ㅎ

2> 성공: brute force로 0~256까지 모든 높이에 대한 계산
=> 잉여 블록으로도 해당 높이를 만들지 못하는 순간 break를 해줘야 시간 초과가 안남
=> heapq, .. 다양한 방법으로 해봄ㅋㅋ
=> 처음에 for문 안에서 time에 대한 연산이 없는 경우에도 break를 해줬으나 이런 경우 node가 한개이거나 변함 없어도 될때 처리가 안됨

3> Python3으로도 해결할 정도로 시간 복잡도 개선하기
'''
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
values = []
min_time = 99999999
max_height = 0
for v in range(257):
    time = 0
    rest_block = b

    for i in range(n):
        for j in range(m):
            if ground[i][j] == v:
                continue
            elif ground[i][j] > v:
                time += 2 * (ground[i][j] - v)
                rest_block += ground[i][j] - v
            else: 
                time += 1 * (v - ground[i][j])
                rest_block -= v - ground[i][j]
    if rest_block < 0:
        break
    elif min_time == time: 
        max_height = max(max_height, v)
    elif min_time > time:
        min_time = time
        max_height = v

time, height = min_time, max_height
print(time, height)

