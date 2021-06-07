import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    T = list(map(int, input().split()))

    DP = [[0] * (10 ** 5 + 100) for _ in range(N + 1)]

    for i in range(N):
        DP[i][0] = 1

        t = T[i]

        for j in range(10 ** 5 + 10):
            if DP[i][j]:
                DP[i + 1][j] = 1
                DP[i + 1][j + t] = 1

    ans = sum(T)
    total = sum(T)
    for i in range(10 ** 5 + 10):
        if DP[N][i]:
            ans = min(max(i, total - i), ans)

    print(ans)

    return


if __name__ == "__main__":
    main()
