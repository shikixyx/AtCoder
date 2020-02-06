import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
XY = np.array(read().split(), np.int64)

X = XY[::2]
Y = XY[1::2]

dx = X[None, :] - X[:, None]
dy = Y[None, :] - Y[:, None]

dist_mat = (dx * dx + dy * dy) ** .5
ans = dist_mat.sum() / N

print(ans)
