"""
[알고리즘 먼데이 챌린지 - 1주차] 04. 소수 찾기

문제 >
n개의 숫자를 가진 배열이 주어졌을 때,
배열에서 '소수'번째에 있는 값을 모두 더한 값을 반환해라!

idea>
- n까지 소수를 모두 구한 후
- 소수를 인덱스로 하는 배열의 값을 다 더함
=> 리스트 인덱스는 0번부터 시작하므로 구한 소수에서 -1을 해준 후 값에 접근
"""
def prime(n):
	prime_dict = {i: True for i in range(2, n+1)}
	for i in range(2, int(n ** 0.5) + 1):
			if i in prime_dict:
					for j in range(2, (n + 1) // i + 1):
							if i*j in prime_dict:
									del prime_dict[i*j]

	return list(prime_dict.keys())

def solution(n:int, A:list) -> int:
	answer = 0
	prime_list = prime(n)
	
	for i in prime_list:
		answer += A[i-1]
		
	return answer

n = int(input())
A = list(map(int, input().split()))

print(solution(n, A))