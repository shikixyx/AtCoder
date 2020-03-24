import bisect
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 15min
# Dよりも簡単だった

N = int(readline())
A = [int(readline()) for _ in range(N)]

NUM = deque()
NUM.appendleft(A[0])

A = A[1:]


for a in A:
    if a <= NUM[0]:
        NUM.appendleft(a)
    else:
        i = bisect.bisect_left(NUM, a)
        NUM[i-1] = a


print(len(NUM))
