import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A = list(map(int,input().split()))
    A.sort()
    print(A[2] + A[1])

    return


if __name__ == "__main__":
    main()
