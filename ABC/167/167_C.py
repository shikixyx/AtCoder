import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, X = map(int, input().split())
CAS = [list(map(int, input().split())) for _ in range(N)]

bit = 2 << 12

ANS = 10 ** 10
ok = False
for i in range(bit):
    USE = [False] * N

    for j in range(N):
        USE[j] = i & 1
        i >>= 1

    m = 0
    POINTS = [0] * M
    for j in range(N):
        if not USE[j]:
            continue

        m += CAS[j][0]

        for k in range(M):
            POINTS[k] += CAS[j][k + 1]

    P = [X <= p for p in POINTS]

    if all(P):
        ok = True
        ANS = min(ANS, m)


if not ok:
    print("-1")
else:
    print(ANS)
