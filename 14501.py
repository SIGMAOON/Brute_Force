# 퇴사
import sys
input = sys.stdin.readline

days = int(input())
T = [0]*days
P = [0]*days
for i in range(days):
    t,p = map(int,input().split())
    T[i] = t
    P[i] = p

dp = [0]*(days+1)

for i in range(days-1,-1,-1):
    if i + T[i] > days:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[0])