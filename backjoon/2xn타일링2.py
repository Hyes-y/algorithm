# 11727 2 X N 타일링2
# 메모리 : 55208KB   /   시간 : 200ms   / 코드 길이 : 451B
# DP
# 더 빠른 풀이 => dp[n] = dp[n-1] + dp[n-2] * 2
import sys
input = sys.stdin.readline

n = int(input())
memo = {i: [] for i in range(1, n+1)}

memo[1] = [1]
memo[2] = [1, 1]

if n >= 3:
    for i in range(3, n+1):
        prev = [0] + memo[i-2]
        cur = memo[i-1]

        if len(prev) != len(cur):
            cur.append(0)
        
        for a, b in zip(prev, cur):
            memo[i].append(a+b)


total = 0
for idx, x in enumerate(memo[n]):
    total += (2**idx) * x
print(total % 10007)