import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W, N, M = map(int, input().split())
LIGHT = [[False] * W for _ in range(H)]
BLOCK = [[False] * W for _ in range(H)]

FLUSH = [[False] * W for _ in range(H)]

AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]


for a, b, in AB:
    LIGHT[a - 1][b - 1] = True

for c, d in CD:
    BLOCK[c - 1][d - 1] = True

# まずは横
for y in range(H):
    flg = False

    for x in range(W):
        # ブロックがあればスルー、flgをオフ
        if BLOCK[y][x]:
            flg = False
            continue

        # ライトがあればflgをTrue
        if LIGHT[y][x]:
            flg = True
            FLUSH[y][x] = True
            continue

        # どちらもなければ、flg次第
        if flg:
            FLUSH[y][x] = True

    flg = False
    for x in range(W)[::-1]:
        # ブロックがあればスルー、flgをオフ
        if BLOCK[y][x]:
            flg = False
            continue

        # ライトがあればflgをTrue
        if LIGHT[y][x]:
            flg = True
            FLUSH[y][x] = True
            continue

        # どちらもなければ、flg次第
        if flg:
            FLUSH[y][x] = True


# まずは横
for x in range(W):
    flg = False

    for y in range(H):
        # ブロックがあればスルー、flgをオフ
        if BLOCK[y][x]:
            flg = False
            continue

        # ライトがあればflgをTrue
        if LIGHT[y][x]:
            flg = True
            FLUSH[y][x] = True
            continue

        # どちらもなければ、flg次第
        if flg:
            FLUSH[y][x] = True

    flg = False
    for y in range(H)[::-1]:
        # ブロックがあればスルー、flgをオフ
        if BLOCK[y][x]:
            flg = False
            continue

        # ライトがあればflgをTrue
        if LIGHT[y][x]:
            flg = True
            FLUSH[y][x] = True
            continue

        # どちらもなければ、flg次第
        if flg:
            FLUSH[y][x] = True


ans = 0
for r in range(H):
    for c in range(W):
        if FLUSH[r][c]:
            ans += 1

print(ans)

