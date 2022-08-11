# 2630 색종이 만들기 
# 메모리 : 30840KB   /   시간 : 104ms   / 코드 길이 : 681B  / cutting_paper
# 메모리 : 30840KB   /   시간 : 84ms   / 코드 길이 : 677B  / cutting_paper2
# 분할정복, 재귀

def cutting_paper(n, start_r, start_c):
    total = 0
    for r in range(start_r, start_r + n):
        for c in range(start_c, start_c + n):
            total += paper[r][c]
    
    if total == n ** 2 or total == 0:
        color = 0 if total == 0 else 1
        cnt[color] += 1
        return
    
    else:
        half = n // 2
        cutting_paper(half, start_r, start_c)
        cutting_paper(half, start_r + half, start_c)
        cutting_paper(half, start_r, start_c + half)
        cutting_paper(half, start_r + half, start_c + half)


def cutting_paper2(n, start_r, start_c):
    color = paper[start_r][start_c]
    for r in range(start_r, start_r + n):
        for c in range(start_c, start_c + n):
            if color != paper[r][c]:
                half = n // 2
                cutting_paper2(half, start_r, start_c)
                cutting_paper2(half, start_r + half, start_c)
                cutting_paper2(half, start_r, start_c + half)
                cutting_paper2(half, start_r + half, start_c + half)

                return
    
    cnt[color] += 1
    return


n = int(input())
cnt = [0, 0]
paper = [list(map(int, input().split())) for _ in range(n)]
cutting_paper2(n, 0, 0)
print(*cnt, sep="\n")