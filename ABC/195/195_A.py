import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    M, H = map(int, input().split())

    if H % M == 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
