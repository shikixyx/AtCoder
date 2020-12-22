import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    s = 0
    m = 1000
    for aa in A:
        m = min(m, min(aa))
        s += sum(aa)

    s -= m * H * W
    print(s)

    return


if __name__ == "__main__":
    main()
