import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = [[0] * 3010 for _ in range(3010)]

    acc = list(itertools.accumulate(A))

    for num in range(1, N + 1):
        for start in range(N):
            if N < start + num:
                break

            t = acc[start + num - 1]
            if start > 0:
                t -= acc[start - 1]

            if t % num == 0:
                count[num][start] = 1

    print(count[3][:N])

    return


if __name__ == "__main__":
    main()
