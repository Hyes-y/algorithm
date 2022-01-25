# 2884 입력받은 H, M 보다 45분 일찍 알람 설정하기
# 메모리 : 30864KB   /   시간 : 68ms   / 코드 길이 : 156B

H, M = map(int, input().split())

if M - 45 >= 0:
    M -= 45
    
else:
    M += 15
    if H - 1 >= 0:
        H -= 1
    else:
        H = 23

print(H, M)