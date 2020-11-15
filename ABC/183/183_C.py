import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    lst = [x for x in range(1, N)]

    ans = 0

    for l in itertools.permutations(lst):
        c = 0
        prev = 0

        for x in l:
            c += T[prev][x]
            prev = x

        c += T[prev][0]

        if K == c:
            ans += 1

    print(ans)

    return


if __name__ == "__main__":
    main()
