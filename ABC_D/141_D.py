import sys
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]
heapify(A)

for _ in range(M):
    a = heappop(A)
    if a == 0:
        break
    a = -(-a // 2)
    heappush(A, a)

ans = -sum(A)
print(ans)
