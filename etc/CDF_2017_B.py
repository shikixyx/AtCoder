import sys
from collections import defaultdict
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
AB = [[int(x) for x in input().split()] for _ in range(M)]
PATH = [[] for _ in range(N+1)]

for a, b in AB:
    PATH[a].append(b)
    PATH[b].append(a)

color = [None] * (N+1)
color[1] = 0
q = deque([1])

while q:
    x = q.popleft()
    for y in PATH[x]:
        if color[y] is None:
            color[y] = 1 - color[x]
            q.append(y)

bl = all([color[a] != color[b] for a, b in AB])

ans = 0
if bl:
    x = sum(color[1:])
    y = N - x
    ans = x * y - M
else:
    ans = (N * (N-1) // 2) - M

print(ans)
