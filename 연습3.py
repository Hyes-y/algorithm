# sk ict 1번

# def solution(money, costs):
#     answer = 0
#     current = [1, 5, 10, 50, 100, 500]
#     valuable_current = {current[i]:costs[i] for i in range(len(costs)) if i == 0 or costs[i-1] * 5 >= costs[i]}
#     for current, value in sorted(valuable_current.items(), reverse=True):
#         max_cnt = money // current
#         answer += max_cnt * value
#         money = money % current
    
#     return answer


# print(solution(4578, [1, 4, 99, 35, 50, 1000]))


# sk ict 2번
import math
from collections import deque

def direction(n, clockwise):
    d = deque([[0, 1], [1, 0], [0, -1], [-1, 0]]) if clockwise else deque([[1, 0], [0, 1], [-1, 0], [0, -1]])
    dcorner = [[0, 0], [0, n-1], [n-1, n-1], [n-1, 0]] if clockwise else [[0, 0], [n-1, 0], [n-1, n-1], [0, n-1]]
    return d, dcorner

def solution(n, clockwise):
    d, dcorner = direction(n, clockwise)
    answer = [[0] * n for _ in range(n)]
    
    rot = 0
    direct = 0
    num = 1
    max_num = math.ceil(n**2 / 4)
    direct_cnt = n - 1
    check = n - 1
    i, j = dcorner[0]
    while True:
        if rot == 3 and num > max_num:
            break
        if num > max_num:
            check = n - 1
            direct_cnt = check
            d.rotate(-1)
            rot += 1
            num = 1
            i, j = dcorner[rot]
            continue

        if num == direct_cnt:
            check -= 2
            direct_cnt += check if check > 1 else 1
            
            direct = (direct + 1) % 4
            continue

        print(rot, d, direct, direct_cnt, i, j, num, max_num)
        answer[i][j] = num
        i, j = i + d[direct][0], j + d[direct][1]
        num += 1

    
    return answer


print(solution(6, False))