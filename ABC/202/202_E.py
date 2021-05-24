import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    P = [0] + list(map(int, input().split()))
    Q = int(input())
    UD = [list(map(int, input().split())) for _ in range(Q)]

    DAN = [0] * (N + 10)
    PATH = [[] for _ in range(N + 10)]

    for i in range(1, N):
        parent = P[i]
        PATH[parent].append(i + 1)

    QUE = [(1, 0)]
    while QUE:
        u, d = QUE.pop()
        DAN[u] = d

        for v in PATH[u]:
            QUE.append((v, d + 1))

    CNT = [{} for _ in range(N + 10)]

    # 数えるべきとこ
    TO_CNT = [set() for _ in range(N + 10)]
    for u, d in UD:
        if DAN[u] <= d:
            TO_CNT[d].add(DAN[u])

    QUE = [(1, [1])]
    while QUE:
        


    return


if __name__ == "__main__":
    main()
