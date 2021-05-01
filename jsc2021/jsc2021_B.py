import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = []
    for i in range(1, (10 ** 3) + 10):
        if i in A and i in B:
            continue

        if not i in A and not i in B:
            continue

        ans.append(i)

    print(" ".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
