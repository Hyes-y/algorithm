# 14500 테트로미노
# 메모리 : 35856KB   /   시간 : 3624ms   / 코드 길이 : 1347B
"""
풀이 방식 : 4 x 1, 3 x 2, 2 x 3, 1 x 4 범위만큼 확인하면서 테트로미노의 빈 부분을 저장한
dict를 참고하여 합을 구하기!

⭐ dfs로 풀면 훨씬 빠르게 풀 수 있음
"""
import sys
input = sys.stdin.readline

tetromino = {
    (4, 1): [],
    (2, 3): [
        [(0, 0), (0, 1)], 
        [(0, 1), (0, 2)], 
        [(1, 0), (1, 1)], 
        [(1, 1), (1, 2)],
        [(0, 0), (1, 2)],
        [(0, 2), (1, 0)],
        [(1, 0), (1, 2)],
        [(0, 0), (0, 2)]
    ],
    (2, 2): [],
    (3, 2): [
        [(0, 0), (1, 0)],
        [(1, 0), (2, 0)],
        [(0, 1), (1, 1)],
        [(1, 1), (2, 1)],
        [(0, 0), (2, 0)],
        [(0, 0), (2, 1)],
        [(2, 0), (0, 1)],
        [(0, 1), (2, 1)],
    ],
    (1, 4): []
}

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        for key, value in tetromino.items():
            di, dj = key
            if i + di <= n and j + dj <= m:
                total = 0
                for mi in range(di):
                    total += sum(board[i+mi][j:j + dj])
                
                if not value and total > answer:
                    answer = total

                for sub_v in value:
                    sub_total = total
                    for sub_i, sub_j in sub_v:
                        sub_total -= board[i+sub_i][j+sub_j]
                    if sub_total > answer:
                        answer = sub_total

print(answer)