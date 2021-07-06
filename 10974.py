# 모든 순열
import sys
from itertools import permutations
n = int(sys.stdin.readline())
num = [i+1 for i in range(n)]
answer = list(permutations(num,n))
for a in answer:
    line = ''
    for i in a:
        line = line + str(i) + ' '
    print(line)