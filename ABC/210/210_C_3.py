import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, len(set(C[i : i + K])))

    print(ans)

    return


if __name__ == "__main__":
    main()
