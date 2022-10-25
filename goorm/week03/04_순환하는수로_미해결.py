import sys
sys.setrecursionlimit(1000000)
n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

visited = [False] * (n+1)
cycle = []
finded = -1

def dfs(node, prev):
	global finded
	if visited[node]:
		finded = node
		if node not in cycle:
			cycle.append(node)
		return

	visited[node] = True
	
	for idx, val in enumerate(graph[node]):
		if val == 0 or idx == prev:
			continue
		dfs(idx, node)
		if finded == -2:
			return

		if finded == node:
			finded = -2
			return
		if finded >= 0:
			if node not in cycle:
				cycle.append(node)
			return
				

# for i in range(1, n+1):
# 	if graph[i] != [0] * (n+1):
# 		dfs(i, 0)
# 		break
dfs(1, 1)

print(cycle)
print(*cycle)

"""
test case
5
5 2
2 4
4 3
3 1
1 2

4
1 2 3 4 
--
6
1 3
3 4
4 5
5 6
6 2
1 5

4
1 3 4 5 
--
5
2 5
5 3
3 1
1 4
4 5

4
1 3 4 5
--
6
1 2
3 2
3 4
5 4
5 6
6 3

4
3 4 5 6
"""