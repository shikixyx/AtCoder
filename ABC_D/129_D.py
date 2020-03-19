import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE
# O(HW(H+W)) で10^8になるので無理

H, W = map(int, input().split())

#S = [[0 if x == '.' else 1 for x in list(input())] for _ in range(H)]
S = [list(input()) for _ in range(H)]
NUM = [[[None] * 2 for _ in range(W)] for _ in range(H)]


def cntDot(r, c, vertical, cnt):
    #print("Input", r, c, vertical, cnt)
    if S[r][c] == '#':
        NUM[r][c][vertical] = 0
        return cnt
    else:
        cnt += 1

    # x軸
    if vertical == 0:
        if c < W - 1:
            t = cntDot(r, c + 1, vertical, cnt)
            NUM[r][c][vertical] = t
            return t
        else:
            NUM[r][c][vertical] = cnt
            return cnt

    # y軸
    if vertical == 1:
        if r < H - 1:
            t = cntDot(r + 1, c, vertical, cnt)
            NUM[r][c][vertical] = t
            return t
        else:
            NUM[r][c][vertical] = cnt
            return cnt

    return 0


for r in range(H):
    for c in range(W):
        if S[r][c] == 1:
            NUM[r][c] = [0, 0]
            continue
        # x軸
        if NUM[r][c][0] == None:
            NUM[r][c][0] = cntDot(r, c, 0, 0)
        # y軸
        if NUM[r][c][1] == None:
            NUM[r][c][1] = cntDot(r, c, 1, 0)

# print(NUM)

ans = 1
for r in range(H):
    v = max(NUM[r])
    ans = max(ans, sum(v)-1)

print(ans)
