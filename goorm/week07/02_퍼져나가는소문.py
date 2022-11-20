import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())

knowing = [False] * (n+1)
knowing[0:2] = [True, True]

m = int(input())

connected = {i: [] for i in range(1, n+1)}

for _ in range(m):
	a, b = map(int, input().split())
	connected[a].append(b)
	connected[b].append(a)

q = dq([1])

while q:
	cur = q.popleft()
	
	for nxt in connected[cur]:
		if not knowing[nxt]:
			knowing[nxt] = True
			q.append(nxt)

print(knowing.count(True)-1)