import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

# A1 ... AnのBIT(1-indexed)
N = H
BIT = [0] * (N + 1)

tate_min_m = [H + 1] * (W + 1)
m_col = [[] for _ in range(W + 1)]

for x, y in XY:
    m_col[y].append(x)
    tate_min_m[y] = min(tate_min_m[y], x)


BLOCK = [False] * (H + 1)

# A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx & (-idx)
    return res_sum


# Ai += x O(logN)
def BIT_update(idx, x):
    global N
    while idx <= N:
        BIT[idx] += x
        idx += idx & (-idx)
    return


ans = 0

for i in range(1, W + 1):
    t = tate_min_m[i]

    for x in m_col[i]:
        if not BLOCK[x]:
            BIT_update(x, 1)
            BLOCK[x] = True

    if t == (H + 1):
        ans += H
    else:
        ans += t - 1
        a = (H - t + 1) - (BIT_query(H) - BIT_query(t - 1))
        ans += a


print(ans)

