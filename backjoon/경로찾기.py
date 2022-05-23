# 11403 경로찾기
# 메모리 : 30840KB   /   시간 : 176ms   / 코드 길이 : 682B
'''
플로이드 워셜 알고리즘 사용이 가능한 문제
but dfs로 풀었음

중간에 방문 처리하는 부분에서 에러가 난 듯..
-> 방문한 경우 stack에 추가가 안되도록 수정
'''
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

answer = [[0 for _ in range(n)] for _ in range(n)]

stack = []

for k in range(n):
    stack.append(k)
    visited = [False for _ in range(n)]
    while stack:
        i = stack.pop()
        # 이 부분에서 문제가 있었던 것 같음
        # if visited[i] == True:
        #     break
        # visited[i] = True
        # 이렇게 하는 대신 방문 안했을때는 stack에 append 안하도록 수정
        for idx, val in enumerate(matrix[i]):
            if val == 1 and not visited[idx]:
                answer[k][idx] = 1
                visited[idx] = True
                stack.append(idx)
            else:
                continue
    
for i in range(n):
    print(*answer[i], sep=" ")