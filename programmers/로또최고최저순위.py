# 2021 dev-matching 상반기 : 웹 백엔드 개발자 
# 로또 최고, 최저 순위 구하기
# map을 이용해 lottos와 win_nums의 겹치는 부분과 0(조커? ㅋㅋ), 겹치지 않는 부분을 구분
# lottos와 win_nums의 겹치는 부분을 구할때 set(lottos) & set(win_nums) 로 구할 수 있음
# set과 연산을 익혀야 할 듯 !!


def solution(lottos, win_nums):
    lotto_rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }

    compares = list(map(lambda x: x if x in win_nums or x == 0 else -1, lottos))
    max_val, min_val = 0, 0
    for num in compares:
        if num > 0:
            min_val += 1
            max_val += 1
        elif num == 0:
            max_val += 1
        else:
            continue
    answer = [lotto_rank[max_val], lotto_rank[min_val]]
    return answer