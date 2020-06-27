import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

CNT = defaultdict(int)

for a in A:
    CNT[a] += 1

TOTAL = sum(A)

ANS = []
for b, c in QUERY:
    TOTAL += (c - b) * CNT[b]
    CNT[c] += CNT[b]
    CNT[b] = 0
    ANS.append(TOTAL)

print("\n".join(map(str, ANS)))

