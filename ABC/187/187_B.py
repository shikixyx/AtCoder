import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for a, b in itertools.combinations(XY, 2):
        xa, ya = a
        xb, yb = b

        if xa == xb:
            continue

        d = (yb - ya) / (xb - xa)

        if -1 <= d <= 1:
            ans += 1

    print(ans)

    return


if __name__ == "__main__":
    main()
