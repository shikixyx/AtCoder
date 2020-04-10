'''
ライブラリとスコアを保持
'''

import math
from collections import deque
import numpy as np


class Library:
    def __init__(self, i, n, t, m, books, L):
        self.id = i
        self.num = n
        self.signup = t
        self.perday = m
        self.books = books
        self.books_submit = books
        self.L = L

    # 出現頻度も加味した図書館の推測評価値
    def calcExpectation(self, FREQ, SCORES):
        perday = self.perday
        signup = self.signup
        books = self.books
        L = self.L
        books_point = {}
        ex = 0
        for b in books:
            # 各本の評価値
            p = SCORES[b] * (math.log(L / FREQ[b]) + 1)
            ex += p

            # 並び替え用
            books_point[b] = p

        # 期待値算出
        ex = (ex / len(books)) * perday
        ex /= signup

        # 評価値で並び替え
        # [key,point]のlist
        books_p_sorted = sorted(
            books_point.items(), key=lambda x: x[1], reverse=True)

        self.ex = ex
        self.books_p_sorted = books_p_sorted

    # 出現頻度の低い順にソート
    def sortBooksByFreq(self, FREQ, SCORES):
        books_freq = [(b, FREQ[b], -SCORES[b]) for b in self.books]
        books_freq_sorted = sorted(books_freq, key=lambda x: (x[1], x[2]))
        books_key = [x[0] for x in books_freq_sorted]

        self.books_submit = books_key

    # スコアの高い順にソート
    def sortBooksByScore(self, FREQ, SCORES):
        books_score = [(b, FREQ[b], -SCORES[b]) for b in self.books]
        books_score_sorted = sorted(books_score, key=lambda x: (x[2], x[1]))
        books_key = [x[0] for x in books_score_sorted]

        self.books_submit = books_key


class Libs:
    def __init__(self, D):
        self.day = D
        self.books = set([])
        self.libs = []
        self.libids = set([])
        self.out = {}

    def calcScore(self, B, books_score):
        flag = np.zeros(B, np.bool)
        flag[list(self.books)] = 1
        r = (books_score * flag).sum()
        return r

    def addLibrary(self, l, books):
        self.books |= set(books)

        self.libids |= set([l.id])
        l.books_submit = books
        self.libs.append(l)

        self.day -= l.signup

        self.out[l.id] = books


# スコア計算用
class Score:
    # 本のスコアと日数
    def __init__(self, scores, totaldays, L, B):
        self.scores = np.array(scores)
        self.totaldays = totaldays
        self.rest = totaldays
        self.L = L
        self.B = B
        self.books = np.zeros(B, dtype=np.bool)
        self.point = 0
        self.ev = 0
        self.libraries = []
        num = len(scores)
        self.usebooks = np.zeros(num)

    # 図書館のIDを返す

    def getLibrariesIDs(self):
        libs = [x.id for x in self.libraries]
        return libs

    # 本の評価値を取得

    def getScoreByBooks(self, books):
        flag = np.zeros(self.B, dtype=np.bool)
        flag[books] = 1
        r = (self.scores * flag).sum()
        return r

    # 図書館を追加
    # 残り日数で追加出来ない場合はFalseを返す
    def addLibrary(self, l):
        d = self.rest
        d -= l.signup

        if d <= 0:
            return False

        # 残っている日数
        self.rest = d
        book_num = d * l.perday

        # 使われている本を列挙
        used_books = np.where(self.books == 1)
        used_books = list(used_books[0])

        # まだ使われていない本から選ぶ
        books_submit = l.books_submit
        books_submit = np.setdiff1d(books_submit, used_books)
        books_submit = books_submit[:book_num]

        # 推定の評価値を登録
        r = self.getScoreByBooks(books_submit)
        ev = r / l.signup
        self.ev = ev

        # 使った本を追加
        l.books_submit = books_submit
        self.books[books_submit] = 1
        self.libraries.append(l)

        return True

    # 図書館のリストを受け取り、スコアを計算
    def calcScore(self, liblist):
        usedBooks = np.zeros(len(self.scores), dtype=np.bool)

        for l in liblist:
            books = l.books_submit
            usedBooks[books] = 1

        r = (self.scores * usedBooks).sum()
        return r

    # 現在のスコアを計算
    def getScore(self):
        #r = self.calcScore(self.libraries)
        r = (self.scores * self.books).sum()
        self.point = r
        return r

    # 現在の推定評価値を計算
    def getEstimateValue(self):
        return self.ev

    # 現在のスコアを表示
    def printScore(self):
        print("{:,}".format(self.point))

    # 出力用のディクショナリ生成
    def makeOutput(self):
        out = {}
        for l in self.libraries:
            out[l.id] = l.books_submit

        return out

    # まだ使ってない図書館を列挙
    def getUnuseLibrary(self):
        list_lib = np.arange(self.L)
        list_used_lib = [l.id for l in self.libraries]
        list_unuse_lib = np.setdiff1d(list_lib, list_used_lib)

        return list_unuse_lib

    # 図書館の並びをprint

    def printLibraries(self):
        libs = [l.id for l in self.libraries]
        print(libs)

    # デバッグ様
    def printDebug(self):
        print()
        print("==== DEBUG SCORE ====")
        print("--libraries--")
        self.printLibraries()
        books = [(l.id, l.books_submit) for l in self.libraries]
        print("--books--")
        print(books)
        print("--score--")
        self.printScore()
        print("====     END     ====")
        print()
