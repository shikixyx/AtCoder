import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, input().split())
    C = A - B
    print(C / A * 100)
    return


if __name__ == "__main__":
    main()
