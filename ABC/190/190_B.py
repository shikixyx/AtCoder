import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x, y in XY:
        if x >= S or y <= D:
            continue

        ans += y

    if ans > 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
