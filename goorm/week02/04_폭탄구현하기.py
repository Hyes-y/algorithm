def solution():
	d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	n, k = map(int, input().split())
	# bomb_map = [[0] * n for _ in range(n)]
	result = 0
	for _ in range(k):
		i, j = map(lambda x: int(x)-1, input().split())
		result += 1
		# bomb_map[i][j] += 1
		for di, dj in d:
			I = i + di
			J = j + dj
			if 0 <= I < n and 0 <= J < n:
				# bomb_map[I][J] += 1
				result += 1
			else:
				continue
	# result = sum([sum(bomb_map[i]) for i in range(n)])
	print(result)
	return

solution()

"""
1 <= n <= 20
1 <= k <= 500000
1 <= a <= n
1 <= b <= n
arr[a][b] : 폭탄 투하 위치

test case
input[1]:
3 3
3 3
3 3
1 1
output[1]:
9

input[2]:
4 4
1 1
4 4
3 3
2 4
output[2]:
15

"""