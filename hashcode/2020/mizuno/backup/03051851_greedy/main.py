import sys
import numpy as np
import datetime
import math
import copy
import heapq
from tqdm import tqdm
from collections import defaultdict
from collections import deque

# my class
from library import Library
from library import Score
from library import Libs

# 入力
B, L, D = map(int, input().split())
BOOKS_SCORES = list(map(int, input().split()))

LIBRARIES = []
for i in range(L):
    n, t, m = map(int, input().split())
    books = list(map(int, input().split()))
    l = Library(i, n, t, m, set(books), L)
    LIBRARIES.append(l)


# 各ライブラリの期待値

# 本の出現頻度
BOOKS_FREQ = defaultdict(int)
for l in LIBRARIES:
    books = l.books
    for b in books:
        BOOKS_FREQ[b] += 1


# 最良の本
def getBestBooks(libs, l):
    d = libs.day
    d -= l.signup
    if d <= 0:
        return []

    books = sorted(l.books - libs.books,
                   key=lambda x: BOOKS_SCORES[x], reverse=True)
    return list(books)[:d*l.perday]


# 評価関数
def eval(libs, l):
    if l.id in libs.libids:
        return float('-inf')

    books = getBestBooks(libs, l)

    s = sum([BOOKS_SCORES[b] for b in books])
    s /= l.signup

    return s


# Choose Greedy
libs = Libs(D)


for i in tqdm(range(L)):
    scores = [eval(libs, l) for l in LIBRARIES]
    best_l_id = np.argmax(scores)

    if best_l_id in libs.libids:
        break

    if libs.day <= 0:
        break

    best_l = LIBRARIES[best_l_id]
    books = getBestBooks(libs, best_l)

    if len(books) == 0:
        break

    libs.addLibrary(best_l, getBestBooks(libs, best_l))


print("SCORE:", libs.calcScore(B, BOOKS_SCORES))

# 出力ファイル作成
OUTPUT = libs.out

argv = sys.argv
now = datetime.datetime.now()
d = now.strftime("%m%d%H%M")
path = "output_" + argv[1] + "_"+d+".txt"
with open(path, mode="w") as f:

    num = len(OUTPUT)
    f.write(str(num))

    libs = []
    books = []
    for i, x in OUTPUT.items():
        libs.append([str(i), str(len(x))])
        books.append([str(a) for a in x])

    for i in range(num):
        f.write("\n")
        f.write(" ".join(libs[i]))
        f.write("\n")
        f.write(" ".join(books[i]))
