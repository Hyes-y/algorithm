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

"""
풀이
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
park = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    trees = list(map(int, input().split()))
    for j in range(1, N + 1):
        park[i][j] = trees[j - 1]
        
def isColored():
    global park, N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if park[i][j]:
                return 0
    return 1

if isColored():
    print(0)
    exit(0)
        
update = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
day = 1

while 1:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if ni < 1 or nj < 1 or ni > N or nj > N:
                    continue
                if not park[ni][nj]:
                    update[i][j] += 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            park[i][j] = max(0, park[i][j] - update[i][j])
                
    if isColored():
        break

    day += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            update[i][j] = 0

print(day)
"""