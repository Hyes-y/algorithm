# Summer/Winter Coding(~2018)
# 문제 > https://school.programmers.co.kr/learn/courses/30/lessons/12987
# 숫자 게임
"""
explain > A팀의 순서별 카드 숫자가 주어질때, B팀이 이길 수 있는 최고 점수
- A: [5, 1, 3, 7] 일 때
- B: [6, 2, 2, 8] 순서로 A와 게임해야 승점 3점으로 이김

idea > 참고한 아이디어 (https://school.programmers.co.kr/questions/37091)
- 최대한 많이 이기기 위해서는 A의 값보다 큰걸 내되, 큰 카드 중 가장 작은 것을 내야한다.
"""
# solve.
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for a in A:
        idx = 0
        win = False
        for i, b in enumerate(B):
            if a >= b:  # A와 같은 걸 굳이 낼 필요 없음
                break
            else:
                win = True
                idx = i
        if win:
            answer += 1
            del B[idx]
            
    return answer


test_a = "1 1 1 1 1 1 1 1 2 2 2 2 3 4 5"
test_b = "1 1 1 1 1 1 1 1 2 2 2 3 4 4 5"
test_a = list(map(int, test_a.split(" ")))
test_b = list(map(int, test_b.split(" ")))
print(solution(test_a, test_b))