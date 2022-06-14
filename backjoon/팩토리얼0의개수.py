# 1676 팩토리얼 0의 개수
# 메모리 : 30840KB   /   시간 : 72ms   / 코드 길이 : 202B
'''
idea > 곱하는 숫자가 5의 배수인경우 5의 개수만큼 0이 증가
'''

import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

for i in range(1, n+1):
    k = i
    while k % 5 == 0:
        k //= 5
        cnt += 1
        if k == 1:
            break
print(cnt)