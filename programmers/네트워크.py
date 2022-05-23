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


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 2)
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4)