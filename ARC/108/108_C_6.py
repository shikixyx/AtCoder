import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC


def main():
    N, M = map(int, input().split())
    UVC = [list(map(int, input().split())) for _ in range(M)]

    path = [[] for _ in range(N + 1)]

    for u, v, c in UVC:
        path[u].append((v, c))
        path[v].append((u, c))

    # make Tree
    used = [False] * (N + 1)
    tpath = [[] for _ in range(N + 1)]

    stack = [1]
    used[1] = True
    while stack:
        u = stack.pop()

        for v, c in path[u]:
            if used[v]:
                continue

            tpath[u].append((v, c))
            stack.append(v)
            used[v] = True

    ans = [1] * (N + 1)

    stack = [(1, 1)]
    while stack:
        u, t = stack.pop()
        ans[u] = t

        for v, c in tpath[u]:
            if c == t:
                c = t + 1
                if c > N:
                    c = 1

            stack.append((v, c))

    print("\n".join(map(str, ans[1:])))

    return


if __name__ == "__main__":
    main()
