# 7662 이중 우선순위 큐
# 메모리 : 51616KB   /   시간 : 260ms   / 코드 길이 : 280B
# 큐
"""
q1: 최소힙
q2: 최대힙
"""
import sys
import heapq as hq
from collections import deque as dq, defaultdict as dd

input = sys.stdin.readline

# 시간초과
# def push(q, val):
#     l = len(q)
#     start = 0
#     end = l
#     idx = 0
#     while start < end:
#         mid = (start + end) // 2
#         if q[mid] <= val:
#             idx = mid + 1
#             start = mid + 1
#         else:
#             end = mid - 1

#     q.insert(idx, val)
    
#     return q


# t = int(input())
# for _ in range(t):
#     qm = []
#     qM = []

#     check = dd(int)
#     n = int(input())
#     for _ in range(n):
#         d = input().split()
#         val = int(d[1])
#         if d[0] == "I":
#             hq.heappush(qm, val)
#             hq.heappush(qM, -val)
#             check[val] += 1
        
#         elif d[1] == "-1":
#             if len(qm) == 0:
#                 continue
#             deleted = hq.heappop(qm)
#             check[deleted] -= 1
        
#         else:
#             if len(qM) == 0:
#                 continue
#             deleted = -hq.heappop(qM)
#             check[deleted] -= 1


#     while qM:
#         v = hq.heappop(qM)
#         if check[-v] != 0:
#             hq.heappush(qM, v)
#             break

#     while qm:
#         v = hq.heappop(qm)
#         if check[v] != 0:
#             hq.heappush(qm, v)
#             break

#     if len(qm) == 0 and len(qM) == 0:
#         print("EMPTY")
#     else:
#         max_val = -hq.heappop(qM)
#         min_val = max_val
#         if len(qM) != 0:
#             min_val = hq.heappop(qm)

#         print(f"{max_val} {min_val}")


# t = int(input())
# for _ in range(t):
#     qm = []
#     qM = []

#     check = dd(bool)
#     idx = 0
#     n = int(input())
#     for _ in range(n):
#         d = input().split()
#         val = int(d[1])
#         if d[0] == "I":
#             hq.heappush(qm, (val, idx))
#             hq.heappush(qM, (-val, idx))
#             check[idx] = True
#             idx += 1
        
#         else:
#             q, nq = qm, qM
#             if d[1] == "1":
#                 q, nq = qM, qm

#             if len(q) == 0:
#                 continue
            
            
#             while q:
#                 _, popped = hq.heappop(q)               
#                 if check[popped]:
#                     check[popped] = False
#                     break

#             while nq:
#                 _, npopped = hq.heappop(nq)
#                 if check[npopped]:
#                     hq.heappush(nq, (_, npopped))
#                     break

#     min_val = False
#     max_val = False

#     while qM:
#         v, popped = hq.heappop(qM)
#         if check[popped]:
#             max_val = -v
#             check[popped] = False
#             break

#     while qm:
#         v, popped = hq.heappop(qm)
#         if check[popped]:
#             min_val = v
#             break
        

#     if not min_val and not max_val:
#         print("EMPTY")
#     elif not min_val or not max_val:
#         val = min_val if min_val else max_val
#         print(f"{val} {val}")
#     else:
#         print(f"{max_val} {min_val}")

t = int(input())
for _ in range(t):
    qm = []
    qM = []

    check = dd(bool)
    idx = 0
    n = int(input())
    for _ in range(n):
        d = input().split()
        val = int(d[1])
        if d[0] == "I":
            hq.heappush(qm, (val, idx))
            hq.heappush(qM, (-val, idx))
            check[idx] = True
            idx += 1
        
        else:
            q = qm
            if d[1] == "1":
                q = qM

            if len(q) == 0:
                continue
            
            while q:
                _, popped = hq.heappop(q)
                if check[popped]:
                    check[popped] = False
                    break

    min_val = False
    max_val = False

    while qM:
        v, popped = hq.heappop(qM)
        if check[popped]:
            max_val = -v
            check[popped] = False
            break

    while qm:
        v, popped = hq.heappop(qm)
        if check[popped]:
            min_val = v
            break
        

    if not min_val and not max_val:
        print("EMPTY")
    elif not min_val or not max_val:
        val = min_val if min_val else max_val
        print(f"{val} {val}")
    else:
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