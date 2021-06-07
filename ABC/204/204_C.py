import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())

    AB = [list(map(int, input().split())) for _ in range(M)]

    path = [[] for _ in range((N + 10))]
    for a, b in AB:
        path[a].append(b)

    ans = 0

    for i in range(1, N + 1):
        visited = [0] * (N + 10)
        visited[i] = 1
        q = [i]
        while q:
            u = q.pop()
            for v in path[u]:
                if visited[v]:
                    continue

                q.append(v)
                visited[v] = 1

        ans += sum(visited)

    print(ans)

    return


if __name__ == "__main__":
    main()
