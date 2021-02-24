import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve():
    X = int(input())
    M = int(input())
    L = len(str(X))

    if L == 1:
        if int(X) <= M:
            return 1
        else:
            return 0

    X = list(str(X))[::-1]
    start = int(max(X)) + 1

    t = 0
    for i in range(L):
        x = int(X[i])
        t += pow(start, i) * x

    if t > M:
        return 0

    right = start
    # left = int(M ** (1 / L)) + 10
    left = 10 ** 18 + 10

    if left < right:
        return 1

    while left - right != 1:
        mid = (left + right) // 2

        t = 0
        for i in range(L):
            x = int(X[i])
            t += pow(mid, i) * x

        if t > M:
            left = mid
        else:
            right = mid

    return right - start + 1


ans = solve()
print(ans)
