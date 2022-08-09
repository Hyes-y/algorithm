# 9095 1, 2, 3 더하기
# 메모리 : 30840KB   /   시간 : 72ms   / 코드 길이 : 264B
# 문제 잘못 읽고,, 풀이 봤음. ㅠㅠ

k = int(input())
dp = [0] * (12)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(k):
    n = int(input())
    
    if dp[n] != 0:
        print(dp[n])
        continue

    for i in range(4, n+1):        
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[n])

