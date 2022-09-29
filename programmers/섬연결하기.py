# 그리디
# 문제 > https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 섬 연결하기
"""
idea > 최소 신장 트리를 구하는 알고리즘으로 풀기
- 프림 알고리즘이란 최소 신장 트리(MST, 간선들의 가중치의 합이 최소)를 구하는 알고리즘 중 하나로
적은 가중치의 간선을 선택하되, 연결된 정점들과 연결된(?) 간선들 중에서 가장 적은 가중치를 고르면서 범위를 확장하는 방식

- 크루스칼 알고리즘은 최소 신장 트리(MST, 간선들의 가중치의 합이 최소)를 구하는 알고리즘 중 하나로
그냥 가장 적은 가중치 간선을 차례대로 선택하는 방법 (이 때 사이클을 만드는 간선은 선택에서 제외한다.)

알고리즘 참고: 
https://ongveloper.tistory.com/376
https://chanhuiseok.github.io/posts/algo-33/
https://techblog-history-younghunjo1.tistory.com/262
"""
# solve 1. 프림 알고리즘
import heapq as hq

def solution_prim(n, costs):
    answer = 0
    connected = [False] * n
    cost_map = [[0] * n for _ in range(n)]
    costs.sort(key=lambda x: x[2])
    for cost in costs:
        cost_map[cost[0]][cost[1]] = cost[2]
        cost_map[cost[1]][cost[0]] = cost[2]
        
    q = [(costs[0][2], costs[0][0], costs[0][1])]
    while connected != [True] * n:
        cost, a, b = hq.heappop(q)
        if connected[a] and connected[b]:
            continue
        else:
            connected[a] = True
            connected[b] = True
            answer += cost
            
            connected_nodes = [i for i, _ in enumerate(connected) if _]
            for idx in connected_nodes:
                for i, val in enumerate(cost_map[idx]):
                    if not connected[i] and val != 0:
                        hq.heappush(q, (val, idx, i))
            
    return answer


# solve 2. 크루스칼 알고리즘
def get_parents(node, parents):
    if parents[node] == node:
        return node
    else:
        return get_parents(parents[node], parents)

def solution_kruskal(n, costs):
    answer = 0
    connected = 0
    parents = [i for i in range(n)]
    costs = [(cost[2], cost[0], cost[1]) for cost in costs]
    costs.sort(key=lambda x: x[0])

    for cost, a, b in costs:
        a_parents = get_parents(a, parents)
        b_parents = get_parents(b, parents)
        if a_parents != b_parents:
            answer += cost
            parents[a_parents] = b
            connected += 1
              
    return answer