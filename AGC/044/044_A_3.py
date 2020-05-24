import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC !!!

T = int(input())


@lru_cache(maxsize=None)
def dfs(n, A, B, C, D):
    # 1
    ans = n * D

    for mul, pt in [(2, A), (3, B), (5, C)]:
        if n % mul == 0:
            n1 = n // mul
            a = dfs(n1, A, B, C, D) + pt
            ans = min(a, ans)
        elif mul <= n:
            md = n % mul
            n1 = (n - md) // mul
            n2 = (n + mul - md) // mul
            a = dfs(n1, A, B, C, D) + (D * md) + pt
            b = dfs(n2, A, B, C, D) + ((mul - md) * D) + pt
            ans = min(a, b, ans)

    return ans


def solve():
    N, A, B, C, D = map(int, input().split())

    ans = dfs(N, A, B, C, D)
    print(dfs.cache_info())
    return ans


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
