import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    X = int(input())
    Y = X + 1
    ans = -(-Y // 100) * 100
    print(ans - X)
    return


if __name__ == "__main__":
    main()
