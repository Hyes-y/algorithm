# # 4344 평균은 넘겠지
# # 메모리 : 30860KB   /   시간 : 76ms   / 코드 길이 : 374B

# # def divide(num):
# #     if num == 10000:
# #         return 1
    


# answer_list = [1]*101

# for i in range(1, 101):
#     num = i
    
#     # 숫자를 배열로 변경해서 풀이
#     num_list = [int(char) for char in str(num)]
#     num += sum(num_list)
#     # new_num = divide(num)

#     if num > 100:
#         continue

#     if answer_list[num] == 1:
#         answer_list[num] = 0
#     elif answer_list[num] == 0:
#         continue


# for i in range(1, 101):
#     if answer_list[i]:
#         print(i)
