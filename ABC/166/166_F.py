import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, A, B, C = map(int, input().split())
SS = [input() for _ in range(N)]

AB = A + B
BC = B + C
CA = C + A

cnt = [[0] * (N + 1) for _ in range(3)]

for i in range(N):
    s = SS[i]

    if 1 <= i:
        for j in range(3):
            cnt[j][i] = cnt[j][i - 1]

    if s == "AB":
        cnt[0][i] += 1
    elif s == "BC":
        cnt[1][i] += 1
    elif s == "AC":
        cnt[2][i] += 1

ANS = []
for i in range(N):
    s = SS[i]

    if s == 'AB':
        



