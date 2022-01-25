# 2753 입력된 연도를 윤년인지 판단 
# 메모리 : 30864KB   /   시간 : 64ms   / 코드 길이 : 113B

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)