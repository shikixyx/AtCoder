import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    for a in A:
        cnt += max(a - 10, 0)

    print(cnt)

    return


if __name__ == "__main__":
    main()
