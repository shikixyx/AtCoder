import sys
import numpy as np
import datetime
import math
from tqdm import tqdm
from collections import defaultdict
from collections import deque

# my class
from library import Library
from library import Score

# 入力
B, L, D = map(int, input().split())
SCORES = list(map(int, input().split()))

LIBRARIES = []
for i in range(L):
    n, t, m = map(int, input().split())
    books = list(map(int, input().split()))
    l = Library(i, n, t, m, books, L)
    LIBRARIES.append(l)


# 各ライブラリの期待値

# 本の出現頻度
FREQ = defaultdict(int)
for l in LIBRARIES:
    books = l.books
    for b in books:
        FREQ[b] += 1


# 期待値計算用 + 本の評価値順
for l in LIBRARIES:
    l.calcExpectation(FREQ, SCORES)


# 出力

# ライブラリをソート、期待値の高いものから

lib_sorted = sorted(LIBRARIES, key=lambda x: x.ex)
lib_sorted = deque(lib_sorted)

# OUTPUT用の変数
OUTPUT = {}


# 残り日数はD日
BAR = tqdm(total=D)
while (D > 0):

    # 大きいのものから取り出す
    if len(lib_sorted) == 0:
        break
    l = lib_sorted.popleft()

    #l, LIBRARY_SORTED = maxLibrary(LIBRARY_SORTED, USED_BOOKS, D)

    # 出せるだけ本を出す
    D -= l.signup
    BAR.update(l.signup)
    if D <= 0:
        break

    num = l.perday * D
    books_key = [x[0] for x in l.books_p_sorted]
    books_key = books_key[:num]

    #books_s_key = np.array(books_s_key)
    OUTPUT[l.id] = books_key

    #USED_BOOKS = np.concatenate([USED_BOOKS, books_s_key])


# 出力ファイル作成
argv = sys.argv
now = datetime.datetime.now()
d = now.strftime("%m%d%H%I")
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
