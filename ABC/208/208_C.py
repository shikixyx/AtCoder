import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    a_to_i = [(a, i) for i, a in enumerate(A)]
    a_to_i.sort()

    base = K // N
    rest = K % N

    ans = [base] * N

    for a, i in a_to_i:
        if rest > 0:
            ans[i] += 1
            rest -= 1
        else:
            break

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
