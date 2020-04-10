import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

PATH = [[] for _ in range(N+1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    PATH[x].append(y)
    PATH[y].append(x)

CNT = [{} for _ in range(N + 1)]


def dfs(u, parent, s, CNT):
    s.append(u)
    for v in PATH[u]:
        if v == parent:
            continue
        t = dfs(v, u, [], CNT)
        CNT[u][v] = t
        s += t

    return s


dfs(1, -1, [], CNT)


print(CNT)
