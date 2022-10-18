n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

visited = [0] * (n+1)
finished = [False] * (n+1)
order = 0
cycle = 0
def dfs(node):
	global order
	global cycle
	order += 1
	visited[node] = order
	
	for idx, val in enumerate(graph[node]):
		if val == 0:
			continue
			
		if visited[idx] == 0:
			graph[idx][node] = 0
			if graph[idx] == [0] * (n+1):
				continue
			dfs(idx)
		elif not finished[idx]:
			cycle = (node, idx)
			break
		else:
			visited[order] = 0
	finished[node] = True

for i in range(1, n+1):
	if graph[i] != [0] * (n+1):
		dfs(i)
		break

print(cycle)
print(visited)
print(finished)
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