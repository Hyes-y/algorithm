import sys
import copy
from collections import deque as dq
input = sys.stdin.readline

n = int(input())

area = [list(map(int, input().split())) for _ in range(n)]
changed = copy.deepcopy(area)

all_changed = [[0] * n for _ in range(n)]
day = 0
while area != all_changed:
    for i in range(n):
        for j in range(n):
            if area[i][j] != 0:
                cnt = 0
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    r = i + di
                    c = j + dj
                    if 0 <= r < n and 0 <= c < n:
                        if area[r][c] == 0:
                            cnt += 1
                if area[i][j] <= cnt:
                    changed[i][j] = 0
                else:
                    changed[i][j] -= cnt

    area = copy.deepcopy(changed)
    day += 1

print(day)