import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for j in range(M + 1):
        dp[0][j] = j

    for i in range(N + 1):
        dp[i][0] = i

    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1)

            if A[i] == B[j]:
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j + 1])
            else:
                dp[i + 1][j + 1] = min(dp[i][j] + 1, dp[i + 1][j + 1])

    # print(dp)
    print(dp[N][M])

    return


if __name__ == "__main__":
    main()
