import sys
import itertools


sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]


ans = 0
for lst in itertools.combinations_with_replacement(range(1, M + 1), N):
    s = 0
    for a, b, c, d in ABCD:
        if (lst[b - 1] - lst[a - 1]) == c:
            s += d

    ans = max(ans, s)

print(ans)
