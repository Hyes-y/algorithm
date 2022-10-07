# 6064 카잉 달력
# 메모리 : 30840KB   /   시간 : 1288ms   / 코드 길이 : 670B
# 수학
# 최소 공배수(유클리드 호제법 이용)
# 39번째 줄에서 나머지 계산을 하기 때문에 y == n인 경우 0으로 바꿔줘야함
import sys
input = sys.stdin.readline

def gcd(a, b):
    mx = max(a, b)
    mn = min(a, b)
    
    gcd_val = 1
    while True:
        r = mx % mn
        if r == 0:
            gcd_val = mn
            break
        mx, mn = mn, r
    return gcd_val


n = int(input())

for _ in range(n):
    m, n, x, y = map(int, input().split())
    lcm = (m * n) // gcd(m, n)
    
    if m == x and n == y:
        print(lcm)
        continue

    if m < n:
        m, n, x, y = n, m, y, x
    limit_m = lcm // m

    y = 0 if n == y else y
    result = -1
    for i in range(limit_m):
        if (m * i + x) % n == y:
            result = m * i + x
            break
    print(result)