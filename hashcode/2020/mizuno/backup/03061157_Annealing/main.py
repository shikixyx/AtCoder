import sys
import numpy as np
import datetime
import math
import copy
import os
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


# 出力ファイルから図書館を読み込み
argv = sys.argv
num = argv[1]

# 出力ファイルを読む
for FILE in os.listdir('./mizuno/'):
    if FILE.startswith(num) and FILE.endswith('.out'):
        with open('./mizuno/'+FILE, 'r') as ifp:
            lines = ifp.readlines()


libs = []
num_lib = int(lines[0])

for i in range(1, num_lib+1):
    l, _ = map(int, lines[2 * i - 1].split())
    books = set(map(int, lines[2 * i].split()))
    libs.append([LIBRARIES[l], books])


# 最良の本
def getBestBooks(l, assigned_books, d):
    d -= l.signup
    if d <= 0:
        return []

    books = sorted(l.books - assigned_books, key=lambda x: -BOOKS_SCORES[x])
    return list(books)[:d*l.perday]


# スコアを計算
def getScore(libs):
    books = set()
    for _, bs in libs:
        books |= bs

    #flag = np.zeros(B, dtype=np.bool)
    #flag[list(books)] = 1
    # return (BOOKS_SCORES * flag).sum()

    return sum([BOOKS_SCORES[b] for b in books])


# print(libs)
iniscore = getScore(libs)
print(iniscore)


# 焼きなまし

T = 100000000
cool = 0.999
len_libs = len(libs)

while (T > 1.):
    state = getScore(libs)

    # choose swap index
    i = np.random.randint(0, len_libs - 2)
    j = i + 1

    # swap
    pre_i_books = libs[i][1]
    pre_j_books = libs[j][1]
    libs[i], libs[j] = libs[j], libs[i]

    # calc new score
    d = D
    asn_books = set()

    # 0 to i-1
    for k in range(i):
        l, bs = libs[k]
        d -= l.signup
        asn_books |= bs

    # i
    i_books = getBestBooks(libs[i][0], asn_books, d)
    i_books = set(i_books)
    libs[i][1] = i_books
    asn_books |= i_books
    d -= l.signup

    # j
    j_books = getBestBooks(libs[j][0], asn_books, d)
    j_books = set(j_books)
    libs[j][1] = j_books

    # newstate
    newstate = getScore(libs)

    # delta and Annealing
    delta = newstate - state
    p = pow(math.e, -abs(delta) / T)

    if delta == 0:
        T *= cool
        continue

    if delta > 0 or np.random.rand() < p:
        score = newstate
    else:
        score = state
        libs[i], libs[j] = libs[j], libs[i]
        libs[i][1] = pre_i_books
        libs[j][1] = pre_j_books

    print("T:{0:>10,.1f} , p:{1:>5.3f} , delta:{3:>6} , SCORE: {2:>7}".format(
        T, p, score, delta))

    T *= cool


# make output file
OUTPUT = {}
for l, books in libs:
    OUTPUT[l.id] = list(books)

print("SCORE:", getScore(libs))
print("INI  :", iniscore)

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
