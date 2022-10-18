import sys
import heapq as hq
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [k + 1] * (n + 1)
for _ in range(m):
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1
	
q = [(0, 1)]
visited[1] = 0
while q:
	dist, node = hq.heappop(q)
	if visited[node] < dist:
		continue
		
	for i, b in enumerate(graph[node]):
		if b == 1:
			if dist + 1 <= k and dist + 1 < visited[i]:
				visited[i] = dist + 1
				hq.heappush(q, (dist + 1, i))

if visited[n] <= k:
	print("YES")
else:
	print("NO")