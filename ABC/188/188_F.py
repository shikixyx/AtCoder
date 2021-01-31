import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    X, Y = map(int, input().split())

    print(dfs(X, Y))

    return


@lru_cache(maxsize=None)
def dfs(X, Y):
    c = 0

    # 同じ
    if X == Y:
        return 0

    # Yの方が小さい
    if X > Y:
        return X - Y

    # Xの方が小さい時

    # 1減らす
    c = Y - X

    # Yが奇数
    if Y % 2 == 1:
        c = min(dfs(X, (Y + 1) // 2) + 2, c)
        c = min(dfs(X, (Y - 1) // 2) + 2, c)
    # Yが偶数
    else:
        c = min(dfs(X, Y // 2) + 1, c)

    return c


if __name__ == "__main__":
    main()
