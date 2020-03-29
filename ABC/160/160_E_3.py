import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC

X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

P = P[:X]
Q = Q[:Y]

ALL = P + Q + R
ALL.sort(reverse=True)

ans = sum(ALL[: X + Y])
print(ans)
