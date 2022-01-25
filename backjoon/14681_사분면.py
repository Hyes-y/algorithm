# 14681 입력된 좌표값의 사분면 위치
# 메모리 : 30860KB   /   시간 : 68ms   / 코드 길이 : 167B

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
