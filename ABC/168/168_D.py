import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
PATH = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    PATH[A].append(B)
    PATH[B].append(A)


USED = [False] * (N + 1)
MARK = [None] * (N + 1)

Q = [1]
Q = deque(Q)

while Q:
    node = Q.popleft()

    for v in PATH[node]:
        if USED[v]:
            continue

        MARK[v] = node
        USED[v] = True
        Q.append(v)

print("Yes")
print("\n".join(map(str, MARK[2:])))
