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
    ans = [1] * (N + 1)

    stack = [(1, 1, -1)]
    while stack:
        u, t, parent = stack.pop()
        ans[u] = t
        used[u] = True

        for v, c in path[u]:
            if used[v] or v == parent:
                continue

            if c == t:
                c += 1
                if c > N:
                    c = 1

            stack.append((v, c, u))
            used[v] = True

    print("\n".join(map(str, ans[1:])))

    return


if __name__ == "__main__":
    main()
