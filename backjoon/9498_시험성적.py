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