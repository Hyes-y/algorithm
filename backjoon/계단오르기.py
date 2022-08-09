# 2579 계단 오르기
# 메모리 : 30840KB   /   시간 : 72ms   / 코드 길이 : 358B
# 미세하게 top down보다 bottom up이 빠름

import sys

input = sys.stdin.readline

n = int(input())

table = [0] * (n+1)
steps = [int(input()) for _ in range(n)]

def bottomup():
    if n >= 1:
        table[1] = steps[0]

    if n >= 2:
        table[2] = max(steps[0] + steps[1], steps[1])

    if n >= 3:
        for i in range(3, n + 1):
            table[i] = max(steps[i-2]+ table[i-3], table[i-2]) + steps[i-1]

    return table[n]

print(bottomup())


def topdown(x):
    if x == 0:
        return 0

    if x == 1:
        return steps[0]
    
    if x == 2:
        return max(steps[0] + steps[1], steps[1])
    
    if table[x] != 0:
        return table[x]
    
    table[x] = max(topdown(x-3) + steps[x-2], topdown(x-2)) + steps[x-1]
    return table[x]

print(topdown(n))