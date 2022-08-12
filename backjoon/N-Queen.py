# 9663 N-Queen
# 메모리 : 204796KB   /   시간 : 31648ms   / 코드 길이 : 610B   /  PyPy3  / DFS(Recursion)
# 메모리 : 128092KB   /   시간 : 7992ms   / 코드 길이 : 777B   /  PyPy3  / 백트래킹(Recursion)
# 백트래킹 , 브루트포스
"""
Python3 으로 풀어보려 했으나 실패 
DFS는 크게 최적화를 고려하지 않고 작성한 코드이므로 패스

> BASE IDEA
- 행 또는 열 중 하나를 기준으로 퀸이 하나만 놓일 수 있다. (굳이 2차원 배열을 쓰지 않아도 됨)
- 한 행 또는 열에 퀸이 위치할 경우 해당 행 또는 열에 퀸이 다시 놓일 수 없다. (배열에 중복 저장 x)
- 현재 퀸의 위치를 i, j 라고 하고, 나머지 칸의 위치를 m, n으로 표현할 때
i + j == m + n 이라면 상향 대각선으로 움직일 수 있고
i - j == m - n 이라면 하향 대각선으로 움직일 수 있다.

> 최적화 과정
처음 풀이는 행을 기준으로 열의 위치를 1차원 배열에 나타내고
해당 열이 가능한지 확인하기 위해 현재 행 이전까지 위 두 가지 조건을 만족하는지 확인(초기 check 함수)

-> for문을 한 번만 돌게 check 함수 수정

-> BT 함수에서 중복인지 확인하게 수정

-> 대각선 확인을 diag_d(하향), diag_u(상향) 배열로 확인

-> 하향 대각선의 경우 i - j 가 음수일 수 있으므로 n - 1을 더해줌

-> BT 함수에서 대각선과 중복 여부 다 확인하는 로직으로 변경
"""

def check(graph, r, c):
    for j in range(1, r):
        if abs(graph[j] - c) == r - j:
            return False
    
    return True


def BT(cols, diag_d, diag_u, n, idx):
    global answer
    
    for i in range(1, n+1):
        diff = idx - i + n - 1
        plus = idx + i
        
        if diag_d[diff] or diag_u[plus] or cols[i]:
            continue
        else:
            if idx == n:
                answer += 1
                return

            cols[i] = True
            diag_d[diff] = True
            diag_u[plus] = True
            BT(cols, diag_d, diag_u, n, idx+1)
            cols[i] = False
            diag_d[diff] = False
            diag_u[plus] = False

    return


n = int(input())

cols = [False] * (n+1)
cols[0] = True
diag_d = [False] * (2 * (n + 1))
diag_u = [False] * (2 * (n + 1))
answer = 0

BT(cols, diag_d, diag_u, n, 1)
print(answer)