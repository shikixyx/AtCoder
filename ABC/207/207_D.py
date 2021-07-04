import sys
import itertools

sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    cd = [list(map(int, input().split())) for _ in range(N)]

    for x, y in itertools.product(range(N), repeat=2):
        print(x, y)

    return


if __name__ == "__main__":
    main()
