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

# import sys
# from collections import deque

# n = int(sys.stdin.readline())

# answer = deque()

# for _ in range(n):
#     param = sys.stdin.readline().rstrip()

#     if len(param) >= 6:
#         func, num = param.split(' ')
#         getattr(answer, 'append')(int(num))
#         continue

#     if param == 'pop':
#         value = answer.popleft() if len(answer) else -1
#     elif param == 'size':
#         value = len(answer)
#     elif param == 'empty':
#         value = 0 if len(answer) else 1
#     elif param == 'front':
#         value = -1 if not len(answer) else answer[0]
#     elif param == 'back':
#         value = -1 if not len(answer) else answer[-1]

#     print(value)



# 1158 요세푸스
# 메모리 : 32352KB   /   시간 : 7424ms   / 코드 길이 : 429B

# import sys
# from collections import deque

# n, k = map(int, sys.stdin.readline().rstrip().split(' '))

# answer = ""

# people = [i for i in range(1, n+1)]
# people_q = deque(people)

# idx = 1
# while len(people_q) > 0:
#     person = people_q.popleft()
#     if idx == k:
#         answer += str(person) + ", "
#         idx = 1
#         continue
#     else:
#         people_q.append(person)
#         idx += 1

# answer = answer[:-2]
# print(f"<{answer}>")



# 11866 요세푸스 0
# 메모리 : 32368KB   /   시간 : 208ms   / 코드 길이 : 393B
'''
from collections import deque as dq

n, k = map(int, input().split())

n_list = dq(list(range(1, n+1)))
answer = []
cnt = 1
while len(n_list) != 0:
    if cnt > k:
        cnt -= k

    t = n_list.popleft()

    if cnt == k:
        answer.append(t)
    else:
        n_list.append(t)
    
    cnt += 1

answer = map(str, answer)

print("<", end='')
print(', '.join(answer), end='')
print(">")
'''


# 2164 카드2

'''

카드는 1(top) ~ n(bottom) 로 놓여져 있다
순서대로 맨 윗장은 제거하고 그 다음장은 맨 아래로 보낸다.

1> deque.rotate 이용
-> deque.rotate(양수) => 시계 방향으로 회전 [1, 2, 3] => [3, 1, 2]



'''

from collections import deque as dq
import sys

# n = int(sys.stdin.readline())

def cardPlay(n):
    card_deck = dq([i for i in range(1, n+1)])

    while len(card_deck) != 1:
        card_deck.popleft()
        card_deck.rotate(-1)

    return card_deck[0]



# for i in range(1, 33):
#     print("n: ", i, " card:", cardPlay(i))

