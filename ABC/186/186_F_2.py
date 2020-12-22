import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

# A1 ... AnのBIT(1-indexed)
N = W
BIT = [0] * (N + 1)

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


# 行と列毎の障害物
m_col = [[] for _ in range(W + 1)]
m_row = [[] for _ in range(H + 1)]

for x, y in XY:
    m_col[y].append(x)
    m_row[x].append(y)

# 1行目/1列目に障害物があれば、そこは埋める
w_limit = W + 1
h_limit = H + 1

if len(m_row[1]) != 0:
    w_limit = min(m_row[1])
    m_row[1] = list(range(w_limit, W + 1))

if len(m_col[1]) != 0:
    h_limit = min(m_col[1])
    m_col[1] = list(range(h_limit, H + 1))

ans = 0

# 右に行って下に行くパターン
for i in range(1, w_limit):
    if len(m_col[i]) == 0:
        ans += H
    else:
        ans += min(m_col[i]) - 1

# 下に行って右に行くパターン
# 上に障害物があるところだけ足す
BLOCK = [False] * (W + 1)

for i in range(1, h_limit):
    if len(m_row[i]) == 0:
        ans += BIT_query(W)
    else:
        c = min(m_row[i])
        ans += BIT_query(c - 1)

        for y in m_row[i]:
            if not BLOCK[y]:
                BIT_update(y, 1)
                BLOCK[y] = True

print(ans)

