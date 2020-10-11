import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# この方法ではダメ
# 周りに番兵を置く必要がある

MOD = 10 ** 9 + 7

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

R_CNT = [[0] * W for _ in range(H)]
C_CNT = [[0] * W for _ in range(H)]

K = 0

for r in range(H):
    cnt = 0
    for c in range(W):
        if S[r][c] == "#":
            cnt = 0
        else:
            cnt += 1
            K += 1

        R_CNT[r][c] = cnt

for r in range(H):
    cnt = 0
    for c in range(W)[::-1]:
        if S[r][c] == "#":
            cnt = 0
        else:
            cnt = max(cnt, R_CNT[r][c])

        R_CNT[r][c] = cnt

for c in range(W):
    cnt = 0
    for r in range(H):
        if S[r][c] == "#":
            cnt = 0
        else:
            cnt += 1

        C_CNT[r][c] = cnt

for c in range(W):
    cnt = 0
    for r in range(H)[::-1]:
        if S[r][c] == "#":
            cnt = 0
        else:
            cnt = max(cnt, C_CNT[r][c])

        C_CNT[r][c] = cnt


pow2 = [1] * (K + 10)

x = 1
for i in range(1, K + 1):
    x *= 2
    x %= MOD
    pow2[i] = x


ans = 0
for r in range(H):
    for c in range(W):
        if S[r][c] == "#":
            continue

        cnt = R_CNT[r][c] + C_CNT[r][c] - 1

        # t = pow(2, cnt, MOD) - 1
        # t *= pow(2, K - cnt, MOD)

        t = pow2[cnt] - 1
        t *= pow2[K - cnt]
        t %= MOD

        ans += t
        ans %= MOD

print(ans)

