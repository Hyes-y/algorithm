# 2839 설탕 배달
# 메모리 : 30864KB   /   시간 : 72ms   / 코드 길이 : 306B

import sys
n = int(sys.stdin.readline())

result = -1
d_f = n // 5
bal = n % 5
if bal == 0:
    result = d_f
else:
    for i in range(d_f, -1, -1):
        bal = n - (5*i)
        if bal < 0:
            continue
        if bal % 3 == 0:
            result = i + (bal // 3)
            break

print(result)




# 1783 병든 나이트
# 메모리 : 32352KB   /   시간 : 7424ms   / 코드 길이 : 429B