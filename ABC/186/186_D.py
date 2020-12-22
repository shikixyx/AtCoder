import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    accA = list(itertools.accumulate(A))

    ans = 0
    for i in range(N - 1):
        a = A[i]
        c = a * (N - i - 1)
        c -= accA[N - 1] - accA[i]

        ans += c

    print(ans)

    return


if __name__ == "__main__":
    main()
