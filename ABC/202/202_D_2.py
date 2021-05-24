import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

fct = [1]
for i in range(1, 62):
    f = fct[-1]
    fct.append(f * i)


def comb(n, k):
    return fct[n] // fct[n - k] // fct[k]


def solve(A, B, K):
    ans = ""

    if A == 0:
        return "b" * B

    if B == 0:
        return "a" * A

    t = comb(A + B - 1, A - 1)
    if K <= t:
        ans += "a"
        ans += solve(A - 1, B, K)
    else:
        ans += "b"
        ans += solve(A, B - 1, K - t)

    return ans


def main():
    A, B, K = map(int, input().split())
    ans = solve(A, B, K)
    print(ans)
    return


if __name__ == "__main__":
    main()
