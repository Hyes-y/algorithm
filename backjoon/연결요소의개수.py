# 11724 연결 요소의 개수
# 메모리 : 68548KB   /   시간 : 872ms   / 코드 길이 : 767B   / DFS(stack)
# 메모리 : 64848KB   /   시간 : 760ms   / 코드 길이 : 577B   / DFS(Recursion)
# DFS 구현
"""
stack보다 재귀 풀이가 적은 시간 소요
재귀 풀이의 경우 recursionlimit을 풀어주지 않으면 통과 안됨

재귀 풀이에서 방문 처리를 할 때 
- visited에 방문한 노드를 추가 (visited.append(node))
- n+1 크기의 배열 visited에 방문한 노드 T/F로 표현(visited[node])

두 가지로 해보았는데 

첫 번째 방식은 이후 방문한 노드를 확인할 때 in 연산자를 사용하다보니(내 생각)
시간이 5820ms 걸림 ㅠㅠ
두 번째 방식(배열 인덱스 T/F로 방문 처리)이 적합한 듯
"""

import sys
sys.setrecursionlimit(10000)    # 재귀 풀이할 때 필요
input = sys.stdin.readline

def DFS(graph, n, start):
    visited = [False] * (n+1)
    visited[0] = True
    answer = 0
    for i in range(start, n+1):
        if visited[i]:
            continue
        
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True

            for c_node in graph[node]:
                if not visited[c_node]:
                    stack.append(c_node)        
        answer += 1
    return answer


def DFS2(start, visited=[]):
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            DFS2(node, visited)     
    
    return visited

n, m = map(int, input().split())

graph = {i+1: [] for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 용 풀이
print(DFS(graph, n, 1))

# DFS2 용 풀이
answer = 0
visited = [False] * (n+1)
for k in range(1, n+1):
    if visited[k]:
        continue
    visited = DFS2(k, visited)
    answer += 1
print(answer)