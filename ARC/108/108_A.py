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
    S, P = map(int, input().split())
    ds = divisor(P)
    ds.sort()

    ans = False
    for d in ds:
        s = P // d
        if s + d == S:
            ans = True
            break

    if ans:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
