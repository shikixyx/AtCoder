import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            t = int(str(i) + str(j).zfill(2))
            cnt += t

    print(cnt)

    return


if __name__ == "__main__":
    main()
