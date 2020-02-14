import sys
sys.setrecursionlimit(10 ** 7)

T = int(input())
CASE = []
for _ in range(T):
    n, m = map(int, input().split())
    CASE.append([n, m])

res = []
for n, m in CASE:
    zero_cnt = n - m
    p, q = divmod(zero_cnt, m+1)

    total = n * (n + 1) // 2

    if p == 0:
        total -= zero_cnt
    else:
        # m + 1 - q -> p
        total -= (p * (p + 1) // 2) * (m + 1 - q)

        # q -> p+1
        total -= ((p + 1) * (p + 2) // 2) * q

    res.append(str(total))


print("\n".join(res))
