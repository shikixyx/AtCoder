import sys
import time
import copy
import math
import itertools

# ver.2
# 2周ずつ全部見てみる

# RESULT
# 1回だけよりも全然スコア悪い
# 回しすぎ

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

time_start = int(time.time() * 1000)

N = int(input())
P = int(input())
G = [[0] * N for _ in range(N)]

for i in range(N * N):
    G[(int)(i / N)][(int)(i % N)] = int(input())


def rotate(G, r, c, s, d, makeNewGrid=False):
    newG = copy.copy(G) if makeNewGrid else G

    columns = []
    for i in range(s):
        cs = []
        for j in range(s):
            cs.append(G[r + j][c + i])
        columns.append(cs)

    if d == "R":
        for i in range(s):
            newG[r + i][c : c + s] = columns[i][::-1]
    elif d == "L":
        for i in range(s):
            newG[r + i][c : c + s] = columns[-(i + 1)]

    return newG


def getManhattanDist(G, r=0, c=0, s=N):
    dist = 0

    for i in range(s):
        for j in range(s):
            a = G[r + i][c + j] - 1
            d = abs((a // N) - (r + i)) + abs((a % N) - (c + j))
            dist += d
    return dist


ANS = []


sub_size = N
rotate_rc = [0]
penalty = 0
for cnt in range(N * 10):
    for rr, rc in itertools.product(rotate_rc, repeat=2):
        now_score = getManhattanDist(G, rr, rc, sub_size) * P + penalty
        NOW = (now_score, "now", G)

        # R
        newR = rotate(G, rr, rc, sub_size, "R", True)
        R_score = (
            getManhattanDist(newR, rr, rc, sub_size) * P
            + math.floor((sub_size - 1) ** 1.5)
            + penalty
        )
        R = (R_score, "R", newR)

        # L
        newL = rotate(G, rr, rc, sub_size, "L", True)
        L_score = (
            getManhattanDist(newL, rr, rc, sub_size) * P
            + math.floor((sub_size - 1) ** 1.5)
            + penalty
        )
        L = (L_score, "L", newL)

        # LL
        newLL = rotate(newL, rr, rc, sub_size, "L", True)
        LL_score = (
            getManhattanDist(newLL, rr, rc, sub_size) * P
            + 2 * math.floor((sub_size - 1) ** 1.5)
            + penalty
        )
        LL = (LL_score, "LL", newLL)

        nxt, op, G = min(NOW, R, L, LL)

        if op == "now":
            continue
        elif op == "LL":
            ANS.append([rr, rc, sub_size, "L"])
            ANS.append([rr, rc, sub_size, "L"])
            now += 2 * math.floor((sub_size - 1) ** 1.5)
        else:
            ANS.append([rr, rc, sub_size, op])
            now += math.floor((sub_size - 1) ** 1.5)

    sub_size -= 1
    if sub_size == 1:
        break

    rotate_rc = [
        x if (x + sub_size) <= N else N - sub_size for x in range(0, N - sub_size + 1)
    ]


L = len(ANS)
print(L)
for i in range(L):
    print(" ".join(map(str, ANS[i])))

sys.stdout.flush()
