import sys
#import numpy as np
import bisect
sys.setrecursionlimit(10 ** 7)

# TLE
# PyPy3 (2.4.0) 2112 ms

N, Q = map(int, input().split())
STX = []
for _ in range(N):
    s, t, x = map(int, input().split())
    STX.append((s, t, x))

PEOPLE = []
for _ in range(Q):
    d = int(input())
    PEOPLE.append(d)

ans = [-1] * Q

STX.sort(key=lambda x: -x[2])

for s, t, x in STX:
    #print("s,t,x", s, t, x)
    #i = np.searchsorted(PEOPLE, s - x)
    #j = np.searchsorted(PEOPLE, t - x)
    i = bisect.bisect_left(PEOPLE, s - x)
    j = bisect.bisect_left(PEOPLE, t - x)
    #print("i,j", i, j)

    ans[i:j] = [x] * (j-i)

    # for k in range(i, j):
    # if ans[k] == '-1':
    #ans[k] = str(x)

    # print(ans)

print("\n".join(map(str, ans)))
