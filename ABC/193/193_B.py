import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    APX = [list(map(int, input().split())) for _ in range(N)]

    flg = False
    ans = 10 ** 10

    for a, p, x in APX:
        if x - a > 0:
            flg = True
            ans = min(ans, p)

    if flg:
        print(ans)
    else:
        print(-1)
    return


if __name__ == "__main__":
    main()
