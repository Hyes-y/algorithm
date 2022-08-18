# 7576 토마토
# 메모리 : 153920KB   /   시간 : 3184ms   / 코드 길이 : 1311B
# BFS

from collections import deque as dq

m, n = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(n)]
days = [[0] * m for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ripe = []

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            ripe.append((i, j))

def check(r, c):
    locs = []
    for k in range(4):
        dr, dc = d[k]
        if 0 <= r + dr < n and 0 <= c + dc < m:
            locs.append((r+dr, c+dc))

    return locs


def BFS(ripe):
    q = dq(ripe)

    while q:
        cur_r, cur_c = q.popleft()

        next_day = days[cur_r][cur_c] + 1

        locs = check(cur_r, cur_c)

        if len(locs) == 0:
            continue
        else:
            for next_r, next_c in locs:
                if tomatoes[next_r][next_c] == -1:
                    continue

                elif tomatoes[next_r][next_c] == 1 and days[next_r][next_c] <= next_day:
                    continue

                else:
                    q.append((next_r, next_c))
                    days[next_r][next_c] = next_day
                    tomatoes[next_r][next_c] = 1
    return


BFS(ripe)

max_val = 0
for i in range(n):
    if 0 in tomatoes[i]:
        max_val = -1
        break
    max_val = max(max_val, max(days[i]))

print(max_val)
