"""
test case
3
5

10000
11034287
"""
from itertools import combinations as cb


cur = 3
cnt = 1

for i in range(cur * 2, 2, -2):
    cnt *= i * (i-1)
    cnt //= 2
    cnt //= i // 2
cnt //= 3
print(cnt % 100000007)