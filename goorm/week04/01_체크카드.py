import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())

cur = n
q = dq([])

for _ in range(m):
	transaction = input().split()
	amount = int(transaction[1])
	
	if transaction[0] == "deposit":
		cur += amount
	
	elif transaction[0] == "pay":
		if cur >= amount:
			cur -= amount

	elif transaction[0] == "reservation":
		if not q and cur >= amount:
			cur -= amount
		else:
			q.append(amount)
		
	while q and cur >= q[0]:
		cur -= q.popleft()

while q and cur >= q[0]:
	cur -= q.popleft()
print(cur)