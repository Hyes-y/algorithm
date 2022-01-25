# 1330 입력된 두 수 값 비교 
# 메모리 : 30864KB   /   시간 : 72ms   / 코드 길이 : 111B

a, b = map(int, input('두 수를 입력하세요> ').split(' '))

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")