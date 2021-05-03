import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, D, H = map(int, input().split())
    dh = [list(map(int, input().split())) for _ in range(N)]

    y = 0

    for d, h in dh:
        if h == 0:
            continue

        t = -((H - h) * d) + ((D - d) * h)

        if t < 0:
            continue

        t /= D - d

        y = max(y, t)

    print(min(1000, max(y, 0)))

    return


if __name__ == "__main__":
    main()
