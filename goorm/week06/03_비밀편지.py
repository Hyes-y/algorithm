import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	s = input().rstrip()
	mode, token = input().split()
	repeated = token * math.ceil(len(s) / len(token))
	answer = ""
	if mode == 'E':
		for origin, key in zip(s, repeated):
			if 97 <= ord(origin) <= 122:
				std = 97
				period = 26
			elif 65 <= ord(origin) <= 90:
				std = 65
				period = 26
			# elif 48 <= ord(origin) <= 57:
			# 	std = 48
			# 	period = 10
			else:
				answer += origin
				continue
			encoded = chr((ord(origin) - std + (ord(key) % period)) % period + std)
			answer += encoded
	elif mode == 'D':
		for encoded, key in zip(s, repeated):
			if 97 <= ord(encoded) <= 122:
				std = 97
				period = 26
			elif 65 <= ord(encoded) <= 90:
				std = 65
				period = 26
			# elif 48 <= ord(encoded) <= 57:
			# 	std = 48
			# 	period = 10
			else:
				answer += encoded
				continue
			decoded = chr((ord(encoded) - std - (ord(key) % period)) % period + std)
			answer += decoded
	
	print(answer)