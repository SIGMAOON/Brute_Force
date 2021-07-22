from itertools import permutations
import sys

N = int(sys.stdin.readline())


for helloworld in permutations([1,2,3,4,5,6,7,8,9,0], 7):
    h,e,l,o,w,r,d = helloworld
    hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
    world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
    if hello + world == N and h != 0 and w != 0:
        print(f"  {hello}")
        print(f"+ {world}")
        print("-------")
        if N>=100000:
            print(f" {N}")
        else:
            print(f"  {N}")
        exit()
print("No Answer")