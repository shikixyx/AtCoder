import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A = list(map(int, input().split()))

    for x in itertools.permutations(A):
        if (x[2] - x[1]) == (x[1] - x[0]):
            print("Yes")
            return

    print("No")

    return


if __name__ == "__main__":
    main()
