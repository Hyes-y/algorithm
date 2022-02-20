def solution(brown, yellow):
    answer = []
    yellow_pair = []

    rt_yellow = int(yellow ** 0.5)
    for i in range(1, rt_yellow+1):
        if yellow % i == 0:
            yellow_pair.append((i, int(yellow/i)))

    for pair in yellow_pair:
        if brown == 2 * sum(pair) + 4:
            answer.append(pair[1]+2)
            answer.append(pair[0]+2)
    return answer