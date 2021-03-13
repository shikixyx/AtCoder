import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    D = [a * a for a in A]
    accD = list(itertools.accumulate(D))
    accA = list(itertools.accumulate(A))

    ans = 0
    for i in range(N-1):
        t1 = accD[N-1] - accD[i]
        t2 = D[i] * (N - i - 1)
        t3 = 2 * A[i] * (accA[N-1] - accA[i])

        # print(t1, t2, t3, t1+t2-t3)
        ans += t1 + t2 - t3

    print(ans)

    return


if __name__ == "__main__":
    main()
