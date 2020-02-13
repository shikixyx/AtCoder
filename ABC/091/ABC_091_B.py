import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

CARDS = defaultdict(int)
N = int(input())

for _ in range(N):
    s = input()
    CARDS[s] += 1

M = int(input())

for _ in range(M):
    s = input()
    CARDS[s] -= 1

ans = 0
for v in CARDS.values():
    ans = max(v, ans)


print(ans)
