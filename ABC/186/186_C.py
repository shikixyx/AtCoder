import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())

    c = 0
    for n in range(1, N + 1):
        s = str(n)
        if "7" in s:
            continue

        flg = True
        while n > 0:
            if n % 8 == 7:
                flg = False
                break

            n >>= 3

        if not flg:
            continue

        c += 1

    print(c)

    return


if __name__ == "__main__":
    main()
