# DFS / BFS
# 문제 > https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환
"""
explain > 시작 단어에서 목표 단어로 변환하는 최소 횟수
- 변환은 한글자만 다른 경우 진행 가능
- 변환이 가능한 단어가 리스트로 주어짐
['hot', 'dog', 'dot', 'cog']
'hit'(시작 단어) > 'hot' > 'dot' > 'dog' > 'cog' (목표 단어)

idea > 문제 그대롭니다

※ DFS로 풀었으나 BFS로 푸는게 효율적인듯
"""

# solve 1. DFS(stack)
def solution(begin, target, words):
    answer = 0
    for i, word in enumerate(words):
        if len(list(filter(lambda x: x[0]!=x[1], zip(begin, word)))) == 1:
            stack = [(i, word)]
            visited = [False] * len(words)
            cnt = 0
            while stack:
                idx, word = stack.pop()
                if visited[idx]:
                    continue
                
                visited[idx] = True
                cnt += 1
                
                if word == target:
                    answer = cnt if answer == 0 else min(answer, cnt)
                    break
                
                for idx, val in enumerate(visited):
                    if val:
                        continue

                    else:
                        if len(list(filter(lambda x: x[0]!=x[1], zip(words[idx], word)))) == 1:
                            stack.append((idx, words[idx]))
                
                

    return answer


# solve 2. BFS(queue)
from collections import deque as dq
def solution2(begin, target, words):
    answer = 0
    q = dq([(begin, 0)])
    visited = [False] * len(words)

    while q:
        word, cnt = q.popleft()

        if word == target:
            answer = cnt
            break
        
        for i, val in enumerate(visited):
            if val:
                continue

            else:
                c = 0
                for w1, w2 in zip(word, words[i]):
                    if w1 != w2:
                        c += 1
                if c == 1:
                    visited[i] = True
                    q.append((words[i], cnt+1))

    return answer
                     
