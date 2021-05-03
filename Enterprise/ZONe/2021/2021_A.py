import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = input()
    print(S.count("ZONe"))

    return


if __name__ == "__main__":
    main()
