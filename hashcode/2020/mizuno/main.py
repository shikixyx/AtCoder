import sys
import numpy as np
import datetime
import math
import copy
import heapq
import random
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


# スコアを取得
def getBooksScore(books):
    return sum([BOOKS_SCORES[b] for b in books])


# K beam serach
K = 100
k_list = [Libs(D) for _ in range(K)]
max_libs = Libs(D)

for i in range(L):

    # if i == 12:
    #K = 20

    new_k_list = []
    for libs in k_list:
        scores = [eval(libs, l) for l in LIBRARIES]

        for _ in range(K):
            best_l_id = np.argmax(scores)
            if best_l_id in libs.libids:
                break

            scores[best_l_id] = float('-inf')
            new_k_list.append(
                (getBestBooks(libs, LIBRARIES[best_l_id]), best_l_id, libs))

    if len(new_k_list) == 0:
        break

    new_k_list = sorted(new_k_list, key=lambda x: -getBooksScore(x[0]))
    # random.shuffle(new_k_list)
    new_k_list = new_k_list[:K]

    k_list = []
    for books, l_id, libs in new_k_list:
        if len(books) == 0:
            continue

        nlibs = copy.deepcopy(libs)
        nlibs.addLibrary(LIBRARIES[l_id], books)

        k_list.append(nlibs)

        max_libs = max(max_libs, nlibs,
                       key=lambda x: x.calcScore(B, BOOKS_SCORES))

    if len(k_list) == 0:
        break
    else:
        m = max(k_list, key=lambda x: x.calcScore(B, BOOKS_SCORES))
        max_libs = max(m, max_libs, key=lambda x: x.calcScore(B, BOOKS_SCORES))

    print("i: {0:>3} , SCORE:{1:>9}".format(
        i, max_libs.calcScore(B, BOOKS_SCORES)))


print("SCORE:", max_libs.calcScore(B, BOOKS_SCORES))

# 出力ファイル作成
OUTPUT = max_libs.out

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
