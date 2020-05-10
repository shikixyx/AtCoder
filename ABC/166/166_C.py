import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
H = [-1] + list(map(int, input().split()))

GOOD = [True] * (N + 1)
GOOD[0] = False
for _ in range(M):
    A, B = map(int, input().split())

    HA = H[A]
    HB = H[B]

    if HA == HB:
        GOOD[A] = False
        GOOD[B] = False
    elif HA < HB:
        GOOD[A] = False
    elif HB < HA:
        GOOD[B] = False

cnt = 0
for i in range(N + 1):
    if GOOD[i]:
        cnt += 1

print(cnt)
