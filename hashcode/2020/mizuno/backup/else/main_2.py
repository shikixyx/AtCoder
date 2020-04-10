import sys
import numpy as np
import math
from tqdm import tqdm
from collections import defaultdict

# 入力
B, L, D = map(int, input().split())
SCORE = list(map(int, input().split()))

LIBRARY = {}
for i in range(L):
    n, t, m = map(int, input().split())
    books = list(map(int, input().split()))
    LIBRARY[i] = {"num": n, "signup": t, "perday": m, "books": books}


# 各ライブラリの期待値

# 本の出現頻度
FREQ = defaultdict(int)
for i in range(L):
    l = LIBRARY[i]
    books = l["books"]
    for b in books:
        FREQ[b] += 1

# print(FREQ)


# 期待値計算用 + 本の評価値順
def calc_ex(l):
    books = l["books"]
    books_score = {}
    s = 0
    for b in books:
        # 各本の評価値
        s += SCORE[b] * (math.log(L / FREQ[b]) + 1)

        # 並び替え用
        books_score[b] = s

    # 期待値算出
    s = (s / len(books)) * l["perday"]
    s /= l["signup"]

    # 評価値で並び替え
    books_score_sorted = sorted(
        books_score.items(), key=lambda x: x[1], reverse=True)

    return s, books_score_sorted


# 期待値をいれる
for i in range(L):
    s, books_score_sorted = calc_ex(LIBRARY[i])
    LIBRARY[i]["ex"] = s
    LIBRARY[i]["books_s"] = books_score_sorted
    LIBRARY[i]["books_s_key"] = [x[0] for x in books_score_sorted]

# print(LIBRARY)


# 出力

# ライブラリをソート、期待値の高いものから

LIBRARY_SORTED = sorted(LIBRARY.items(), key=lambda x: x[1]["ex"])

print()
print("### LIBRARY_SORTED ###")
print()
# print(LIBRARY_SORTED)

# OUTPUT用の変数
OUTPUT = {}

# 使用済みの本
USED_BOOKS = np.array([])

# 残り日数はD日
BAR = tqdm(total=D)
while (D > 0):

    # 大きいのものから取り出す
    if len(LIBRARY_SORTED) == 0:
        break

    l = LIBRARY_SORTED.pop()

    # 出せるだけ本を出す
    D -= l[1]["signup"]
    BAR.update(l[1]["signup"])
    if D <= 0:
        break

    num = l[1]["perday"] * D
    books_s_key = l[1]["books_s_key"][:num]

    # 使ってる本は取り除く
    books_s_key = np.array(books_s_key)

    remain_books = np.setdiff1d(books_s_key, USED_BOOKS)

    if len(remain_books) == 0:
        continue

    OUTPUT[l[0]] = remain_books

    USED_BOOKS = np.concatenate([USED_BOOKS, remain_books])

# print(OUTPUT)


# 出力ファイル作成
argv = sys.argv
path = "output_" + argv[1] + "_2.txt"
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
