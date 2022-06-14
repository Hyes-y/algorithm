# 1260 DFS와 BFS
# 메모리 : 38708KB   /   시간 : 284ms   / 코드 길이 : 1150B
import sys
from collections import deque as dq

def DFS(n, graph, v):
    visited = [False] * (n+1)
    order = []
    stack = [v]
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        order.append(cur)
        visited[cur] = True
        for idx in range(n, 0, -1):
            val = graph[cur][idx]
            if val == 1 and not visited[idx]:
                stack.append(idx)
        
    return order

def BFS(n, graph, v):
    visited = [False] * (n+1)
    order = []
    q = dq([v])
    while q:
        cur = q.popleft()
        if visited[cur]:
            continue
        order.append(cur)
        visited[cur] = True
        for idx in range(1, n+1):
            val = graph[cur][idx]
            if val == 1 and not visited[idx]:
                q.append(idx)
        
    return order

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1


print(DFS(n, graph, v))
print(BFS(n, graph, v))