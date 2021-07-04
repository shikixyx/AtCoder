import sys
import bisect
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    MEMO = {}
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    setA = set(A)

    K = [int(input()) for _ in range(Q)]

    ans = []
    for k in K:
        left = k
        right = 10 ** 18 + 10

        flg = False
        while (right - left) != 1:
            mid = (left + right) // 2

            num = 0
            if mid in MEMO:
                num = MEMO[mid]
            else:
                num = mid - bisect.bisect_left(A, mid)
                MEMO[mid] = num

            if num == k:
                if mid in setA:
                    left = mid
                else:
                    ans.append(mid)
                    flg = True
                    break
            elif num > k:
                right = mid
            else:
                left = mid

        if not flg:
            num = left - bisect.bisect_left(A, left)
            if num == k and not left in setA:
                ans.append(left)
            else:
                ans.append(right)

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
