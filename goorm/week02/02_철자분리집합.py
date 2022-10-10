def solution(n:int, s:str) -> int:
	if n == 1:
		return 1
	
	cur = s[0]
	result = 1
	for i in range(1, n):
		if s[i] != cur:
			cur = s[i]
			result += 1
	
	return result

n = int(input())
s = input()

print(solution(n, s))

"""
test case
input[1]:
5
goorm
output[1]:
4

input[2]:
9
algorithm
outuput[2]:
9
"""