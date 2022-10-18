import sys
input = sys.stdin.readline

n = int(input())
friends = list(map(int, input().split()))

print(sum(friends))