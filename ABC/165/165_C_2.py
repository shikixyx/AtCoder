import sys
import itertools


sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]


def calsScore(lst):
    s = 0
    for a, b, c, d in ABCD:
        if (lst[b - 1] - lst[a - 1]) == c:
            s += d
    return s


import copy


def dfs(i, lst, N):
    ans = 0
    lst.append(i)
    N -= 1

    if N == 0:
        return calsScore(lst)
    else:
        for j in range(i, M + 1):
            nlst = copy.copy(lst)
            ans = max(dfs(j, nlst, N), ans)

    return ans


ans = dfs(1, [], N)
print(ans)
