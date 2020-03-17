import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 30min

N, K = map(int, input().split())
V = list(map(int, input().split()))


def solve(l, r):
    get = V[:l] + (V[-r:] if r != 0 else [])
    get.sort()
    minus = [x for x in get if x < 0]
    plus = [x for x in get if x >= 0]

    s = sum(plus) + sum(minus[K-l-r:])

    if (l + r) < N and (l + r) < K:
        get_left = solve(l + 1, r)
        get_right = solve(l, r + 1)
        s = max(s, get_left, get_right)

    return s


ans = solve(0, 0)

print(ans)
