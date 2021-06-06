import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]

    has_porn = defaultdict(lambda: False)
    visited = defaultdict(lambda: False)


    return


if __name__ == "__main__":
    main()
