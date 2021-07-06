# 백설 공주와 일곱 난쟁이
import sys
input = sys.stdin.readline
hats = [int(input()) for _ in range(9)]

out = sum(hats) - 100
idx = []

for i in range(9):
    for j in range(i):
        if hats[i] + hats[j] == out:
            idx.append(i)
            idx.append(j)
            break
            
for k in range(9):
    if k in idx:
        pass
    else:
        print(hats[k])