import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 15min
# 2020/03/10

N = int(readline())

E = [[] for _ in range(N + 1)]

for _ in range(N-1):
    u, v, w = map(int, readline().split())
    E[u].append((v, w))
    E[v].append((u, w))

COLOR = [None] * (N + 1)


def setColor(v, c):
    COLOR[v] = c
    for w, l in E[v]:
        if COLOR[w] == None:
            nc = c
            if l % 2 != 0:
                nc = int(not nc)
            setColor(w, nc)


setColor(1, 0)

print("\n".join(map(str, COLOR[1:])))
