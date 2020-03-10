import sys
import bisect
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Not AC
# というかグチャグチャ


N = int(readline())
MOD = 998244353


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


XD = [[int(x) for x in readline().split()] for _ in range(N)]
XD.sort()
X = [x for x, _ in XD]
B = [0] + [bisect.bisect_left(X, x + d) for x, d in XD]
seg = SegmentTree(N+1, max, 0, B)

C = [0] * (N + 1)
for n in range(N, 0, -1):
    r = B[n]
    x = seg.query(n, r)
    C[n] = x
    seg.update(n, x)

print(C)

s = 0
for c in C:
    if c == 0:
        continue
    m = pow(2, c-1, MOD) - 1
    s += m
    s %= MOD

al = pow(2, N, MOD)
#print(al, s)
ans = al - s
ans %= MOD
print(ans)
exit()


for i, b in enumerate(B):
    if b == i or i == N:
        continue
    r = seg.query(i, b + 1)
    C[i] = r - i

s = 0
for c in C:
    m = pow(2, c, MOD) - 1
    s += m
    s %= MOD

al = pow(2, N, MOD)
ans = al - s
ans %= MOD
print(ans)
exit()

E = []
for i, xd in enumerate(XD):
    x, d = xd
    E.append((x, 0, i))
    E.append((x + d - 1, 1, x))

E.sort()

NUM = {}
B = {}
prev = -1
for x, op, r in E:
    if op == 0:
        prev = r
    elif op == 1:
        NUM[x] = prev
        seg.update(r+pow(10, 9), prev)


#R_XD = sorted(XD, reverse=True)

C = {}
for i, xd in enumerate(XD):
    x, d = xd
    b = seg.query(x, x + d)
    C[x] = b - i

s = 0
for x, d in XD:
    #cnt = NUM[x + d - 1] - NUM[x]
    cnt = C[x]
    m = pow(2, cnt, MOD) - 1
    s += m
    s %= MOD

al = pow(2, N, MOD)
ans = al - s
ans %= MOD
print(ans)
