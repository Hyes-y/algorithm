# 1417 국회의원 선거
# 메모리 : 32908KB   /   시간 : 76ms   / 코드 길이 : 384B

import heapq as hq

def solution():
    n = int(input())
    dasom = int(input())
    heap = []
    for _ in range(n-1):
        hq.heappush(heap, -int(input()))

    cnt = 0
    if len(heap) == 0:
        return 0

    while dasom <= -heap[0]:
        a = -hq.heappop(heap)
        hq.heappush(heap, -(a-1))
        dasom += 1
        cnt += 1
    
    return cnt


print(solution())
    