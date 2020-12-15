import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


@lru_cache(maxsize=None)
def devide(l, c):
    ret = 0

    if c == 0:
        return 1

    if l <= c:
        return 0
    for i in range(1, l):
        ret += devide(l - i, c - 1)

    return ret


def main():
    L = int(input())

    ans = devide(L, 11)

    print(ans)

    return


if __name__ == "__main__":
    main()
