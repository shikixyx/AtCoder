import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    A = [0] + A
    A += [N + 1]

    L = []
    for i in range(M + 1):
        t = A[i + 1] - A[i] - 1
        if t == 0:
            continue

        L.append(t)

    if len(L) == 0:
        print(0)
        return

    k = min(L)
    ans = 0

    for l in L:
        ans += -(-l // k)

    print(ans)

    return


if __name__ == "__main__":
    main()
