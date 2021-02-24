import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ANS = [a for a in A if a != X]
    print(" ".join(map(str, ANS)))
    return


if __name__ == "__main__":
    main()
