import sys
import bisect
from functools import lru_cache
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE
# メモ化でやったけどかなり遅い

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

MOD = 10 ** 9 + 7

if N < M:
    N, M = M, N
    S, T = T, S


@lru_cache(maxsize=None)
def solve(i, j):
    arr1 = S[i:]
    arr2 = T[j:]

    if len(arr1) == 0 or len(arr2) == 0:
        return 1

    ans = 0
    t = arr2[0]

    if arr1[0] == arr2[0]:
        ans += solve(i + 1, j + 1) + 1
        ans %= MOD

    #ans += solve(i + 1, j)
    ans += solve(i, j+1)
    ans %= MOD

    #print("i,j,ans", i, j, ans)

    return ans


r = solve(0, 0)

print(r)
