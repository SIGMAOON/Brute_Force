# 떡 먹는 호랑이
import sys
D,K = map(int,sys.stdin.readline().split())
a,b = 1,0
for _ in range(D-1):
    a,b = b,a+b
for i in range(1,100001):
    if (K-i*a)%b == 0:
        print(i)
        print((K-i*a)//b)
        exit()