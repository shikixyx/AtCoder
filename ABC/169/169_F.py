import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, S = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353

DP = [0] * (S + 10)

for a in A:
    DP[a] += 1
    for i in range(S + 1 - a):
        if DP[i]:
            DP[i + a] = DP[i] + 1



