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
R.sort()

P = P[:X]
Q = Q[:Y]

ans = sum(P[:X]) + sum(Q[:Y])

p = P.pop()
q = Q.pop()
r = R.pop()

INF = 10 ** 10


while True:
    m = min(p, q, r)

    if m == r or m == INF:
        break

    if m == p:
        ans += (r - p)

        if P:
            p = P.pop()
        else:
            p = INF
    elif m == q:
        ans += (r - q)

        if Q:
            q = Q.pop()
        else:
            q = INF

    if R:
        r = R.pop()
    else:
        break

print(ans)
