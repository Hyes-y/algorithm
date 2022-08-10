# 11659 구간합 구하기 4
# 메모리 : 30840KB   /   시간 : 72ms   / 코드 길이 : 264B
# 구간합은 리스트의 각 원소를 더한 값을 다시 리스트로 만들어서 빼주는 방식으로 구현
# ex. 1 - 3 구간을 구할때 합을 저장한 리스트의 3번 인덱스에서 0번 인덱스를 빼줌

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().rstrip().split(" ")))

sum_arr = []
sub_sum = 0
for _ in range(n):
    sum_arr.append(sub_sum)
    sub_sum += arr[_]
sum_arr.append(sub_sum)

for k in range(m):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])

