import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

fct = [1]
for i in range(1, 32):
    f = fct[-1]
    fct.append(f * i)


def comb(n, k):
    return fct[n] // fct[n - k] // fct[k]


def solve(A, B, K):
    print("==== A={},B={},K={}".format(A, B, K))
    if A == 0:
        return "b" * B

    if B == 0:
        return "a" * A

    L = A + B
    ans = ""

    # 先頭にaがいくつか
    for i in range(1, A + 1)[::-1]:
        # print("i: {},t: {}".format(i, t))
        t = 0

        if i == A:
            t = comb(L - i, A - i)
        else:
            t = comb(L - i - 1, A - i - 1)

        print("a i={} t={} K={}".format(i, t, K))

        if K <= t:
            ans += "a" * i + "b"
            ans += solve(A - i, B - 1, K - t)

            return ans
        else:
            K -= t

    # 先頭にbがいくつか
    for i in range(1, B + 1):

        
        t = comb(L - i, B - i)

        if K <= t:
            ans += "b" * i + "a"
            ans += solve(A - 1, B - i, K - t)
            return ans

        else:
            K -= t

    return ans


def main():
    A, B, K = map(int, input().split())
    ans = solve(A, B, K)
    print(ans)

    return


if __name__ == "__main__":
    main()
