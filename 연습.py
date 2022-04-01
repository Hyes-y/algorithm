# H = [1, 3, 5, 3, 4, 5, 2]
# rectangle_cnt = {x:0 for x in set(H)}
# for h in sorted(rectangle_cnt.keys(), reverse=True):
#     print(h)

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
        
    
    return loc


print(dummy(2, [3, 3, 2, 3, 4, 3, 1, 4, 2]))

# rectangle_cnt = {2:2, 1:11, 3:2}
# answer = [[key, value] for key, value in sorted(rectangle_cnt.items(), key=lambda x:x[0])]

# print(answer)



# point = 0
#         check = False
#         for i in range(len(H)):
#             if h > H[i] and not check:
#                 point = i
#                 continue
#             elif h > H[i] and check:
#                 partial_list = H[point:i]
#                 total = partial(len(partial_list))
#                 for part in dummy(h, partial_list):
#                     total -= partial(part)
#                 rectangle_cnt[h] += total
#             else:
#                 check=True
#                 if h < H[i]: