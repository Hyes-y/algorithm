"""
[알고리즘 먼데이 챌린지 - 1주차] 03. 최장 맨해튼 거리

문제 >
4개의 정수가 주어졌을 때 해당 정수로 만들 수 있는 최장 맨해튼 거리를 구해라!

idea>
순서에 상관 없이 2개씩 짝 지은후 거리를 계산
combinations 를 써도 되지만 정수 개수가 적으므로(4개) 직접 구하기
"""
def solution(nums:list) -> int:
	answer = 0
	case = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]
	
	for x1, x2, y1, y2 in case:
		temp = abs(nums[x1] - nums[x2]) + abs(nums[y1] - nums[y2])
		answer = max(answer, temp)
	
	return answer

nums = list(map(int, input().split()))
print(solution(nums))