# 숫자 야구
from sys import stdin
from itertools import permutations
input = stdin.readline

n = int(input())
nums = list(map(list,permutations([1,2,3,4,5,6,7,8,9],3))) # 모든 수

# 입력과 결과 같을 때 true
def baseball(key,num,s,b):
    snt = bnt = 0
    for i in range(3):
        if key[i] in num:
            if key[i] == num[i]:
                snt+=1
            else:
                bnt+=1
    if snt == s and bnt == b:
        return True
    else:
        return False

for _ in range(n):
    gauss,s,b = map(int,input().split())
    gauss = str(gauss)
    gauss = [int(gauss[x]) for x in range(3)]
    sub = []
    for num in nums:
        if baseball(gauss,num,s,b):
            sub.append(num)
    nums = sub # update nums

print(len(nums))