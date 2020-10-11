import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

cnt = 0
for r in range(H):
    for c in range(W):
        cur = S[r][c]
        if cur == "#":
            continue
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= r + x < H and 0 <= c + y < W:
                if S[r + x][c + y] == ".":
                    cnt += 1

print(cnt // 2)

