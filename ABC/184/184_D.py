import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


@lru_cache(maxsize=None)
def f(x, y, z):
    if x == 100 or y == 100 or z == 100:
        return 0

    xyz = x + y + z

    t = 0.0

    if x > 0:
        t += (f(x + 1, y, z) + 1) * x / xyz
    if y > 0:
        t += (f(x, y + 1, z) + 1) * y / xyz
    if z > 0:
        t += (f(x, y, z + 1) + 1) * z / xyz

    return t


def main():
    x, y, z = map(int, input().split())
    ans = f(x, y, z)
    print(ans)
    return


if __name__ == "__main__":
    main()
