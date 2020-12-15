import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A = list(map(int, input().split()))
    print(min(A))
    return


if __name__ == "__main__":
    main()
