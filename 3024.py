# 마라톤 틱택토, 다시 풀기, 주대각선 말고 작은 대각선도 보기
import sys
input = sys.stdin.readline

N = int(input())
board = [input().strip() for _ in range(N)]

ans = []
# 가로 세로
for i in range(N):
    sub = board[i][0]
    sub2 = board[0][i]
    for j in range(N-1):
        if board[i][j] == board[i][j+1]:
            sub+=board[i][j+1]
        else:
            ans.append(sub)
            sub = ''
        if board[j][i] == board[j+1][i]:
            sub2+=board[j+1][i]
        else:
            ans.append(sub2)
            sub2 = ''
    ans.append(sub)
    ans.append(sub2)
    sub = sub2 = ''

for x in ans:
    if len(x) == 3 and x[0]!='.':
        print(x[0])
        exit()

# 주대각선 위에
sub = sub2 = ''
for i in range(N):
    sub = board[0][i]
    sub2 = board[i][N-1]
    for j in range(N):
# 주대각선 아래
sub = sub2 = ''
for i in range(N):
    sub = board[i][0]
    sub2 = board[0][N-1]
print("ongoing")
