import sys
from copy import deepcopy
from collections import deque as dq
input = sys.stdin.readline

def sink(i, j, n, m, arr):
	d = ((-1, 0), (1, 0), (0, -1), (0, 1))
	
	for di, dj in d:
		I = i + di
		J = j + dj
		if 0 <= I < n and 0 <= J < m and arr[I][J] == 0:
			return True
	return False

def bfs(i, j, arr, visited):
	global n
	global m
	q = dq([(i, j)])
	visited[i][j] = True
	while q:
		ci, cj = q.popleft()
		
		d = ((-1, 0), (1, 0), (0, -1), (0, 1))
		for di, dj in d:
			I = ci + di
			J = cj + dj
			if 0 <= I < n and 0 <= J < m and arr[I][J] == 1 and not visited[I][J]:
				q.append((I, J))
				visited[I][J] = True
	return visited

def countIsland(arr):
	visited = [[False] * m for _ in range(n)]
	cnt = 0
	for i in range(n):
		for j in range(m):
			if not visited[i][j] and arr[i][j] == 1:
				cnt += 1
				visited = bfs(i, j, arr, visited)
	
	return cnt

def solution(n, m, arr):
	day = 0
	all_sinked = [[0] * m for _ in range(m)]
	while True:
		if arr == all_sinked:
			break
		temp = deepcopy(arr)
		for i in range(n):
			for j in range(m):
				if arr[i][j] == 1 and sink(i, j, n, m, arr):
					temp[i][j] = 0

		arr = temp
		day += 1
		if countIsland(arr) >= 2:
			return day
	return -1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, arr))