"""
[알고리즘 먼데이 챌린지 - 1주차] 02. 동명이인

문제 >
찾아야 할 이름이 주어졌을때,  n개의 이름 중 찾아야 할 이름이 포함된 이름의 개수를 구해라!

idea>
'in'을 이용해 찾자!
"""
def solution(n:str, name:str) -> int:
	n = int(n)
	answer = 0
	for _ in range(n):
		another_name = input()
		if name in another_name:
			answer += 1
	
	return answer

n, name = input().split()

print(solution(n, name))
