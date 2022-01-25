# # 1110 더하기 사이클
# # 메모리 : 30864KB   /   시간 : 80ms   / 코드 길이 : 272B


n = int(input())
cnt = 0
temp = n
while True:
    
    if n == 0:
        print(1)
        break

    a = temp // 10
    b = temp % 10

    element_sum = a + b
    temp = int(str(b) + str(element_sum % 10))

    cnt += 1

    if temp == n:
        print(cnt)
        break