'''
lost 의 앞 뒷번호 reserve 여부 확인 후 
있는 경우 reserve랑 lost에서 해당 번호 제거

여벌 체육복이 있는 학생이 도난 당했을 수도 있음 ㅠㅠ

def solution(n, lost, reserve):
    lost_real = list(set(lost) - set(reserve))
    reserve_real = list(set(reserve) - set(lost))
    answer = n - len(lost_real)
    for idx, num in enumerate(lost_real):
        if (num - 1) in reserve_real:
            answer += 1
            del reserve_real[reserve_real.index(num-1)]
        elif (num + 1) in reserve_real:
            answer += 1
            del reserve_real[reserve_real.index(num+1)]
    
    return answer
'''

'''
list 보다는 set을 사용하는게 시간 복잡도 면에서 나음
'''
def solution(n, lost, reserve):
    lost_real = set(lost) - set(reserve)
    reserve_real = set(reserve) - set(lost)
    
    answer = n - len(lost_real)
    for num in lost_real:
        if (num - 1) in reserve_real:
            answer += 1
            reserve_real.remove(num - 1)
        elif (num + 1) in reserve_real:
            answer += 1
            reserve_real.remove(num+1)
    
    return answer
print(solution(5, [2, 4], [1, 3, 5]))