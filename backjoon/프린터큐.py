# 1966 프린터큐
# 메모리 : 32452KB   /   시간 : 88ms   / 코드 길이 : 622B
'''
input>
t : test case 개수
n, m : 문서의 개수, 출력 순서를 알고싶은 문서의 위치
중요도 ... 

idea> deque 2개 사용(하나는 출력위한 우선순위 오름차순, 하나는 real 출력)
'''
from sys import stdin
from collections import deque as dq

t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().rstrip().split())
    arr = list(map(int, stdin.readline().rstrip().split()))

    deq_sort = dq(sorted(arr, reverse=True))
    deq_printer = dq([(val, idx) for idx, val in enumerate(arr)])

    cnt = 1
    while deq_sort:
        doc = deq_printer.popleft()
        # 지금 출력 순서이며 index도 m과 같은 경우
        if doc[0] == deq_sort[0] and doc[1] == m:
            break
        # 지금 출력 순서인 경우
        elif doc[0] == deq_sort[0]:
            deq_sort.popleft()
            cnt += 1
        # 지금 출력 순서가 아닌 경우
        else:
            deq_printer.append(doc)

    print(cnt)