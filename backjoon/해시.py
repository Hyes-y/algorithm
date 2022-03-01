# # 9375 패션왕 신해빈
# # 메모리 : 30860KB   /   시간 : 68ms   / 코드 길이 : 451B

# import sys

# n = int(sys.stdin.readline())

# for _ in range(n):
#     item_dict = {}
#     cnt = int(sys.stdin.readline())
#     for _ in range(cnt):
#         item, category = sys.stdin.readline().rstrip().split(' ')
#         if category in item_dict:
#             item_dict[category] += 1
#         else:
#             item_dict[category] = 1

#     answer = 1

#     for key, value in item_dict.items():
#         answer *= (value + 1)

#     answer -= 1
#     print(answer)



# # 1764 듣보잡
# # 메모리 : 37776KB   /   시간 : 120ms   / 코드 길이 : 438B

# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split(' '))

# unknown_dict = {}

# for _ in range(n):
#     name = sys.stdin.readline().rstrip()
#     unknown_dict[name] = False
# for _ in range(m):
#     name = sys.stdin.readline().rstrip()
#     if name in unknown_dict:
#         unknown_dict[name] = True

# answer = [ key for key, value in unknown_dict.items() if value ]
# answer.sort()
# print(len(answer))
# for name in answer:
#     print(name)