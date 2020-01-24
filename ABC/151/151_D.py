import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import random


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
MEIJI = [[0] * W for i in range(H)]

for i in range(H):
    a = input()
    for j in range(len(a)):
        if a[j] == "#":
            MEIJI[i][j] = 1


def findStart():
    for x in range(H):
        for y in range(W):
            if MEIJI[x][y] == 0:
                return x, y

    return False


def bfs(H, W, sx, sy):
    if MEIJI[sx][sy] == 1:
        return 0, 0, 0, -1
    d = [[-1] * W for i in range(H)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque([])
    q.append((sx, sy))
    d[sx][sy] = 0

    mx = -1
    gx, gy = -1, -1
    while(len(q) != 0):
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (0 <= nx and nx <= (H-1) and 0 <= ny and ny <= (W-1) and MEIJI[nx][ny] == 0 and d[nx][ny] == -1):
                q.append((nx, ny))
                l = d[x][y] + 1
                d[nx][ny] = l

                if l > mx:
                    gx, gy = nx, ny
                    mx = l
    return d, gx, gy, mx


mx = 0
for x in range(H):
    for y in range(W):
        _, _, _, l = bfs(H, W, x, y)
        if l > mx:
            mx = l

print(mx)
exit()

sx, sy = findStart()
_, x, y, _ = bfs(H, W, sx, sy)
_, _, _, l = bfs(H, W, x, y)

if l < 0:
    l = 0

print(l)
