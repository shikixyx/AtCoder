import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 40min

H, W = map(int, input().split())
MEIJI = [input() for _ in range(H)]


@lru_cache(maxsize=None)
def dfs(r, c, cnt, iswhite=True):
    # if r == H - 1 and c == W - 1:
        # return cnt

    now = '.' if iswhite == True else '#'

    ans = 200

    if MEIJI[r][c] != now:
        if iswhite == True:
            cnt += 1

        iswhite = not (iswhite)

    if r == H-1 and c == W - 1:
        return cnt
    if r < H-1:
        ans = min(dfs(r + 1, c, cnt, iswhite), ans)
    if c < W-1:
        ans = min(dfs(r, c + 1, cnt, iswhite), ans)

    return ans


ans = dfs(0, 0, 0, True)
print(ans)
