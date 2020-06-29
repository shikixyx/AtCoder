import sys
import itertools
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_acc = list(itertools.accumulate(A))
B_acc = list(itertools.accumulate(B))

all_a = bisect.bisect_right(A_acc, K)
all_b = bisect.bisect_right(B_acc, K)

ans = max(all_a, all_b)

for i in range(N):
    rest = K - A_acc[i]

    if rest <= 0:
        break

    b = bisect.bisect_right(B_acc, rest)

    ans = max(ans, i + b + 1)

print(ans)
