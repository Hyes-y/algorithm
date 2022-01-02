"""
<문제 설명 : 다리를 지나는 트럭>
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

"""

"""
idea!
- deq는 다리(len(deq)는 다리에 올라갈 수 있는 트럭 수 의미)
- 다리에 들어간 순서대로 트럭이 나와야 함
- 다리를 다 지난 트럭은 already_gone
- deq(다리)의 총합은 weight 보다 작아야 함 (다리에 올라가기 전에 미리 무게 비교)

고려사항!
1. 리스트에서 pop(0) 은 0번 인덱스 요소를 제거한 후에 나머지를 끌어오는 작업이 필요해서 시간이 오래걸림
-> collections 에 있는 deque를 활용
2. 다리 무게 제한을 위해 sum(deq)를 사용할 경우 deque의 요소를 일일히 확인하므로 시간이 오래걸림
-> deq_sum 변수를 활용
3. 같은 아이디어에서 클래스를 사용한 방법도 있었음
"""


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    already_gone = []
    deq = deque([])
    deq_sum = 0
    i = 0
    while i < len(truck_weights):
        if len(deq) == bridge_length:
            gone_truck = deq.popleft()
            deq_sum -= gone_truck
            already_gone.append(gone_truck)
        else:
            if deq_sum + truck_weights[i] > weight:
                deq.append(0)
            else:
                deq.append(truck_weights[i])
                deq_sum += truck_weights[i]
                i += 1
            
    answer = len(already_gone) + len(deq) + bridge_length    
    return answer
