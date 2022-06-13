# 1012 유기농 배추
# 메모리 : 30840KB   /   시간 : 80ms   / 코드 길이 : 1184B
'''
<input>
t : test case 수
m, n, k : 배추밭 가로, 세로, 배추가 심어져 있는 위치의 개수
x1, y1
x2, y2 ...
---

idea > 각 좌표를 1로 표현한 배추밭을 정의하고 네 방향(상하좌우)의 dx, dy를 정의한 후 풀이는 dfs로

'''
import sys
input = sys.stdin.readline

def dfs(loc_map, loc_list, m, n):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    for i in range(k):
        X, Y = loc_list[i]
        if visited[X][Y] == True:
            continue
        cnt += 1
        stack = [(X, Y)]
        while stack:
            x, y = stack.pop()
            for dx, dy in d:
                move_x = x + dx
                move_y = y + dy
                if move_x < 0 or move_y < 0 or move_x >= m or move_y >= n:
                    continue
                elif loc_map[move_x][move_y] == 1 and not visited[move_x][move_y]:
                    visited[move_x][move_y ]= True
                    stack.append((move_x, move_y))
                else:
                    continue
    return cnt

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().rstrip().split())
    cnt = 0
    loc_map = [[0] * n for _ in range(m)]
    loc_list = []
    
    for i in range(k):
        x, y = map(int, input().rstrip().split())
        loc_map[x][y] = 1
        loc_list.append((x, y))
    
    cnt = dfs(loc_map, loc_list, m, n)
    print(cnt)
        
