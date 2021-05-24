import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    ST = [list(input().split()) for _ in range(N)]

    ST.sort(key=lambda x: int(x[1]), reverse=True)
    print(ST[1][0])

    return


if __name__ == "__main__":
    main()
