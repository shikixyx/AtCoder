import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


# nの約数列挙
def divisor(n):
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if i ** 2 == n:
                continue
            ans.append(n // i)
    return ans  # sortされていない


def main():
    N = int(input())
    N = N * 2

    if N == 1 or N == -1:
        print(2)
        return

    divs = divisor(N)

    ans = 0
    for n in divs:
        Y = n - 1
        G = N // n
        if (G - Y) % 2 == 0:
            ans += 1

    print(ans)

    return


if __name__ == "__main__":
    main()
