# 사탕 게임, pypy
import sys
input = sys.stdin.readline

n = int(input())
candy = [list(input())[:-1] for _ in range(n)]
maximum = 0

# 탐색
def countNeum():
    cnt = 0
    for i in range(n):
        garo = saero = 1 
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                garo+=1
            else:
                cnt = max(cnt,garo)
                garo = 1
            if candy[j][i] == candy[j+1][i]:
                saero+=1
            else:
                cnt = max(cnt,saero)
                saero = 1
        cnt = max(cnt,garo,saero)
    return cnt



# 교환
for i in range(n):
    for j in range(n-1):
        # 가로
        if candy[i][j] == candy[i][j+1]:
            maximum = max(maximum,countNeum())
        else:
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
            maximum = max(maximum,countNeum())
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j] # 판 되돌려놓기
        # 세로
        if candy[j][i] == candy[j+1][i]:
            maximum = max(maximum,countNeum())
        else:
            candy[j][i],candy[j+1][i] = candy[j+1][i],candy[j][i]
            maximum = max(maximum,countNeum())
            candy[j][i],candy[j+1][i] = candy[j+1][i],candy[j][i] # 판 되돌려놓기

print(maximum)