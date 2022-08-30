# 2022 KAKAO TECH INTERNSHIP
# 문제 > https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 두 큐의 합 같게 만들기 => 큐의 FIFO 성질에 따라 popleft()와 append() 이용
"""
idea > 합이 큰 큐에서 원소를 추출하여 작은 큐에 삽입
종료 조건 :
1) 두 큐의 전체 합 // 2  값보다 두 큐의 최댓값이 크면 합이 같을 수 없음
2) 큐 연산이 두 큐의 합의 1.5배를 넘어가면 무한 루프이므로 연산을 종료해야함
=> 길이가 같은 큐 2개가 주어지므로 l = len(q1)일때 cnt < 3 * l
=> ex> [1, 1, 1, 1, 1], [1, 1, 1, 9, 1] => 12
※ 채점 케이스 1번이 cnt가 큰 경우
※ while 탈출 조건을 total1 혹은 total2가 0인 경우를 조건으로 줄시 11, 28번 시간초과
"""

from collections import deque as dq

def solution(queue1, queue2):
    answer = -1
    total1 = sum(queue1)
    total2 = sum(queue2)
    max1 = max(queue1)
    max2 = max(queue2)
    l = len(queue1)
    if ((total1 + total2) // 2) < max(max1, max2):
        return answer
    else:
        q1 = dq(queue1)
        q2 = dq(queue2)
        
        cnt = 0
        while cnt <= (l * 3): 
            if total1 == total2:
                answer = cnt
                break

            elif total1 > total2:
                val = q1.popleft()
                q2.append(val)
                total1 -= val
                total2 += val
                cnt += 1
                
            elif total1 < total2:
                val = q2.popleft()
                q1.append(val)
                total2 -= val
                total1 += val
                cnt += 1
        return answer
