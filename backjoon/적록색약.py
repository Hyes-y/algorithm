# 10026 적록색약
# 메모리 : 32468KB   /   시간 : 120ms   / 코드 길이 : 926B
import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
picture = [list(input().rstrip()) for _ in range(n)]

def bfs(i, j, color):
    q = dq([(i, j)])
    
    while q:
        r, c = q.popleft()

        if visited[r][c]:
            continue

        visited[r][c] = True

        for dr, dc in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            R = r + dr
            C = c + dc

            if 0 <= R < n and 0 <= C < n \
                and picture[R][C] in color\
                and not visited[R][C]:
                q.append((R, C))

answer = []
for c in ("N", "RG"):
    areas = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                color = picture[i][j] if picture[i][j] not in c else c
                bfs(i, j, color)
                areas += 1
    answer.append(areas)

print(*answer)