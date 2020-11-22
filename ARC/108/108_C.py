import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    UVC = [list(map(int, input().split())) for _ in range(M)]

    candidate = [[] for _ in range(N + 1)]
    forbid = [[] for _ in range(N + 1)]
    PATH = [[] for _ in range(N + 1)]
    USED = [False] * (N + 1)

    for u, v, c in UVC:
        PATH[u].append(v)
        PATH[v].append(u)
        candidate[u].append(c)
        candidate[v].append(c)

    ans = [0] * (N + 1)
    stack = [1]
    while stack:
        u = stack.pop()

        t = 0
        if candidate[u]:
            t = candidate[u][0]
        else:
            for i in range(1, N + 1):
                if i in forbid[u]:
                    continue

                t = i
                break

        ans[u].append(u)

    return


if __name__ == "__main__":
    main()
