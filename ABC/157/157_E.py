import sys
sys.setrecursionlimit(10 ** 7)

# AC
# Python3 (3.4.3) TLE
# PyPy3 (2.4.0) 1572 ms


class SegmentTree:
    """
    引数：
        N: 処理する区間の長さ
        operator: モノイド演算 (max, min, __add__,ラムダ式,関数定義など)
        UNIT: 単位元
        a: 長さNの配列 a で初期化（a を与えない場合、単位元で初期化）
    注意: 内部的には 1-indexed
    """

    def __init__(self, N, operator, unit, a=None):
        self.op = operator
        self.UNIT = unit

        self.N0 = 2**(N-1).bit_length()
        self.tree = [self.UNIT]*(2*self.N0)
        if a != None:
            self.tree[self.N0:self.N0+N] = a[:]
            for k in range(self.N0-1, 0, -1):
                self.tree[k] = self.op(self.tree[2*k], self.tree[2*k+1])

    # a_k の値を x に更新
    def update(self, k, x):
        k += self.N0
        self.tree[k] = x
        k //= 2
        while k:
            self.tree[k] = self.op(self.tree[2*k], self.tree[2*k+1])
            k //= 2

    # 区間[l,r)をopでまとめる
    def query(self, l, r):
        L = l + self.N0
        R = r + self.N0
        s = self.UNIT
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(self.tree[R], s)
            if L & 1:
                s = self.op(s, self.tree[L])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def get(self, k):  # k番目の値を取得。query[k,k]と同じ
        return self.tree[k + self.N0]

    def all(self):
        return self.tree[1]


N = int(input())
S = input()
S = list(S)


def ope(x, y):
    r = []
    if type(x) is str and type(y) is str:
        r = [x, y]
    elif type(x) is str:
        r = [x] + y
    elif type(y) is str:
        r = x + [y]
    else:
        r = x + y

    return list(set(r))


seg = SegmentTree(N, ope, '-', S)

Q = int(input())

ans = []
for _ in range(Q):
    q, a, b = input().split()

    if q == '1':
        seg.update(int(a) - 1, b)
    else:
        r = seg.query(int(a) - 1, int(b))
        ans.append(str(len(r)-1))


print("\n".join(ans))
