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

S = input()

a = 0
if S == 'SUN':
    a = 0
elif S == 'MON':
    a = 1
elif S == 'TUE':
    a = 2
elif S == 'WED':
    a = 3
elif S == 'THU':
    a = 4
elif S == 'FRI':
    a = 5
elif S == 'SAT':
    a = 6

print(7-a)
