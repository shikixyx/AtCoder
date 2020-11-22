import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    UVC = [list(map(int, input().split())) for _ in range(M)]

    label = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
    forbid = [[] for _ in range(N + 1)]
    PATH = [[] for _ in range(N + 1)]
    USED = [False] * (N + 1)

    for u, v, c in UVC:
        PATH[u].append(v)
        PATH[v].append(u)
        label[u][v].append(c)
        label[v][u].append(c)

    ans = [0] * (N + 1)
    stack = [(1, 1)]
    while stack:
        u, t = stack.pop()
        if USED[u]:
            continue

        ans[u] = t
        USED[u] = True

        for v in PATH[u]:
            if USED[v]:
                continue

            candidate = label[u][v]

            s = -1
            for ns in candidate:
                if t == ns:
                    continue

                s = ns
                break

            if s == -1:
                s = t + 1
                if s > N:
                    s = 1

            stack.append((v, s))
            USED[v] = True

    print("\n".join(map(str, ans[1:])))

    return


if __name__ == "__main__":
    main()
