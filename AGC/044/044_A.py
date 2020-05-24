import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


@lru_cache(maxsize=None)
def dfs(n, A, B, C, D, P):
    if n == 0:
        return P

    ans = float("inf")

    # 1
    ans = min(ans, n * D)

    # 2
    t = P + A
    if n % 2 == 0:
        a = dfs(n // 2, A, B, C, D, t)
        ans = min(a, ans)
    else:
        a = dfs((n + 1) // 2, A, B, C, D, t + D) if n != 1 else float("inf")
        b = dfs((n - 1) // 2, A, B, C, D, t + D)
        ans = min(a, b, ans)

    # 3
    t = P + B
    if n % 3 == 0:
        a = dfs(n // 3, A, B, C, D, t)
        ans = min(a, ans)
    else:
        m = n % 3
        a = dfs((n - m) // 3, A, B, C, D, t + D * m)
        b = (
            dfs((n + 3 - m) // 3, A, B, C, D, t + (3 - m) * D)
            if n != 1
            else float("inf")
        )
        ans = min(a, b, ans)

    # 5
    t = P + D
    if n % 5 == 0:
        a = dfs(n // 5, A, B, C, D, t)
        ans = min(a, ans)
    else:
        m = n % 5
        a = dfs((n - m) // 3, A, B, C, D, t + D * m)
        b = (
            dfs((n + 5 - m) // 3, A, B, C, D, t + (5 - m) * D)
            if n != 1
            else float("inf")
        )
        ans = min(a, b, ans)

    return ans


def solve():
    N, A, B, C, D = map(int, input().split())

    ans = dfs(N, A, B, C, D, 0)
    return ans


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
