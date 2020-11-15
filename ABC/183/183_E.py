import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    T = [[[0, 0, 0, 0] for _ in range(W)] for _ in range(H)]
    T[0][0][0] = 1
    T[0][0][1] = 1
    T[0][0][2] = 1
    T[0][0][3] = 1

    for r in range(H):
        for c in range(W):
            if r == 0 and c == 0:
                continue

            if S[r][c] == "#":
                continue

            # 持ってきて足す
            # 1: 縦
            # 2: 横
            # 3: 斜め

            cnt = 0

            # 上
            if 0 <= (r - 1):
                cnt += T[r - 1][c][1]
                cnt %= MOD

            # 左
            if 0 <= (c - 1):
                cnt += T[r][c - 1][2]
                cnt %= MOD

            # 左上
            if 0 <= (r - 1) and 0 <= (c - 1):
                cnt += T[r - 1][c - 1][3]
                cnt %= MOD

            T[r][c][0] = cnt
            T[r][c][1] = cnt
            T[r][c][2] = cnt
            T[r][c][3] = cnt

            # 更新
            # 上
            if 0 <= (r - 1):
                T[r][c][1] += T[r - 1][c][1]

            # 左
            if 0 <= (c - 1):
                T[r][c][2] += T[r][c - 1][2]

            # 左上
            if 0 <= (r - 1) and 0 <= (c - 1):
                T[r][c][3] += T[r - 1][c - 1][3]

            T[r][c][1] %= MOD
            T[r][c][2] %= MOD
            T[r][c][3] %= MOD

    ans = T[H - 1][W - 1][0] % MOD
    print(ans)

    return


if __name__ == "__main__":
    main()
