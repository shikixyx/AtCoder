import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

A_and_i = [[a, i] for i, a in enumerate(A)]
A_and_i.sort(reverse=True)

DP = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    a, idx = A_and_i[i]

    for j in range(N):
        # 右に持っていく
        if j <= i:
            DP[i + 1][j] = max(DP[i + 1][j], DP[i][j] +
                               a * abs(N - 1 - (i - j) - idx))
            DP[i + 1][j + 1] = max(DP[i + 1][j + 1], DP[i]
                                   [j] + a * abs(idx - j))

ans = max(DP[N])
print(ans)
