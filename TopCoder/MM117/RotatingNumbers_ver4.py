import sys
import time
import copy
import math
import itertools
import math
import random

# ver.4
# 焼きなまし

# 11ポイント
# 前回よりも悪い

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


ANS = []
ANS_SCORE = []

SIMULATE_TIME = 3200
C = SIMULATE_TIME * 100000
op_penalty = 0

for _ in range(10):
    time_now = int(time.time()) * 1000
    if 9500 <= time_now - time_start:
        break

    time_end = time_now + SIMULATE_TIME
    time_cur = int(time.time()) * 1000

    nowG = duplicate(G)
    now_score = getManhattanDist(nowG) * P
    operations = []

    limit = 30
    sub_size = N

    while time_cur < time_end:
        """
        if limit == 0:
            sub_size -= 1
            if sub_size == 1:
                break
            limit = 30 * (N - sub_size) * (N - sub_size)
        limit -= 1
        """

        sub_size = random.randint(2, N)
        r = random.randint(0, N - sub_size)
        c = random.randint(0, N - sub_size)
        d = random.randint(0, 2)

        if d == 0:
            d = "R"
            n = 1
        elif d == 1:
            d = "L"
            n = 1
        elif d == 2:
            d = "LL"
            n = 2

        nextG = rotate(nowG, r, c, sub_size, d)
        next_score = getManhattanDist(nextG)
        next_score += math.floor((sub_size - 1) ** 1.5) * n
        next_score += op_penalty

        delta = next_score - now_score
        forceLine = (time_end - time_cur) / C

        if delta < 0 or random.random() < forceLine:
            if d == "LL":
                operations.append([r, c, sub_size, "L"])
                operations.append([r, c, sub_size, "L"])
            else:
                operations.append([r, c, sub_size, d])

            nowG = nextG
            now_score = next_score
            op_penalty += math.floor((sub_size - 1) ** 1.5) * n

        time_cur = int(time.time()) * 1000

    ANS.append(operations)
    ANS_SCORE.append(now_score)

min_idx = ANS_SCORE.index(min(ANS_SCORE))
ANS = ANS[min_idx]


L = len(ANS)
print(L)
for i in range(L):
    print(" ".join(map(str, ANS[i])))

# print(ANS_SCORE)
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
