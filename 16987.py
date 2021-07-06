# 계란으로 계란치기
import sys
input = sys.stdin.readline

n = int(input())
eggs = [0]*n
damages = [0]*n

for i in range(n):
    eggs[i], damages[i] = map(int, input().split())

ans = 0 

def bomb(idx, eggs):
    global ans
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt +=1
        if cnt > ans:
            ans = cnt
        return

    if eggs[idx] > 0:
        for i in range(n):
            check = False
            if eggs[i] > 0 and i != idx:
                check = True
                tmp = eggs[:]
                tmp[i] -= damages[idx]
                tmp[idx] -= damages[i]
                bomb(idx+1, tmp)
        if not check:
            bomb(idx+1, eggs)
    else:
        bomb(idx+1, eggs)

bomb(0, eggs)
print(ans)