# 1697 숨바꼭질
# 메모리 : 35476KB   /   시간 : 152ms   / 코드 길이 : 898B 
# BFS
"""
- 메모리 초과로 애먹었던 문제
- Queue에 현재 노드와 지금까지 움직인 거리를 같이 넣어줬던게 메모리 초과의 원인이었던 것 같음
- 거리를 다른 리스트로 빼니까 메모리 초과 해결
"""
import sys
from collections import deque as dq

input = sys.stdin.readline

n, k = map(int, input().split())
maximum = 100001
d = [0] * maximum
visited = [False] * maximum

def BFS(start, end):
    q = dq([])
    q.append(start)
    visited[start] = True
    while q:
        cur = q.popleft()
        if cur == end:
            break

        else:
            if 0 <= cur * 2 <= maximum and not visited[cur*2]:
                q.append(cur * 2)
                visited[cur*2] = True
                d[cur*2] = d[cur] + 1
            if 0 <= cur + 1 <= end and not visited[cur+1]:
                q.append(cur + 1)
                visited[cur+1] = True
                d[cur+1] = d[cur] + 1
            if cur - 1 >= 0 and not visited[cur-1]:
                q.append(cur - 1)
                visited[cur-1] = True
                d[cur-1] = d[cur] + 1           
    return

BFS(n, k)
print(d[k])