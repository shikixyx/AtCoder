import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    a, b, c = map(int, input().split())

    d = [a, b, c]

    flg = False
    for i in range(1, 7):
        if d.count(i) == 2 or d.count(i) == 3:
            flg = True
            break

    if flg:
        for i in range(1, 7):
            if d.count(i) == 1 or d.count(i) == 3:
                print(i)
    else:
        print(0)

    return


if __name__ == "__main__":
    main()
