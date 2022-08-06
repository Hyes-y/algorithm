# 1463 1로 만들기
# 메모리 : 38652KB   /   시간 : 476ms   / 코드 길이 : 295B

def solution(n: int):
    """
    dynamic programming (bottom up) 방식 사용
    3이나 2로 나눠지거나 1을 빼는 3가지 경우 중 최솟값을 저장
    """
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # 1을 빼야 하는 경우
        dp[i] = dp[i-1] + 1

        # 3으로 나눠지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        
        # 2로 나눠지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
    
    return dp[n]

x = int(input())
print(solution(x))


# 다른 풀이 (다른 분의 풀이)
# 시간이 훨씬 적게 걸림
# top down 방식
dic = {1:0}
def f(n,c) :
    if n == 1 :
        return c
    elif n in dic :
        return c + dic[n]
    elif n%6 == 0:
        return min(f(n/3,c+1),f(n/2,c+1))
    elif n%3 == 0:
        return min(f(n/3,c+1),f(n-1,c+1))
    elif n%2 == 0:
        return min(f(n/2,c+1),f(n-1,c+1))
    else:
        return f(n-1,c+1)
for n in range(2,min(10000,x)) :
    dic[n] = f(n,0)
print(f(x,0))
