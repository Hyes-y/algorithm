import sys
from itertools import permutations as pm
input = sys.stdin.readline

n = int(input())
arr = list(input().split())

min_val = 9998979695949393
for case in list(pm(arr, n)):
	string = ""
	for i in range(n):
		if string != "" and string[-1] == case[i][0]:
			string += case[i][1]
		else:
			string += case[i]
	
	if min_val > int(string):
		min_val = int(string)
	
print(min_val)