# 1931 회의실 배정
# 메모리 : 51616KB   /   시간 : 260ms   / 코드 길이 : 280B
# 정렬
# 회의실 중복 제거하면 안됨ㅠㅠ

n = int(input())

times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: (x[1], x[0]))
check = 0
answer = 0
for start, end in times:
    if start >= check:
        answer += 1
        check = end

print(times)
print(answer)

"""
반례>
5
4 5
4 4
3 4
2 5
1 3
=> 4
"""