# # 10828 스택
# # 메모리 : 30864KB   /   시간 : 84ms   / 코드 길이 : 675B	
# # getattr(param, attr)(arg) => param의 attr속성(arg: 속성이 함수일때 필요한 인자)을 호출
# # 문자열과 속성명이 동일할때 사용

# import sys


# class myStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, n):
#         self.stack.append(n)

#     def pop(self):
#         return self.stack.pop(-1) if not self.empty() else -1

#     def size(self):
#         return len(self.stack)

#     def empty(self):
#         return 1 if not self.size() else 0

#     def top(self):
#         return self.stack[-1] if not self.empty() else -1


# n = int(sys.stdin.readline())

# answer = myStack()

# for _ in range(n):
#     param = sys.stdin.readline().rstrip()

#     if len(param) >= 6:
#         func, num = param.split(' ')
#         getattr(answer, func)(int(num))
#     else:
#         print(getattr(answer, param)())



# # 9012 괄호
# # 메모리 : 30864KB   /   시간 : 80ms   / 코드 길이 : 589B

# import sys

# cnt = int(sys.stdin.readline().rstrip())

# for _ in range(cnt):
#     vps_check = sys.stdin.readline().rstrip()

#     check_stack = []

#     if vps_check[0] == ')' or vps_check[-1] == '(':
#         print('NO')

#     else:
#         try:
#             for parenthesis in vps_check:
#                 if parenthesis == '(':
#                     check_stack.append(1)
#                 else:
#                     check_stack.pop(-1)
#         except:
#             print('NO')
#         else:    
#             if not check_stack:
#                 print('YES')
#             else:
#                 print('NO')



# # 4949 균형잡힌 세상
# # 메모리 : 30864KB   /   시간 : 112ms   / 코드 길이 : 756B

# import sys


# while True:
#     vps_check = sys.stdin.readline().rstrip()
#     if vps_check == '.':
#         break
    
#     underflow = False
#     balance = True
#     check_stack = []
    
#     for chr in vps_check:
#         try:  
#             if chr == '(':
#                 check_stack.append(')')
#             elif chr == '[':
#                 check_stack.append(']')
#             elif chr == ')' or chr == ']':
#                 check = check_stack.pop(-1)
#                 if check != chr:
#                     balance = False
#                     break
#             else:
#                 continue
#         except:
#             underflow = True
#             break
    
#     if not check_stack and not underflow and balance:
#         print('yes')
#     else:
#         print('no')


# # 17298 오큰수
# # 메모리 : 30864KB   /   시간 : 112ms   / 코드 길이 : 756B