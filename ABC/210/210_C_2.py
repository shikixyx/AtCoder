import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    count = defaultdict(int)

    t = 0
    for i in range(K):
        count[C[i]] += 1
        if count[C[i]] == 1:
            t += 1

    ans = t

    for i in range(1, N - K + 1):
        t = ans
        count[C[i - 1]] -= 1
        if count[C[i - 1]] == 0:
            t -= 1

        count[C[i + K - 1]] += 1
        if count[C[i + K - 1]] == 1:
            t += 1

        ans = max(ans, t)

    print(ans)

    return


if __name__ == "__main__":
    main()
