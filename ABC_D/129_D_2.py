import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 60min
# 解答見た
# PyPy3(2.4.0)

H, W = map(int, input().split())

S = [input() for _ in range(H)]
NUM = [[0] * (W) for _ in range(H)]

for r in range(H):
    cnt = 0
    for c in range(W):
        if S[r][c] == '#':
            cnt = 0
        else:
            cnt += 1
            NUM[r][c] += cnt

    cnt = 0
    for c in range(W - 1, -1, -1):
        if S[r][c] == '#':
            cnt = 0
        else:
            cnt += 1
            NUM[r][c] += cnt

for c in range(W):
    cnt = 0
    for r in range(H):
        if S[r][c] == '#':
            cnt = 0
        else:
            cnt += 1
            NUM[r][c] += cnt

    cnt = 0
    for r in range(H - 1, -1, -1):
        if S[r][c] == '#':
            cnt = 0
        else:
            cnt += 1
            NUM[r][c] += cnt

ans = 4
for i in range(H):
    t = max(NUM[i])
    ans = max(ans, t)

print(ans-3)
