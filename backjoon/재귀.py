# # 10872 팩토리얼
# # 메모리 : 30860KB   /   시간 : 68ms   / 코드 길이 : 133B

# n = int(input())

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(n))


# # 10870 피보나치 수 5
# # 메모리 : 30864KB   /   시간 : 68ms   / 코드 길이 : 146B

# n = int(input())

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     return fib(n-1) + fib(n-2)

# print(fib(n))


# # 2447 별찍기 10
# # 메모리 : 40208KB   /   시간 : 84ms   / 코드 길이 : 457B

# def starpattern(n):
#     if n == 1:
#         pattern = ["*"]
#         return pattern
    
#     prev_pattern = starpattern(n//3)
#     new_pattern = []
#     for pattern in prev_pattern:
#         new_pattern.append(pattern * 3)
#     for pattern in prev_pattern:
#         new_pattern.append(pattern + ' '*(n//3) + pattern)
#     for pattern in prev_pattern:
#         new_pattern.append(pattern * 3)

#     return new_pattern

# n = int(input())
# print('\n'.join(starpattern(n)))


# # 11729 하노이 탑
# # 메모리 : 121488KB   /   시간 : 1572ms   / 코드 길이 : 311B

# def hanoi(n, first, last):
#     if n == 1:
#         return [(first, last)]
    
#     next = 6 - (first + last)
    
#     return hanoi(n-1, first, next) + hanoi(1, first, last) + hanoi(n-1, next, last)


# n = int(input())

# answer = hanoi(n, 1, 3)
# print(len(answer))
# for move in answer:
#     a, b = move
#     print(a, b)

