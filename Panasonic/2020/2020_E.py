import sys
import itertools
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE
# 文字列をそのまま扱っていた

A = list(input())
B = list(input())
C = list(input())

N = len(A)


def compare(x, y):
    # print("COMPARE:", x, y)
    if not (x and y):
        return False
    for a, b in zip(x, y):
        if a == b or a == '?' or b == '?':
            continue
        else:
            # print("False")
            return False
    # print("True")
    return True


def getNewStr(X, Y):
    ans = []
    for _ in range(2):
        X, Y = Y, X
        for i in range(N, -1, -1):
            if compare(X[-i:], Y[:i]):
                ans.append(X + Y[i:])
                break

    return ans


def getMaxStr(X, Y):
    # print("getMAX", X, Y)
    n = len(X)
    m = len(Y)
    ans = 0
    for i in range(n, -1, -1):
        if m < i:
            if compare(X[i - m:i], Y):
                ans = max(ans, m)
                break
        else:
            if compare(X[:i], Y[-i:]):
                ans = max(ans, i)
                break

    for i in range(n, -1, -1):
        if m < i:
            if compare(X[-i: -i + m], Y):
                ans = max(ans, m)
                break
        else:
            if compare(X[-i:], Y[i:]):
                ans = max(ans, i)
                break

    return ans


# まずAとBを比較
# 先頭から

ans = N * 3
# for _ in range(3):
# A, B, C = C, A, B

for A, B, C in itertools.permutations([A, B, C]):

    rs = getNewStr(A, B)

    # print("rs", rs)
    if not rs:
        continue

    for r in rs:
        m = getMaxStr(r, C)
        # print("r", r, "m", m)
        if m == 0:
            ans = min(ans, len(r)+len(C))
        elif m == len(C):
            ans = min(ans, len(r))
        else:
            ans = min(ans, len(r)+len(C)-m)

print(ans)
