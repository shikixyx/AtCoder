import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    C = [0] + list(map(int, input().split()))

    idx_B = [[] for _ in range(N + 10)]
    idx_C = [[] for _ in range(N + 10)]

    for i in range(1, N + 1):
        b = B[i]
        c = C[i]
        idx_B[b].append(i)
        idx_C[c].append(i)

    MEMO = [-1] * (N + 10)

    # print(idx_B)
    # print(idx_C)

    cnt = 0
    for i in range(1, N + 1):
        a = A[i]

        if MEMO[a] != -1:
            cnt += MEMO[a]
            continue

        t = 0
        if idx_B[a]:
            for b in idx_B[a]:
                t += len(idx_C[b])

        cnt += t
        MEMO[a] = t

    print(cnt)

    return


if __name__ == "__main__":
    main()
