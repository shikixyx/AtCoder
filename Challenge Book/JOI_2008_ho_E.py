import sys
sys.setrecursionlimit(10 ** 7)

# 座標圧縮
# 座圧
# できていない

W, H = map(int, input().split())
N = int(input())
TAPES = [[int(x) for x in input().split()] for _ in range(N)]
X1, Y1, X2, Y2 = zip(*(TAPES))

print(X1, Y1, X2, Y2)

X = sorted(set(X1 + X2 + (0, W)))
Y = sorted(set(Y1 + Y2 + (0, H)))

print(X)

x_to_i = {x: i for i, x in enumerate(X)}
y_to_i = {x: i for i, x in enumerate(Y)}

print(x_to_i)

X1 = [x_to_i[x] for x in X1]
X2 = [x_to_i[x] for x in X2]
Y1 = [y_to_i[x] for x in Y1]
Y2 = [y_to_i[x] for x in Y2]
W = x_to_i[W]
H = y_to_i[H]

print(X1)

del x_to_i, y_to_i, X, Y
