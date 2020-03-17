import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
ABC = [[int(x) for x in readline().split()] for _ in range(N)]

dp = [[0] * 3 for _ in range(10 ** 5 + 10)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] + ABC[i][k])

ans = max(dp[N])
print(ans)
