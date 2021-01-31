import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    t = 0
    for i in range(N):
        t += A[i] * B[i]

    if t == 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
