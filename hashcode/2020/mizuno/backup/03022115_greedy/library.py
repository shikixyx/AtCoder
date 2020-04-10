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


# スコア計算用
class Score:
    # 本のスコアと日数
    def __init__(self, scores, totaldays):
        self.scores = np.array(scores)
        self.totaldays = totaldays
        self.point = 0
        self.libraries = []
        num = len(scores)
        self.usebooks = np.zeros(num)

    # 図書館を追加
    def addLibrary(self, l):
        self.libraries.append(l)

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
        r = self.calcScore(self.libraries)
        return r

    # 出力用のディクショナリ生成
    def makeOutput(self):
        out = {}
        for l in self.libraries:
            out[l.id] = l.books_submit

        return out
