# def partial(n):
#     return n*(1 + n) // 2

# def dummy(n, arr):
#     loc = []
#     cnt = 0
#     serial = False
#     for el in arr:
#         if el >= n and serial:
#             cnt += 1
#         elif el < n and serial:
#             loc.append(cnt)
#             cnt = 0
#             serial = False
#         elif el >= n and not serial:
#             cnt += 1
#             serial = True
#     loc.append(cnt)
#     return loc


# def solution(H):
#     rectangle_cnt = {x:0 for x in set(H)}

#     for h in sorted(rectangle_cnt.keys(), reverse=True):
#         a = dummy(h, H)
#         b = dummy(h+1, H)
#         print(a)
#         print(b)
#         if len(a) == 0:
#             continue
#         else:
#             for i in a:
#                 rectangle_cnt[h] += partial(i)
            
#             if len(b) == 0:
#                 continue
#             else:
#                 for j in b:
#                     rectangle_cnt[h] -= partial(j)
    

#     answer = [[key, value] for key, value in sorted(rectangle_cnt.items(), key=lambda x:x[0])]

#     return answer



# H = [3, 2, 1, 1, 3]

# print(solution(H))

# # print(dummy(1, H))
# # print(dummy(2, H))


def partial(n):
    return n*(1 + n) // 2

def dummy(n, arr):
    loc = []
    cnt = 0
    serial = False
    for el in arr:
        if el >= n and serial:
            cnt += 1
        elif el < n and serial:
            loc.append(cnt)
            cnt = 0
            serial = False
        elif el >= n and not serial:
            cnt += 1
            serial = True
    loc.append(cnt)
    
    return loc


def solution(H):
    rectangle_cnt = {x:0 for x in set(H)}

    for h in sorted(rectangle_cnt.keys(), reverse=True):
        a = dummy(h, H)
        b = dummy(h+1, H)
        if len(a) == 0:
            continue
        else:
            for i in a:
                rectangle_cnt[h] += partial(i)
            
            if len(b) == 0:
                continue
            else:
                for j in b:
                    rectangle_cnt[h] -= partial(j)
    

    answer = [[key, value] for key, value in sorted(rectangle_cnt.items(), key=lambda x:x[0])]

    return answer

H = [3, 2, 1, 1, 3]

print(solution(H))


print(abs(-3))