import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    C = [list(input()) for _ in range(N)]

    DP = [[[0] * 2 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            for x in ["B", "W"]:
                t = 0

                # 上みる
                if 0 < i:
                    pass

                # 左みる

            if C[i][j] == "B":
                DP[i][j][1] = -1
            elif C[i][j] == "W":
                DP[i][j][0] = -1

    return


if __name__ == "__main__":
    main()
