import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())

    ans = 0.
    for i in range(1, N):
        ans += N / i

    print(ans)
    return


if __name__ == "__main__":
    main()
