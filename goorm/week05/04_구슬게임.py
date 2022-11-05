import sys
from collections import deque as dq
input = sys.stdin.readline

n, m, k = map(int, input().split())

def game(n, m, k):
	case = ((1, -1), (-1, 1), (0, 0))
	answer = 0
	q = dq([(n, m, 0)])
	
	while q:
		a, b, cnt = q.popleft()
		if cnt > k:
			continue
		
		if a == 0 or b == 0:
			answer += 1
			answer %= 100000007
			continue
		
		for da, db in case:
			if a + da >= 0 and b + db >= 0:
				q.append((a+da, b+db, cnt + 1))
	
	return answer

print(game(n, m, k))