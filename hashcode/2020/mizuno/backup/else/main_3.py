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

# 使った本
USED_BOOKS = np.array([])


# スコアの計算
def calcScore(books):
    score = 0
    for b in books:
        score += SCORE[b]
    return score


# スコアの最も大きいライブラリと、それを除いた物を返す
def maxLibrary(lib, used, rest):
    mx = -1
    key = -1
    for l in lib:
        rest_day = rest

        # 出せるだけ本を出す
        rest_day -= l[1]["signup"]
        if rest_day <= 0:
            s = 0
        else:
            num = l[1]["perday"] * rest_day
            books_s_key = l[1]["books_s_key"]
            books_s_key = np.array(books_s_key)
            books_s_key = np.setdiff1d(books_s_key, used)

            s = calcScore(books_s_key[:num])

        if mx < s:
            key = l[0]
            mx = s

    l = lib[key]
    lib.pop(key)

    return l, lib


# 残り日数はD日
BAR = tqdm(total=D)
while (D > 0):

    # 大きいのものから取り出す
    if len(LIBRARY_SORTED) == 0:
        break

    l, LIBRARY_SORTED = maxLibrary(LIBRARY_SORTED, USED_BOOKS, D)

    # 出せるだけ本を出す
    D -= l[1]["signup"]
    BAR.update(l[1]["signup"])
    if D <= 0:
        break

    num = l[1]["perday"] * D
    books_s_key = l[1]["books_s_key"][:num]

    books_s_key = np.array(books_s_key)
    OUTPUT[l[0]] = books_s_key

    USED_BOOKS = np.concatenate([USED_BOOKS, books_s_key])

# print(OUTPUT)


# 出力ファイル作成
argv = sys.argv
path = "output_" + argv[1] + "_3.txt"
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
