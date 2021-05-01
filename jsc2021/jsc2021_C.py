import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, input().split())

    m = B - A
    ans = 1
    for i in range(1, m + 1)[::-1]:
        sml = -(-A // i) * i
        big = sml + i
        if big <= B:
            ans = i
            break

    print(ans)

    return


if __name__ == "__main__":
    main()
