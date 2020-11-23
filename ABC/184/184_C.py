import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    if a == c and b == d:
        return 0

    # 1手
    if abs(a - c) + abs(b - d) <= 3:
        return 1

    if (a + b) == (c + d):
        return 1

    if (a - b) == (c - d):
        return 1

    # 2手
    # 普通に2回
    if abs(a - c) + abs(b - d) <= 6:
        return 2

    # 一番近いところまで移動
    # 右上軸
    X = (-a + c - b + d) // 2
    na = a + X
    nb = b + X

    for p, q in [(na, nb), (na + 1, nb + 1), (na - 1, nb - 1)]:
        if abs(p - c) + abs(q - d) <= 3:
            return 2

        if (na + nb) == (c + d):
            return 2

        if (na - nb) == (c - d):
            return 2

    # 左上軸
    X = (a - c - b + d) // 2
    na = a - X
    nb = b + X

    for p, q in [(na, nb), (na - 1, nb + 1), (na + 1, nb - 1)]:
        if abs(p - c) + abs(q - d) <= 3:
            return 2

        if (na + nb) == (c + d):
            return 2

        if (na - nb) == (c - d):
            return 2

    return 3


def main():
    ans = solve()

    print(ans)
    return


if __name__ == "__main__":
    main()
