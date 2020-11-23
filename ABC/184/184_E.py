import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    dist = [[-1] * W for _ in range(H)]
    warp = defaultdict(list)

    start = None
    goal = None
    for i in range(H):
        for j in range(W):
            a = A[i][j]
            if a == "S":
                start = (i, j)
            elif a == "G":
                goal = (i, j)
            elif a == "." or a == "#":
                pass
            else:
                warp[a].append((i, j))

    Q = deque()
    Q.append((start[0], start[1], 0))
    visited = [[False] * W for _ in range(H)]

    while Q:
        x, y, d = Q.popleft()

        dist[x][y] = d
        visited[x][y] = True

        if x == goal[0] and y == goal[1]:
            break

        # 移動する
        for p, q in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if not (0 <= x + p < H and 0 <= y + q < W):
                continue

            nx = x + p
            ny = y + q
            na = A[nx][ny]

            if visited[nx][ny]:
                continue

            if na == "#":
                continue
            else:
                Q.append((nx, ny, d + 1))
                visited[nx][ny] = True

        # ワープ
        if not (A[x][y] == "#" or A[x][y] == "." or A[x][y] == "S" or A[x][y] == "G"):
            lst = warp[A[x][y]]

            for p, q in lst:
                if p == x and q == y:
                    continue
                if visited[p][q]:
                    continue

                Q.append((p, q, d + 1))
                visited[p][q] = True

            warp[A[x][y]] = []

    ans = dist[goal[0]][goal[1]]
    print(ans)

    return


if __name__ == "__main__":
    main()
