import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

USE = [False] * (N + 1)

CITY = [1]
nxt = A[1]
USE[1] = True

while not USE[nxt]:
    CITY.append(nxt)
    USE[nxt] = True
    nxt = A[nxt]

loop_start = nxt
loop_start_i = CITY.index(nxt)

if K <= loop_start_i:
    print(CITY[K])
    exit()

L = len(CITY) - loop_start_i

K = (K - loop_start_i) % L
print(CITY[K + loop_start_i])
