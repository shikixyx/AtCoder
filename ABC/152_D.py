import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = [[0 for _ in range(10)] for _ in range(10)]

'''
while(True):
    Nstr = str(N)
    l = len(Nstr) - 1

    if Nstr[0] == Nstr[l]:
        break

    N -= 1
'''

# print(N)


for i in range(N+1):
    s = str(i)
    l = len(s) - 1

    if s[l] == '0':
        continue
    A[int(s[0])][int(s[l])] += 1


ans = 0
for j in range(1, 10):
    for k in range(1, 10):
        ans += A[j][k] * A[k][j]

# print(A)
print(ans)
