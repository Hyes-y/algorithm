def solution(n, computers):
    answer = 0
    network = [False for _ in range(n)]
    stack = []
    while True:
        if network == [True for _ in range(n)]:
            break
        for idx, bool in enumerate(network):
            if bool == False:
                key = idx
                break
        stack.append((key, computers[key]))
        while stack:
            idx, is_connected = stack.pop()
            for i in range(n):
                if is_connected[i] == 1 and network[i] == False:
                    network[i] = True
                    stack.append((i, computers[i]))
                else:
                    continue
        answer += 1
    return answer

# 다른 풀이
def solution2(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                
                for k in range(n):
                    if k != node and computers[node][k] == 1 and not visited[k]:
                        visited[k] = True
                        stack.append(k)
            answer += 1
        if False not in visited:
            break
    return answer

# 다른 풀이 2.
def solution3(n, computers):
    visited = [i for i in range(n)]

    def find(node):
        if visited[node] != node:
            visited[node] = find(visited[node])
        return visited[node]

    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if computers[i][j] == 1:
                p_i = find(i)
                p_j = find(j)
                if p_i < p_j:
                    # visited[j] = p_i
                    visited[p_j] = p_i
                elif p_i > p_j:
                    # visited[i] = p_j
                    visited[p_i] = p_j
    
    for i in range(n):
        visited[i] = find(i)
    # print(visited)      
    return len(set(visited))




print(solution3(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution3(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution3(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 2)
print(solution3(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
print(solution3(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4)
print(solution3(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]), 1) # 7, 9번 테스트케이스?