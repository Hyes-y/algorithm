# 1927 최소힙
# 메모리 : 30764KB   /   시간 : 148ms   / 코드 길이 : 242B
# 최소힙 구현

import heapq as hq
import sys

input = sys.stdin.readline

h = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        min_val = hq.heappop(h) if h else 0
        print(min_val)
    else:
        hq.heappush(h, x)

