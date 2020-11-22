import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    UVC = [list(map(int, input().split())) for _ in range(M)]

    # ここで O(N^2)の配列を作るのはイケテナイ。めちゃ重い。
    label = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
    # path = [[] for _ in range(N + 1)]
    path = [set() for _ in range(N + 1)]

    for u, v, c in UVC:
        # path[u].append(v)
        # path[v].append(u)
        path[u].add(v)
        path[v].add(u)
        label[u][v].append(c)
        label[v][u].append(c)

    for i in range(N + 1):
        path[i] = list(path[i])

    # make Tree
    used = [False] * (N + 1)
    tpath = [[] for _ in range(N + 1)]

    stack = [1]
    while stack:
        u = stack.pop()
        if used[u]:
            continue

        used[u] = True

        for v in path[u]:
            if used[v]:
                continue

            tpath[u].append((v, label[u][v][0]))
            # tpath[u].append((v, 1))
            stack.append(v)
            used[v] = True

    ans = [1] * (N + 1)

    stack = [(1, 1, -1)]
    while stack:
        u, t, parent = stack.pop()
        ans[u] = t

        for v, c in tpath[u]:
            if v == parent:
                continue
            if c != t:
                stack.append((v, c, u))
            else:
                c += 1
                if c > N:
                    c = 1

                stack.append((v, c, u))

    print("\n".join(map(str, ans[1:])))

    return


if __name__ == "__main__":
    main()
