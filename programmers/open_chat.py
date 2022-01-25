"""
프로그래머스 코딩테스트 연습
2019 KAKAO BLIND RECRUITMENT
level2 . 오픈채팅방 
"""

def solution(record):
    answer = []
    order = []
    nickname = {}
    for string in record:
        obj = []
        sep = string.split(" ")
        if sep[0] == "Leave":
            pass
        else:
            nickname[sep[1]] = sep[2]
            if sep[0] == "Change":
                continue
        
        order.append([sep[0], sep[1]])
    
    for obj in order:
        if obj[0] == "Enter":
            action = "들어왔습니다."
        else:
            action = "나갔습니다."
            
        sentence = f"{nickname[obj[1]]}님이 {action}"
        answer.append(sentence)
    return answer
