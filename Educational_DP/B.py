import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())
H = list(map(int, input().split()))

INF = 10 ** 10
dp = [INF] * (10 ** 5 + 10)
H += [H[-1] * K]

dp[0] = 0

for i in range(N):
    for k in range(1, K + 1):
        if i + k <= N:
            dp[i + k] = min(dp[i + k], dp[i] + abs(H[i + k] - H[i]))


print(dp[N-1])
