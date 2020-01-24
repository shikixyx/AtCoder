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
A = list(input())


for i in range(len(A)):
    a = ord(A[i])
    a += N
    #print(a)
    while(a > 90):
        a -= 26

    A[i] = chr(a)

print(''.join(A))
