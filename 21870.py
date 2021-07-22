# 시철이가 사랑한 GCD
import sys
from math import gcd
input = sys.stdin.readline

S = int(input())
bang = list(map(int,input().split()))

def sub_gcd(lists):
    sub = lists[0]
    for i in range(1,len(lists)):
        sub = gcd(sub,lists[i])
    return sub

def recur(lists):
    if len(lists) == 1:
        return lists[0]
    l = lists[:len(lists)//2]
    r = lists[len(lists)//2:]

    return max(sub_gcd(r)+recur(l),sub_gcd(l)+recur(r))

print(recur(bang))