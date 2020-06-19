import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    a, b, n = map(int, input().split())
    a, b = min(a, b), max(a, b)

    c = 0
    while b <= n:
        c += 1
        a, b = b, a + b

    return c


ans = []
for i in range(1, T + 1):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
