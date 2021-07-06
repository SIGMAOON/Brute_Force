# 팰린드롬 만들기
# 주어진 문장 중 가장 긴 팰린드롬 찾아서, 그 차이만큼 더해서 반환
import sys
line = sys.stdin.readline()

def pal(lists):
    while len(lists) > 1:
        a,b = lists[0],lists[-1]
        if a == b:
            lists = lists[1:-1]
        else:
            return False
    return True

long = 0
for i in range(len(line)):
    sub = line[i:]
    if pal(sub):
        if len(sub) > long:
            long = len(sub)

print(2*len(line)-long)