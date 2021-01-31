import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    m = max(A)
    m_i = A.index(m)

    half = 2 ** (N - 1)

    ans = 0
    if m_i >= half:
        s = max(A[:half])
        ans = A.index(s)
    else:
        s = max(A[half:])
        ans = A.index(s)

    print(ans + 1)

    return


if __name__ == "__main__":
    main()
