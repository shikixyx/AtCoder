import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[0 for i in range(N + 1)] for j in range(M + 1)]  # 0で初期化

    for i in range(M):
        for j in range(N):
            if A[j] == B[i]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    t = dp[M][N]
    print(dp)
    ans = (N - t) + (M - t)
    print(ans)
    return


if __name__ == "__main__":
    main()
