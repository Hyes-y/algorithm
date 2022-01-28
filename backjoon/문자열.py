# # 11720 입력 받은 숫자의 각 자릿수 합
# # 메모리 : 30864KB   /   시간 : 68ms   / 코드 길이 : 89B

# n = int(input())

# num = input()
# total = 0
# for i in num:
#     total += int(i)

# print(total)


# # 10809 입력받은 문자열의 각 알파벳이 처음 나오는 위치
# # 메모리 : 30864KB   /   시간 : 72ms   / 코드 길이 : 224B

# chr_dict = { x: -1 for x in range(97, 123)}
# string = input()

# for i in range(len(string)):
#     if chr_dict[ord(string[i])] == -1:
#         chr_dict[ord(string[i])] = i


# for item in chr_dict.values():
#     print(item, end=' ')


# 1157 입력받은 문자열에서 많이 나온 문자 찾기
# 메모리 : 32820KB   /   시간 : 272ms,264ms    / 코드 길이 : 270B

# 리스트 사용
# string = input().upper()
# answer_list = [0]*26

# for c in string:
#     answer_list[ord(c)-65] += 1

# max_val = max(answer_list)
# answer = [i for i, v in enumerate(answer_list) if v == max_val]

# if len(answer) == 1:
#     print(chr(answer[0] + 65).upper())
# else:
#     print("?")

# string = input().upper()
# chr_dict = { x: 0 for x in range(65, 91)}

# for c in string:
#     chr_dict[ord(c)] += 1

# max_val = max(chr_dict.values())

# answer = [i for i, v in chr_dict.items() if v == max_val]

# if len(answer) == 1:
#     print(chr(answer[0]))
# else:
#     print("?")



# # 5622 다이얼 누르기
# # 메모리 : 30860KB   /   시간 : 72ms    / 코드 길이 : 227B
# string = input()
# total = 0
# for c in string:
#     c = ord(c) - 65
#     if c >= 22:
#         total += 10
#     elif c >= 19:
#         total += 9
#     elif c >= 15:
#         total += 8
#     else:
#         total += (c // 3) + 3

# print(total)

# # 1316 그룹 단어 체커
# # 메모리 : 30864KB   /   시간 : 76ms    / 코드 길이 : 350B

# n = int(input())
# cnt = 0
# for _ in range(n):
#     word = input()
#     check_dict = {}
#     check_val = ''
#     check = True
#     for w in word:
#         if (check_val != w) and (w in check_dict):
#             check = False
#             break
#         else:
#             check_dict[w] = 1
#             check_val = w
    
#     if check:
#         cnt += 1

# print(cnt)
            
