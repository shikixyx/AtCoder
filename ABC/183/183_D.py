import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, W = map(int, input().split())
    STP = [list(map(int, input().split())) for _ in range(N)]

    L = 2 * 10 ** 5 + 10
    T = [[] for _ in range(L)]
    for s, t, p in STP:
        T[s].append(p)
        T[t].append(-p)

    K = [0] * L

    p = 0
    for i in range(L):
        if len(T[i]) != 0:
            for x in T[i]:
                p += x

        K[i] += p

    flg = True
    for i in range(L):
        if K[i] > W:
            flg = False
            break

    if flg:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
