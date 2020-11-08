import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    H, W, N, M = map(int, input().split())

    TYPE = [[0] * W for _ in range(H)]
    FLUSH = [[0] * W for _ in range(H)]

    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [list(map(int, input().split())) for _ in range(M)]

    for a, b, in AB:
        TYPE[a - 1][b - 1] = 1

    for c, d in CD:
        TYPE[c - 1][d - 1] = 2

    # まずは横
    for y in range(H):
        flg = False
        for x in range(W):
            t = TYPE[y][x]

            # ブロックがあればスルー、flgをオフ
            if t == 2:
                flg = False
                continue

            # ライトがあればflgをTrue
            if t == 1:
                flg = True
                FLUSH[y][x] = 1
                continue

            # どちらもなければ、flg次第
            if flg:
                FLUSH[y][x] = 1

    for y in range(H):
        flg = False
        for x in range(W - 1, -1, -1):
            t = TYPE[y][x]

            # ブロックがあればスルー、flgをオフ
            if t == 2:
                flg = False
                continue

            # ライトがあればflgをTrue
            if t == 1:
                flg = True
                FLUSH[y][x] = 1
                continue

            # どちらもなければ、flg次第
            if flg:
                FLUSH[y][x] = 1

    for x in range(W):
        flg = False
        for y in range(H):
            t = TYPE[y][x]

            # ブロックがあればスルー、flgをオフ
            if t == 2:
                flg = False
                continue

            # ライトがあればflgをTrue
            if t == 1:
                flg = True
                FLUSH[y][x] = 1
                continue

            # どちらもなければ、flg次第
            if flg:
                FLUSH[y][x] = 1

    for x in range(W):
        flg = False
        for y in range(H - 1, -1, -1):
            t = TYPE[y][x]

            # ブロックがあればスルー、flgをオフ
            if t == 2:
                flg = False
                continue

            # ライトがあればflgをTrue
            if t == 1:
                flg = True
                FLUSH[y][x] = 1
                continue

            # どちらもなければ、flg次第
            if flg:
                FLUSH[y][x] = 1

    ans = 0
    for r in range(H):
        ans += sum(FLUSH[r])

    print(ans)


if __name__ == "__main__":
    main()
