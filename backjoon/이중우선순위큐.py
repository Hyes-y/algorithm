# 7662 이중 우선순위 큐
# 메모리 : 51616KB   /   시간 : 260ms   / 코드 길이 : 280B
# 큐
"""
q1: 최소힙
q2: 최대힙
"""
import sys
import heapq as hq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    q1 = []
    q2 = []
    check = {}
    n = int(input())
    for _ in range(n):
        d = input().split()
        val = int(d[1])
        if d[0] == "I":
            if val not in check:
                check[val] = 0
            check[val] += 1
            hq.heappush(q1, val)
            hq.heappush(q2, -val)

        
        elif d[1] == "-1":
            if len(q1) == 0:
                continue
            hq.heappop(q1)
            check[val] -= 1

        
        else:
            if len(q2) == 0:
                continue
            hq.heappop(q2)
            check[val] -= 1


    if len(q1) == 0:
        print("EMPTY")
    else:
        min_val = 0
        max_val = 0
        
        q2.pop()
        max_val = -hq.heappop(q2) if len(q2) > 0 else min_val
        
        print(f"{max_val} {min_val}")


"""
테스트 케이스
1
9
D -1
D -1
I 8088
D 1
I 5585
I 9097
I -6416
D 1
D -1

5585 5585
"""