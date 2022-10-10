def solution():
	t = int(input())
	
	for _ in range(t):
		n = int(input())
		scores = list(map(int, input().split()))
		
		avg = sum(scores) / n
		
		rank = list(filter(lambda x: x >= avg, scores))
		print(f"{len(rank)}/{n}")
	
	return

solution()

"""
test case
input[1]:
2
3
1 3 7
1
5 
output[1]:
1/3
1/1

input[2]:
2
5
1 2 3 4 5
4
1 10 10 10
output[2]:
3/5
3/4
"""