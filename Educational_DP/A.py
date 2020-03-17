import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 典型DP

N = int(input())
H = list(map(int, input().split()))

H += [H[-1]] * 2

INF = 10 ** 10
dp = [INF] * (N+1)
dp[0] = 0

for i in range(N):
    if i + 1 <= N:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i + 1] - H[i]))
    if i + 2 <= N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i + 2] - H[i]))


print(dp[-1])
