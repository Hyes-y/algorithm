'''
시간 초과
from itertools import combinations

def solution(number, k):    
    keys = list(map(lambda x: int(''.join(x)), combinations(number, len(number) - k)))
    answer = str(max(keys))
    return answer
'''
'''
리턴해야하는 자릿수 : l 일때
number[:len(number) - l + 1] 에서 최댓값 하나 구하고
그 인덱스부터 다시 또 범위정해서 최댓값 구하기

테스트 10(시간초과), 11(런타임에러) 틀림
def solution(number, k):
    l = len(number) - k # 최종 자릿수
    answer = ""
    i = 0 # 기준 인덱스
    j = k # slice 인덱스
    while len(answer) != l:
        val = max(number[i:j])
        answer += val
        for m in range(i, len(number)):
            if number[m] == val:
                i = m + 1
                break
        j = len(number) - l + len(answer) + 1
        
    return answer
'''
def solution(number, k):
    l = len(number) - k # 최종 자릿수
    answer = ""
    i = 0 # 기준 인덱스
    j = k # slice 인덱스
    while len(answer) != l:
        val = "0"
        for m in range(i, j+1):
            if number[m] == "9":
                i = m + 1
                val = number[m]
                break
            if int(number[m]) > int(val):
                i = m + 1
                val = number[m]
        answer += val        
        j = len(number) - l + len(answer)
        
    return answer