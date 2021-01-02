import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, input().split())
    a, b = list(str(A)), list(str(B))

    da = sum(map(int, a))
    db = sum(map(int, b))

    print(max(da, db))

    return


if __name__ == "__main__":
    main()
