# 5525 IOIOI
# 메모리 : 32796KB   /   시간 : 216ms   / 코드 길이 : 453B
"""
- 첫번째 풀이로 푸는 경우 50점
- m - (2n + 1) 만큼 확인하지만 계속해서 슬라이싱하므로 시간초과 나는듯
- 패턴을 'I' + 'OI' * n 으로 해석

- 두번째 풀이로 푸는 경우 100점
- 패턴을 'IOI'로 해석
- 기준 인덱스로부터 +2 한 값이 'IOI'인 경우 인덱스를 2 증가, 패턴 개수를 1 증가
- 패턴 개수가 n이 되면 구하는 패턴('IOIOIOI..') 이 됨
- 패턴 개수 -= 1 해준 후 정답 개수 += 1  
"""
"""
첫번째 풀이:
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

p = "I" + ("OI" * n)

total = 0
for idx in range(m - (2*n + 1)):
    if s[idx:idx+(2*n+1)] == p:
        total += 1
print(total)
"""
import sys
input = sys.stdin.readline

def solution(n, m, s):
    idx = 0
    p_cnt = 0
    total = 0
    while idx < m - 1:
        if s[idx:idx+3] == "IOI":
            p_cnt += 1
            if p_cnt == n:
                total += 1
                p_cnt -= 1
            idx += 2
        
        else:
            p_cnt = 0
            idx += 1
    
    return total

n = int(input())
m = int(input())
s = input().rstrip()

print(solution(n, m, s))
