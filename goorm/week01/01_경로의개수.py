"""
[알고리즘 먼데이 챌린지 - 1주차] 01. 경로의 개수

문제 >
n개의 섬이 있을 때 
i번째 섬은 i+1번째 섬과 다리를 통해 연결되어 있고 i -> i+1 의 이동만 가능하며
i -> i+1 을 연결하는 다리가 k개라면 i -> i+1 을 갈 수 있는 경로는 k개이다.
(n번째 섬은 1번 섬으로 갈 수 있다.)

이때, 1번 섬부터 다시 1번 섬까지 올 수 있는 경로의 수를 구해라!

idea>
i번째에서 i+1번째 섬으로 갈 수 있는 다리의 개수가 주어지니
다 곱해버리자!
"""
def solution(n, bridges):
	answer = 1
	for val in bridges:
		answer *= val
	return answer

n = int(input())
bridges = list(map(int, input().split()))

print(solution(n, bridges))
