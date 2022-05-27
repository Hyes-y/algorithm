# 2512 예산
# 메모리 : 30840KB   /   시간 : 112ms   / 코드 길이 : 508B
'''
* 이분탐색

3 <= n(지방 수) <= 10000
1 <= 예산 <= 100000
n <= m(총 예산) <= 1000000000

idea > 총 예산 범위를 기준으로 절반씩 줄여나가며 탐색
-> 해당 예산일때 총 예산 값이 m보다 큰 경우 end = mid - 1
-> 해당 예산일때 총 예산 값이 m보다 같거나 작은 경우 answer = mid 지정 후 start = mid + 1
반복문은 start <= end가 아닐때 종료
'''
from sys import stdin

n = int(stdin.readline())
budget_list = list(map(int, stdin.readline().rstrip().split()))
m = int(stdin.readline())
start = 1
end = 1000000000
answer = 0
while start <= end:
    cnt = 0
    if sum(budget_list) <= m:
        answer = max(budget_list)
        break

    mid = (start + end) // 2
    
    for budget in budget_list:
        cnt += budget if budget <= mid else mid
    if cnt <= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)