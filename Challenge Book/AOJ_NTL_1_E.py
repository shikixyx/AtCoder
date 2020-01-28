import sys
sys.setrecursionlimit(10 ** 7)

# 拡張Euclidの互除法
# 拡張ユークリッドの互除法
# https://qiita.com/drken/items/b97ff231e43bce50199a

# whileを使う方法


a, b = map(int, input().split())


def extgcd(a, b):
    if b == 0:
        return a, 1, 0

    p, q = a // b, a % b
    d, x, y = extgcd(b, q)
    x, y = y, x - p * y
    return d, x, y


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


d, x, y = extgcd(a, b)


print(x, y)
