import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dogamNo = {}
dogamKo = {}

for i in range(n):
    name = input().rstrip()
    dogamNo[i+1] = name
    dogamKo[name] = i+1

for j in range(m):
    ques = input().rstrip()
    if ques.isdigit():
        print(dogamNo[int(ques)])
    else:
        print(dogamKo[ques])