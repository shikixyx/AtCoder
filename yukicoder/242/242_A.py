import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))


def pay(a, X, Y, Z):
    # 1万円札はあるだけ
    if a >= 10000:
        z = a // 10000

        if Z >= z:
            Z -= z
            a -= z * 10000
        else:
            a -= Z * 10000
            Z = 0

    # 1万円札未満
    # 5千円以上かつ、5千円札あり
    if a >= 5000:
        y = a // 5000

        if Y >= y:
            a -= 5000 * y
            Y -= y
        else:
            a -= 5000 * Y
            Y = 0

    # 千円札で端数まで払う
    if a > 0:
        x = -(-a // 1000)

        if X >= x:
            X -= x
            a -= x * 1000

    # 払い切れてない時
    # 5千円札あり
    if a > 0 and Y > 0:
        y = -(-a // 5000)

        if Y >= y:
            Y -= y
            a -= y * 5000

    # 一万円札あり
    if a > 0 and Z > 0:
        z = -(-a // 10000)
        if Z >= z:
            Z -= z
            a -= z * 10000

    ok = True
    if a > 0:
        ok = False
    elif a == 0:
        if 0 < X:
            X -= 1
        elif 0 < Y:
            Y -= 1
        elif 0 < Z:
            Z -= 1
        else:
            ok = False

    return ok, X, Y, Z


for a in A:
    ok, X, Y, Z = pay(a, X, Y, Z)
    if ok:
        continue
    else:
        print('No')
        exit()

print('Yes')
