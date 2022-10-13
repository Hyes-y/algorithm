# 2020 카카오 인턴십
# 문제 > https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 보석 쇼핑 => 투포인터 알고리즘!
"""
idea > 투포인터 알고리즘으로 모든 보석을 포함하는 최소 구간 구하기
구간 길이가 같은 경우 시작 위치가 더 작은 구간을 리턴
p1, p2 를 움직이면서 보석이 모두 포함되어있는지 확인

로직:
p2를 증가시키다가 종료 조건을 만족하면 p1을 증가
p1의 종료 조건을 만족하면 answer를 갱신

p2 종료 조건 :
1) p1 ~ p2 위치까지 모든 보석을 포함했을때
= 보석 종류 및 개수를 저장하는 dict의 길이가 보석의 개수와 같을때

p1 종료 조건 :
1) p1 ~ p2 위치까지 모든 보석을 포함하지 않았을 때
= 보석 종류 및 개수를 저장하는 dict의 길이가 보석의 개수와 같지 않을때

=> p1이 종료 조건에 걸리면 p1 - 1이 보석을 모두 포함하는 인덱스가 됨


※ 답은 맨 처음 보석의 위치를 1로 지정
=> 보석을 모두 포함하는 구간은 [p1 - 1, p2] 이므로 
정답은 [p1, p2 + 1]을 반환
"""
from collections import defaultdict as dd

def solution(gems):
    answer = [0, len(gems)-1]
    l = len(set(gems))
    dic = dd(int)
    p1 = 0
    for p2, val in enumerate(gems):
        dic[val] += 1
        
        if len(dic) == l:
            while len(dic) == l:
                if p1 >= len(gems):
                    p1 -= 1
                    break
                if dic[gems[p1]] == 1:
                    del dic[gems[p1]]
                else:
                    dic[gems[p1]] -= 1
                
                p1 += 1
            
            if answer[1] - answer[0] > p2 - p1:
                answer = [p1, p2]
            elif answer[1] - answer[0] == p2 - p1 and answer[0] > p1:
                answer = [p1, p2]
            
    answer[1] += 1        
    return answer


print(solution(["DIA", "RUBY", "EMERALD", "SAPPHIRE"])) # [1, 4]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))    # [3, 7]