import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())

PATH = []
#COLOR = [[None for _ in range(N+1)] for _ in range(N+1)]
COLOR = defaultdict(int)
PT = [[] for _ in range(N+1)]
cmax = 1
for i in range(N-1):
    a, b = map(int, input().split())
    PATH.append((a, b))
    PT[a].append(b)
    PT[b].append(a)

    '''
    la = len(PT[a])
    lb = len(PT[b])

    l = la if la > lb else lb
    if l > cmax:
        cmax = l
    '''

q = deque([(1, -1)])
while(q):
    a, ng = q.popleft()
    bs = PT[a]

    c = 1
    for b in bs:
        if b > a:
            na = a
            nb = b
        else:
            na = b
            nb = a

        cab = COLOR[(na, nb)]

        if cab == ng:
            continue

        if cab == 0:
            if c == ng:
                c += 1
            clr = c
            COLOR[(na, nb)] = clr
            q.append((b, clr))
            c += 1

print(max(COLOR.values()))

clr = []
for a, b in PATH:
    clr.append(COLOR[(a, b)])

print("\n".join(map(str, clr)))
