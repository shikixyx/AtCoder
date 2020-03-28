from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 60min
# 制約の厳しい方から

N, M = map(int, readline().split())
AB = [[int(x) for x in readline().split()] for _ in range(N)]

AB.sort()

STOCK = []
ans = 0

idx = 0
for d in range(1, M+1):
    for i in range(idx, N):
        a, b = AB[i]
        if a <= d:
            heappush(STOCK, -b)
            idx += 1
        else:
            break

    if STOCK:
        p = heappop(STOCK)
        ans -= p


print(ans)
