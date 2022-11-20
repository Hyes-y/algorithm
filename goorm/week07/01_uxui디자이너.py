import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {i: 0 for i in range(1, n+1)}

for _ in range(m):
	events = list(map(int, input().split()))[1:]
	
	for event in events:
		dic[event] += 1
	
max_val = max(dic.values())

answers = [idx for idx, val in dic.items() if val == max_val]
print(*sorted(answers, reverse=True))