import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


K = int(input())
S = list(input())

MOD = 10 ** 9 + 7

LS = len(S)
if K == 0:
    print(1)
    exit()

L = LS + K
DP = [[0] * (LS + 1) for _ in range(L + 10)]
DP[0][0] = 1

for i in range(L + 1):
    for j in range(LS + 1):
        if j < LS:
            DP[i + 1][j] += DP[i][j] * 25
        else:
            DP[i + 1][j] += DP[i][j] * 26

        DP[i + 1][j] %= MOD

        if j >= 1:
            DP[i + 1][j] += DP[i][j - 1]

        DP[i + 1][j] %= MOD


print(DP[L][LS])
