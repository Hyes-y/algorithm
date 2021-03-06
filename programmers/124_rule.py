"""
프로그래머스 코딩테스트 연습
https://programmers.co.kr/learn/courses/30/lessons/12899
[124 나라의 숫자]
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라
1	1	
2	2	
3	4	
4	11	
5	12	
6	14
7	21
8	22
9	24
10	41

자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
"""

hash = {1:'1', 2:'2', 3:'4'}
def rule_124(k):
    if k in hash:
        return hash[k]
    
    quotient = k // 3
    remainder = k % 3
    if remainder == 0:
        if quotient in hash:
            hash[k] = hash[quotient-1] + '4'
            return hash[k]
        else:
            return rule_124(quotient-1) + '4'
    else:
        return rule_124(quotient) + str(remainder)


def solution(n):
    answer = rule_124(n)
    
    return answer
