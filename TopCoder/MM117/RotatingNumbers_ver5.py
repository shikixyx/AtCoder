import sys
import time
import copy
import math
import itertools
import math
import random
from heapq import heappop, heappush, heappushpop

# ver.5
# N = 4でのビームサーチ
# ありったけ回してみる

# 20ステップほどで収束

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


def duplicate(G):
    newG = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newG[i][j] = G[i][j]

    return newG


def rotate(G, r, c, s, d):
    newG = duplicate(G)

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
    elif d == "RR" or d == "LL":
        rows = []
        for i in range(s):
            rs = []
            for j in range(s):
                rs.append(G[r + i][c + j])
            rows.append(rs)

        for i in range(s):
            newG[r + i][c : c + s] = rows[-(i + 1)][::-1]

    return newG


def getManhattanDist(G, r=0, c=0, s=N):
    dist = 0

    for i in range(s):
        for j in range(s):
            a = G[r + i][c + j] - 1
            d = abs((a // N) - (r + i)) + abs((a % N) - (c + j))
            dist += d
    return dist


BEAM_SIZE = 10
now_score = getManhattanDist(G) * P

ANS = []
ANS_SCORE = now_score

nowG = duplicate(G)
Q = [(now_score, 0, nowG, [])]

debug_cnt = 0
for cnt in range(10 ** 10):
    debug_cnt += 1
    nxtQ = []
    # print([(s, len(a)) for s, _, _, a in Q])

    time_cur = int(time.time()) * 1000
    if 9500 <= time_cur - time_start:
        break

    for _, p, g, ops in Q:
        # make next grid
        for sub_size in range(2, N + 1):
            for r, c in itertools.product(range(N - sub_size + 1), repeat=2):
                for d in ["R", "L", "LL"]:
                    nxtG = rotate(g, r, c, sub_size, d)
                    nxt_p = p + math.floor((sub_size - 1) ** 1.5) * len(d)
                    nxt_score = getManhattanDist(nxtG) * P + nxt_p
                    nxt_ops = copy.copy(ops)

                    if d != "LL":
                        nxt_ops.append((r, c, sub_size, d))
                    else:
                        nxt_ops.append((r, c, sub_size, "L"))
                        nxt_ops.append((r, c, sub_size, "L"))

                    if len(nxtQ) < BEAM_SIZE:
                        heappush(nxtQ, (-nxt_score, nxt_p, nxtG, nxt_ops))
                    else:
                        heappushpop(nxtQ, (-nxt_score, nxt_p, nxtG, nxt_ops))

    Q = nxtQ
    s, _, _, ops = max(Q)
    s = -s
    if s < ANS_SCORE:
        ANS_SCORE = s
        ANS = ops


s, _, _, ops = max(Q)
s = -s
if s < ANS_SCORE:
    ANS_SCORE = s
    ANS = ops

L = len(ANS)
print(L)
for i in range(L):
    print(" ".join(map(str, ANS[i])))

sys.stdout.flush()

with open(DEBUG_FILE, mode="a") as f:
    f.write(str(debug_cnt))
    f.write("\n")


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
