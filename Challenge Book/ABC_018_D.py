import itertools
import sys
sys.setrecursionlimit(10 ** 7)

# 半分全列挙
# 固定してGreedy

N, M, P, Q, R = map(int, input().split())

Z = [[] for _ in range(N+1)]
for _ in range(R):
    x, y, z = map(int, input().split())
    Z[x].append((y, z))

seq = range(N)
GIRLS = list()

ans = 0
for gs in itertools.combinations(seq, P):
    BOYS = [0] * (M+1)
    for g in gs:
        for y, z in Z[g+1]:
            BOYS[y] += z

    BOYS.sort(reverse=True)

    ans = max(ans, sum(BOYS[:Q]))

print(ans)
