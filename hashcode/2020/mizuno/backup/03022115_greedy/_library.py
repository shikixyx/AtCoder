'''
ライブラリとスコアを保持
'''

import numpy as np
import math


class Library:
    def __init__(self, i, n, t, m, books, L):
        self.id = i
        self.num = n
        self.signup = t
        self.perday = m
        self.books = books
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
        self.scores = scores
        self.totaldays = totaldays
        self.point = 0
        num = len(scores)
        self.usebooks = np.zeros(num)

    # 図書館を追加
    def addLibrary(self):
        return 0

    # 図書館のリストを受け取り、スコアを計算
    def calcScore(self, liblist):
        return 0
