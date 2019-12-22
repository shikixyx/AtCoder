from collections import deque
import numpy as np


def bfs(N, u, path):
    d = [-1] * N
    d[u-1] = 0
    q = deque([])
    q.append(u-1)

    while(len(q) != 0):
        p = q.popleft()

        rs = path[p]

        for r in rs:
            if d[r] == -1:
                d[r] = d[p] + 1
                q.append(r)

    return d


def bfs2(N, u, path, d):
    e = [-1] * N
    e[u-1] = 0
    q = deque([])
    q.append(u-1)
    far_p = u-1

    while(len(q) != 0):
        p = q.popleft()

        if (d[p] - e[p]) >= 1:
            rs = path[p]

            is_end = len(rs)
            for r in rs:
                if e[r] == -1:
                    e[r] = e[p] + 1
                    q.append(r)
                else:
                    is_end -= 1

            if is_end == 0:
                if d[p] >= d[far_p]:
                    far_p = p

    return e, far_p


N, u, v = map(int, input().split())
path = [[] * N for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    path[a].append(b)
    path[b].append(a)

d = bfs(N, v, path)
e, far_p = bfs2(N, u, path, d)

print(d[far_p]-1)
