"""
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

=> 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
(단, 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.)

입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2

"""

"""
아이디어!
-> heap 파트인 만큼 파이썬의 heapq 라이브러리 사용
-> 기존 리스트를 힙으로 변환해주는 heapify() 
-> heappush()는 원소를 삽입할 때 힙을 고려해줌

고려사항!
-> heapq보다 최소값 두 가지로 만든 new_scoville을 별도의 queue에 저장하는 경우 시간이 더 빠르다고 함
"""

import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        min1 = hq.heappop(scoville)
        min2 = hq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        answer += 1
        hq.heappush(scoville, new_scoville)
    
    if scoville[0] < K:
        return -1

    
    return answer
