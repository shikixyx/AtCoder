import itertools
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE

N = int(input())
A = list(map(int, input()))

if N == 1:
    print(A[0])
    exit()
elif N == 2:
    print(abs(A[0] - A[1]))
    exit()

TRI = [[[0] * 4 for _ in range(4)] for _ in range(4)]

for a, b, c in itertools.product(range(1, 4), repeat=3):
    p = abs(a - b)
    q = abs(b - c)
    r = abs(p - q)
    TRI[a][b][c] = r


@lru_cache(maxsize=None)
def F(i, j):
    if i == 3:
        a = A[j - 1]
        b = A[j]
        c = A[j + 1]
        return TRI[a][b][c]

    a = F(i - 1, j)
    b = F(i - 1, j + 1)
    r = abs(a - b)

    return r


ans = F(N, 1)

print(ans)
