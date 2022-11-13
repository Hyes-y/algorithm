import sys
input = sys.stdin.readline

for _ in range(5):
	number = input().rstrip()
	
	answer = 0
	for i in range(0, 7, 2):
		answer += int(number[i])
	
	for j in range(1, 7, 2):
		even = int(number[j])
		if even != 0:
			answer = answer * even % 10
		
	print(answer % 10)