import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    P = int(input())

    ans = 0
    fact = [0] * 100
    t = 1
    for i in range(11):
        if i != 0:
            t *= i

        fact[i] = t

    for i in range(11)[::-1]:
        ans += P // fact[i]
        P %= fact[i]

    print(ans)

    return


if __name__ == "__main__":
    main()
