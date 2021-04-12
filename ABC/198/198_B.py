import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = input()

    flg = False
    for i in range(20):
        NN = "0" * i + N
        R_NN = NN[::-1]

        if NN == R_NN:
            flg = True

    if flg:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
