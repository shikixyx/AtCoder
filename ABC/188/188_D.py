import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]

    days = defaultdict(int)

    for a, b, c in ABC:
        days[a] += c
        days[b + 1] -= c

    D = list(days.keys())
    D.sort()

    L = len(D)
    ans = 0
    t = 0
    for i in range(L - 1):
        d = D[i]
        t += days[d]

        cost = min(t, C)
        ans += (D[i + 1] - D[i]) * cost

    print(ans)

    return


if __name__ == "__main__":
    main()
