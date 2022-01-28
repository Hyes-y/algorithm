# # 2562 입력받은 9개의 수 중 최대값과 나온 순서
# # 메모리 : 30860KB   /   시간 : 68ms   / 코드 길이 : 126B

# num_list = [(int(input()), i) for i in range(9)]

# num_list.sort(reverse=True)

# print(num_list[0][0])
# print(num_list[0][1] + 1)


# # 2577 입력 받은 세 수의 곱에서 0-9까지 숫자 개수 구하기
# # 메모리 : 30860KB   /   시간 : 72ms   / 코드 길이 : 179B

# answer_list = [0] * 10
# num = 1
# for _ in range(3):
#     num *= int(input())

# num = str(num)

# for i in num:
#     answer_list[int(i)] += 1

# for answer in answer_list:
#     print(answer)


# # 4344 평균은 넘겠지
# # 메모리 : 30860KB   /   시간 : 76ms   / 코드 길이 : 374B

# n = int(input())
# answer_list = []

# for _ in range(n):
#     num_list = list(map(int, input().split(' ')))
#     avg = sum(num_list[1:]) / num_list[0]
#     avghigh = list(filter(lambda x: x > avg, num_list[1:]))
#     percent = (len(avghigh) * 100) / num_list[0]
    
#     answer_list.append(percent)

# for answer in answer_list:
#     print(f'{answer:.3f}%')
