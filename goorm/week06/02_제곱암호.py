import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

answer = ""
for i in range(0, n, 2):
	cnt = int(s[i+1]) ** 2
	decoding = chr((ord(s[i]) - ord('a') + cnt) % 26 + ord('a'))
	answer += decoding

print(answer)