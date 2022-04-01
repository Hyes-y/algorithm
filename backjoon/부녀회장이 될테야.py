# 2775 부녀회장이 될테야
# 메모리 : 32972KB   /   시간 : 68ms   / 코드 길이 : 280B
'''
1> 재귀로 풀었으나 시간 초과
2> apart[i][j] = apart[i][j-1] + apart[i-1][j]
3> 최단 경로 공식으로 해결!
'''
import time

start = time.time()

import math

for _ in range(int(input())):
    f = int(input())
    i = int(input())
    if i == 1:
        print(1)
    else:
        print(math.factorial(f + i) // (math.factorial(f+1) * math.factorial(i - 1)))

end = time.time()
print(f'{end - start} sec')