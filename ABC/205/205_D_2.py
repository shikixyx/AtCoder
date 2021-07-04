import sys
import bisect

sys.setrecursionlimit(10 ** 7)

# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    setA = set(A)

    K = [(int(input()), i) for i in range(Q)]
    K.sort()

    ans = [0] * Q
    for k, i in K:
        t = k
        p = bisect.bisect_left(A, t)
        num = k - p

        while num != k or (num == k and t in setA):
            if not t in setA:
                num += 1

            t += 1

        ans[i] = t

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
