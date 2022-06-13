# 1074 Z
# 메모리 : 30840KB   /   시간 : 72ms   / 코드 길이 : 292B

'''
z모양으로 칸을 채움

idea
> i, j 를 2진수로 변환한 뒤, 자릿수를 제곱하여 자릿수별 세로에 해당하는 값을 곱해준 합이 해당 칸의 숫자

ex> i = 3, j = 6
3 => 011
6 => 110
    3 |   0     1     1
    6 |   1     1     0
자릿수|   4     2     1
세로값| 1(01) 3(11) 2(10)
계산  | 4*4*1  2*2*3  1*1*2    => 30
'''
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

binary_r = format(r, 'b').zfill(n)
binary_c = format(c, 'b').zfill(n)

result = 0
for i in range(n):
    d = 2 ** (n - 1 - i)
    col_int = int(binary_r[i]+binary_c[i], 2)
    result += d * d * col_int 
print(result)