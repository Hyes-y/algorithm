# # 2292 벌집
# # 메모리 : 30860KB   /   시간 : 80ms   / 코드 길이 : 155B
# # 가우스 정리 이용

# n = int(input())

# step = 1

# while True:
#     check = (6 * step * (step - 1) / 2) + 1
#     if n <= check:
#         print(step)
#         break
    
#     step += 1


# # 2869 달팽이는 올라가고 싶다
# # 메모리 : 30864KB   /   시간 : 72ms   / 코드 길이 : 199B

# a, b, v = map(int, input().split())

# if a >= v:
#     print(1)

# else:
#     if (v - b) % (a - b) == 0:
#         answer = (v-b) // (a-b)
#     else:
#         answer = (v - b) // (a - b) + 1

#     print(answer)


# # 1929 소수 구하기(에라토스테네스의 체)
# # 메모리 : 141464KB   /   시간 : 264ms   / 코드 길이 : 	285B

# n, m = map(int, input().split())

# num_list = [False, False] + [True for _ in range(2, m+1)]

# rm = int(m**0.5)

# for i in range(2, m):
#     if num_list[i]:
#         for j in range(2, m//i + 1):
#             num_list[i*j] = False

# for k in range(n, m+1):
#     if num_list[k]:
#         print(k)


# # 9020 골드바흐의 추측
# # 메모리 : 126352KB   /   시간 : 212ms   / 코드 길이 : 	568B

# num_list = [False, False] + [True for _ in range(2, 10001)]
# prime_dict = {}
# for i in range(2, len(num_list)):
#     if num_list[i]:
#         prime_dict[i] = 0
#         for j in range(2, 10000//i + 1):
#             num_list[i*j] = False


# n = int(input())
# answer_list = []
# for _ in range(n):
#     k = int(input())
#     partition = ""
#     for key in prime_dict:
#         if key > k // 2:
#             answer_list.append(partition)
#             break
#         if k - key in prime_dict:
#             partition = (key, k-key)

# for answer in answer_list:
#     print(answer[0], answer[1])


# # 1002 터렛
# # 메모리 : 30860KB   /   시간 : 76ms   / 코드 길이 : 579B

# t = int(input())

# point_list = []
# for _ in range(t):
#     point_list.append(input())

# for point in point_list:
#     x1, y1, r1, x2, y2, r2 = map(int, point.split(" "))
#     if (x1 == x2) and (y1 == y2) and (r1 == r2):
#         print(-1)
#     elif (x1 == x2) and (y1 == y2):
#         print(0)
#     else:    
#         d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
#         if abs(r1 - r2) > d:
#             print(0)
#         elif abs(r1 - r2) == d:
#             print(1)
#         elif r1 + r2 > d:
#             print(2)
#         elif r1 + r2 == d:
#             print(1)
#         else:
#             print(0)
