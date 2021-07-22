# 13일의 금요일

import sys

N = int(sys.stdin.readline())

cnt = 0
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
check = 4 # 첫 번 째 금요일이 4일임
for year in range(2019,N+1):
    if year%400 == 0 or (year%4==0 and year%100!=0):
        dates[1] = 29
    else:
        dates[1] = 28
    
    for i in range(12):
        while check <= dates[i]:
            if check == 13:
                cnt+=1
            check+=7
        check-=dates[i]
    
print(cnt)