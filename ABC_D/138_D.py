import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC (1WA)
# 20min

N, Q = map(int, readline().split())

PATH = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, readline().split())
    PATH[a].append(b)
    PATH[b].append(a)

POINT = [0] * (N + 1)

for _ in range(Q):
    p, x = map(int, readline().split())
    POINT[p] += x


ans = [0] * (N+1)

STATE = [False] * (N+1)


def dfs(s, plus):
    p = POINT[s]
    pt = p + plus
    ans[s] += pt

    STATE[s] = True

    for v in PATH[s]:
        if STATE[v]:
            continue
        dfs(v, pt)


dfs(1, 0)
print(" ".join(map(str, ans[1:])))
