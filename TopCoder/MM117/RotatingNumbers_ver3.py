import sys
import time
import copy
import math
import itertools

# ver.3
# スコアが良くなる回転は行う
# N - 2　までを2回繰り返す

# 12P
# 良いけど、ロスが大きそう

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

time_start = int(time.time() * 1000)

DEBUG_FILE = "./debug.txt"
DEBUG = False

N = int(input())
P = int(input())
G = [[0] * N for _ in range(N)]

for i in range(N * N):
    G[(int)(i / N)][(int)(i % N)] = int(input())


def rotate(G, r, c, s, d):
    newG = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newG[i][j] = G[i][j]

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
now_score = getManhattanDist(G) * P
for cnt in range(N * 10):
    time_now = int(time.time() * 1000)
    if 9500 <= time_now - time_start:
        break

    for rr, rc in itertools.product(rotate_rc, repeat=2):
        # NOW
        NOW = (now_score, "now", G)
        # R
        newR = rotate(G, rr, rc, sub_size, "R")
        R_score = (
            getManhattanDist(newR) * P + math.floor((sub_size - 1) ** 1.5) + penalty
        )
        R = (R_score, "R", newR)

        # L
        newL = rotate(G, rr, rc, sub_size, "L")
        L_score = (
            getManhattanDist(newL) * P + math.floor((sub_size - 1) ** 1.5) + penalty
        )
        L = (L_score, "L", newL)

        # LL
        newLL = rotate(newL, rr, rc, sub_size, "L")
        LL_score = (
            getManhattanDist(newLL) * P
            + 2 * math.floor((sub_size - 1) ** 1.5)
            + penalty
        )
        LL = (LL_score, "LL", newLL)

        if cnt and DEBUG:
            with open(DEBUG_FILE, mode="a") as f:
                f.write(str(cnt) + "\n")
                f.write(" ".join(map(str, [now_score, R_score, L_score, LL_score])))
                f.write("\n")
                f.write("nxt = {}".format(min(NOW, R, L, LL)[0]))
                f.write("\n")

        now_score, op, G = min(NOW, R, L, LL)

        if op == "now":
            continue
        elif op == "LL":
            ANS.append([rr, rc, sub_size, "L"])
            ANS.append([rr, rc, sub_size, "L"])
            penalty += 2 * math.floor((sub_size - 1) ** 1.5)
        else:
            ANS.append([rr, rc, sub_size, op])
            penalty += math.floor((sub_size - 1) ** 1.5)

    # sub_size -= 1
    sub_size = -(-sub_size // 2)
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


if not DEBUG:
    exit()

with open(DEBUG_FILE, mode="a") as f:
    f.write(" ===== ANS =====")
    f.write(str(L))
    f.write("\n")
    for i in range(L):
        f.write(" ".join(map(str, ANS[i])))
        f.write("\n")

    d = getManhattanDist(G)
    f.write("DIST = {}".format(d * P))
    f.write("\n")

    for i in range(N):
        f.write(" ".join(map(str, G[i])))
        f.write("\n")

sys.stdout.flush()
