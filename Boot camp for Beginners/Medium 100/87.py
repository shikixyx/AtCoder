import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = np.array(input().split(), dtype="int64")
    B = np.array(input().split(), dtype="int64")

    diff = A - B

    if diff.sum() < 0:
        print("-1")
        return

    minus = diff[diff < 0]
    plus = diff[diff > 0]

    plus = np.sort(plus)[::-1]
    need = -minus.sum()

    if need == 0:
        print("0")
        return

    acc_plus = np.cumsum(plus)
    ans = np.searchsorted(acc_plus, need) + 1 + len(minus)

    print(ans)

    return


if __name__ == "__main__":
    main()
