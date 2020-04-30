import sys
import time
import copy
import math
import itertools
import math
import random
from heapq import heappop, heappush, heappushpop

# ver.7
# 大きい場合は分割してみる
# N <= 7 までは普通にやる
# 8 <= N なら 4 * 4 に分割して揃えてみる

# 微妙
# 分割がそれほど良くない

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


def debugPrint(s):
    if DEBUG:
        with open(DEBUG_FILE, mode="a") as f:
            if type(s) is str or int:
                f.write(str(s))
            elif type(s) is list:
                f.write(" ".join(map(str, s)))

            f.write("\n")

    return


BEAM_SIZE = 10
now_score = getManhattanDist(G) * P

ANS = []
ANS_SCORE = now_score

nowG = duplicate(G)
Q = [(now_score, 0, nowG, [])]

sub_sizes = [N, N // 2, ((N // 2) + N) // 2] if N >= 8 else list(range(2, N + 1))
sub_gird_size = N
prefixes = [0]

debugPrint(sub_sizes)

for cnt in range(10 ** 10):
    nxtQ = []
    # print([(s, len(a)) for s, _, _, a in Q])

    time_cur = int(time.time()) * 1000
    if 9500 <= time_cur - time_start:
        debugPrint("cnt={}".format(cnt))
        break

    for _, p, g, ops in Q:

        # time limit
        time_cur = int(time.time()) * 1000
        if 9500 <= time_cur - time_start:
            debugPrint("cnt={}".format(cnt))
            break

        # make next grid
        for sub_size in sub_sizes:
            debugPrint("subsize = {}".format(sub_size))

            for pre in prefixes:
                for r, c in itertools.product(
                    range(pre, sub_gird_size - sub_size + 1, -(-sub_gird_size // 4)),
                    repeat=2,
                ):

                    debugPrint([r, c, sub_size])

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

    if cnt % 20 == 19:
        sub_gird_size //= 2
        if sub_gird_size <= 2:
            break
        elif sub_gird_size == 3:
            sub_sizes = [3, 2]
        else:
            sub_sizes = [
                sub_gird_size,
                sub_gird_size // 2,
                ((sub_gird_size // 2) + sub_gird_size) // 2,
            ]
        prefixes = [
            x * sub_gird_size if x * sub_gird_size <= N else N - (x * sub_gird_size)
            for x in range(N // sub_gird_size + 1)
        ]

        debugPrint("change size")
        debugPrint(sub_gird_size)
        debugPrint(sub_sizes)
        debugPrint(prefixes)

    Q = nxtQ
    s, _, _, ops = max(Q)
    s = -s
    if s < ANS_SCORE:
        ANS_SCORE = s
        ANS = ops


s, _, g, ops = max(Q)
s = -s
if s < ANS_SCORE:
    ANS_SCORE = s
    ANS = ops

L = len(ANS)
print(L)
for i in range(L):
    print(" ".join(map(str, ANS[i])))

sys.stdout.flush()


if not DEBUG:
    exit()

with open(DEBUG_FILE, mode="a") as f:
    f.write(" ===== ANS =====\n")
    f.write(str(L))
    f.write("\n")
    for i in range(L):
        f.write(" ".join(map(str, ANS[i])))
        f.write("\n")

    d = getManhattanDist(g)
    f.write("DIST = {}".format(d * P))
    f.write("\n")

    for i in range(N):
        f.write(" ".join(map(str, g[i])))
        f.write("\n")

sys.stdout.flush()
