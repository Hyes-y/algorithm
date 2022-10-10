def solution():
	n, k = map(int, input().split())
	d = []
	for _ in range(n):
		name, height = input().split()
		d.append((name, height))
	d.sort(key=lambda x:(x[0], float(x[1])))
	print(*d[k-1], sep=" ")
	return

solution()

"""
test case
input[1]:
5 1
goorm 110.40
goormee 111.50
goormy 109.50
oscar 100.00
henry 200.00
output[1]:
goorm 110.40

input[2]:
5 5
abcabc 120.00
abcabca 120.00
abcabcb 120.00
abcabcc 120.00
abcabcd 120.00
output[2]:
abcabcd 120.00
"""