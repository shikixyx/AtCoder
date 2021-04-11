import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B, W = map(int, input().split())
    W *= 1000
    sml = 10 ** 6 + 10
    big = 1
    flg = False
    for i in range(1, (10**6) + 10):
        if A * i <= W <= B * i:
            flg = True
            big = max(i, big)
            sml = min(i, sml)

    if flg:
        print("{} {}".format(sml, big))
    else:
        print("UNSATISFIABLE")

    return


if __name__ == "__main__":
    main()
