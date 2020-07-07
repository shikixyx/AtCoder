import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

r_bit = 1 << H
w_bit = 1 << W

# print(r_bit, w_bit)

ans = 0
for r in range(r_bit):
    n_row = []
    for i in range(H):
        if r & 1:
            n_row.append(i)
        r >>= 1

    for c in range(w_bit):
        # 使えない行、列

        n_col = []

        for j in range(W):
            if c & 1:
                n_col.append(j)
            c >>= 1

        cnt = 0
        for i in range(H):
            for j in range(W):
                if i in n_row or j in n_col:
                    continue
                if C[i][j] == "#":
                    cnt += 1

        if cnt == K:
            ans += 1

print(ans)

