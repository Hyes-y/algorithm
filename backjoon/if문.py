# 1330 입력된 두 수 값 비교 
# 메모리 : 30864KB   /   시간 : 72ms   / 코드 길이 : 111B

a, b = map(int, input('두 수를 입력하세요> ').split(' '))

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")


# 9498 입력된 성적 값을 조건문으로 학점 판별 
# 메모리 : 30864KB   /   시간 : 68ms   / 코드 길이 : 172B

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")




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




# 2753 입력된 연도를 윤년인지 판단 
# 메모리 : 30864KB   /   시간 : 64ms   / 코드 길이 : 113B

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)







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