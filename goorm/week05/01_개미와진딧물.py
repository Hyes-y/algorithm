import sys
from collections import deque as dq
input = sys.stdin.readline

"""
idea 1. 진딧물에서 m만큼 범위 내에 있는 개미집 수 구하기
기준: 진딧물

시간초과
def bfs(r, c):
	global m
	global n
	answer = 0
	q = dq([(r, c, 0)])
	
	while q:
		cr, cc, cd = q.popleft()
		
		if cd == m:
			continue
		
		for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			R = cr + dr
			C = cc + dc
			if 0 <= R < n and 0 <= C < n:
				if arr[R][C] == 1:
					answer += 1
					arr[R][C] = 0
				q.append((R, C, cd + 1))
				
	return answer

def solution(n, m, arr):
	answer = 0
	for i in range(n):
		for j in range(n):
			if arr[i][j] == 2:
				answer += bfs(i, j)
	return answer
"""

"""
idea 2. 개미집 기준 m 범위 내에 진딧물이 있으면 해당 개미집 수 세기

기준: 개미집

통과 => 
진딧물의 경우 필수적으로 m만큼 확인을 해야하고 진딧물이 많은 경우 의미 없는 탐색이 진행됨.
개미집을 기준으로 하면 최대 m칸이므로 그 안에 진딧물이 있을 수 있고 개미집의 개수를 세는것이므로 
개미집은 반드시 모두 확인해야함.
"""
def bfs(r, c):
	global m
	global n
	visited = [[False] * n for _ in range(n)]
	q = dq([(r, c, 0)])
	visited[r][c] = True
	while q:
		cr, cc, cd = q.popleft()
		
		if cd == m:
			continue
		
		for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			R = cr + dr
			C = cc + dc
			if 0 <= R < n and 0 <= C < n and not visited[R][C]:
				visited[R][C] = True
				if arr[R][C] == 2:
					return 1
				q.append((R, C, cd + 1))
				
	return 0

def solution(n, m, arr):
	answer = 0
	for i in range(n):
		for j in range(n):
			if arr[i][j] == 1:
				answer += bfs(i, j)
	return answer

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, arr))