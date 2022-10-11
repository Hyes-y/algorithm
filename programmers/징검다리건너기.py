# 2019 카카오 개발자 겨울 인턴십
# 문제 > https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 징검다리 건너기 => 이분탐색!
"""
idea > 이분 탐색으로 k만큼의 거리가 벌어진 최댓값 구하기
- 연속으로 k개 이상 징검다리가 0이 된 경우 건너갈 수 없음
- 0이 되는 징검다리가 연속으로 k개 되지 않는 최댓값 구하기

종료 조건 :
1) start < end
2) 기준값보다 같거나 작은 징검다리가 연속으로 k개 있는 경우

※ start와 end가 같은 경우 while문을 탈출하므로 mid값이 갱신이 안됨 => 마지막에 한번 더 처리해줌
"""
def solution(stones, k):
    start = min(stones)
    end = max(stones)
    
    while start < end:
        mid = (start + end) // 2
        seq = 0
        
        for i in range(len(stones)):
            if stones[i] <= mid:
                seq += 1
            else:
                seq = 0
            if seq == k:
                break
        
        if seq == k:
            end = mid
        else:
            start = mid + 1
    if start == end:
        mid = (start + end) // 2
    return mid


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3)
print(solution([4, 1, 1, 1, 4, 4, 4, 1, 1, 1], 4), 4)