# 10845 큐
# 메모리 : 32404KB   /   시간 : 96ms   / 코드 길이 : 653B

"""
collections의 deque 사용

- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

"""

import sys
from collections import deque

n = int(sys.stdin.readline())

answer = deque()

for _ in range(n):
    param = sys.stdin.readline().rstrip()

    if len(param) >= 6:
        func, num = param.split(' ')
        getattr(answer, 'append')(int(num))
        continue

    if param == 'pop':
        value = answer.popleft() if len(answer) else -1
    elif param == 'size':
        value = len(answer)
    elif param == 'empty':
        value = 0 if len(answer) else 1
    elif param == 'front':
        value = -1 if not len(answer) else answer[0]
    elif param == 'back':
        value = -1 if not len(answer) else answer[-1]

    print(value)