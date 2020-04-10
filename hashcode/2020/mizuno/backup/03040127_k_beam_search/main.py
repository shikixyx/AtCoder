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
    l.sortBooksByFreq(FREQ, SCORES)
    #l.sortBooksByScore(FREQ, SCORES)
    l.calcExpectation(FREQ, SCORES)


# Kビームサーチ
K = 1
USE_LIBRARY = L

# 初期化
max_s = None
queue = []

libs = sorted(LIBRARIES, key=lambda l: l.ex, reverse=True)
#libs = libs[:USE_LIBRARY]
for l in libs:
    s = Score(SCORES, D, L, B)
    res = s.addLibrary(l)

    # 図書館を追加できた場合のみ
    if res:
        queue.append(s)

print("Start Beam Search")
#BAR = tqdm(total=L)

# 図書館を順次選んでいく
# 1ループで1図書館増える
cnt = 0
while (len(queue) > 0):
    # BAR.update(1)
    cnt += 1
    if cnt < 5:
        K = 50
    else:
        K = 10

    print("=====", cnt, "=====")

    k_list = []

    # queue の中で最大のスコアをk個以下で抽出
    i = 0
    for s in queue:
        i += 1
        r = s.getScore()
        ev = s.getEstimateValue()
        # K個しか残さない
        if len(k_list) >= K:
            heapq.heappushpop(k_list, (ev, r, i, s))
        else:
            k_list.append((ev, r, i, s))

        # print(k_list)

    # 最大のものは取っておく
    # 図書館が増えなくても大きいものがある可能性
    m = max(k_list, key=lambda x: (x[1], x[2]))
    if max_s == None:
        max_s = m
    else:
        max_s = max(max_s, m, key=lambda x: (x[1], x[2]))

    #print("max_s", max_s)
    #visual_score = [(x[1], x[0], x[-1].getLibrariesIDs()) for x in k_list]
    visual_score = [(x[1], x[0]) for x in k_list]
    print("- k_list")
    print(visual_score)
    print("- max score")
    print(max_s[1])

    # 次の候補を作る
    queue = []
    for ev, r, _, s in k_list:
        # 残りの図書館を列挙
        list_unuse_lib = s.getUnuseLibrary()
        libs = np.array(LIBRARIES)
        libs = libs[list_unuse_lib]
        #libs = sorted(libs, key=lambda l: l.ex, reverse=True)

        for l in libs[:USE_LIBRARY]:
            # deep copy は遅い
            #ns = copy.deepcopy(s)
            #nl = copy.deepcopy(l)

            ns = copy.copy(s)
            ns.libraries = copy.copy(s.libraries)
            ns.books = copy.copy(s.books)
            nl = copy.copy(l)
            nl.books_submit = copy.copy(l.books_submit)

            res = ns.addLibrary(nl)

            if res:
                queue.append(ns)

# BAR.close()

out = max_s[-1]
books = out.books
print(len(out.libraries), "図書館")
print(len(np.where(books == 1)[0]), "冊")
out.printScore()


# 出力ファイル作成
OUTPUT = out.makeOutput()

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
