# 2606 바이러스
# 메모리 : 30840KB   /   시간 : 68ms   / 코드 길이 : 521B
import sys

input = sys.stdin.readline

n = int(input())
c_map = {i: [] for i in range(1, n+1)}
m = int(input())

for _ in range(m):
    key, value = map(int, input().split())
    c_map[key].append(value)
    c_map[value].append(key)

stack = [1]
visited = [0 for _ in range(n + 1)]
while stack:
    cur = stack.pop()
    for connected in c_map[cur]:
        if visited[connected] == 1:
            continue
        else:
            visited[connected] = 1
            stack.append(connected)

print(visited[2:].count(1))