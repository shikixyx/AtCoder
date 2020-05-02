import sys
import random
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 文字列アルゴリズム
# RollingHash
# ローリングハッシュ

# AC
# 164ms (python3)


# 64bit 溢れないように
class RollingHash:
    MASK30 = (1 << 30) - 1
    MASK31 = (1 << 31) - 1
    MOD = (1 << 61) - 1
    POSITVIZER = MOD * ((1 << 3) - 1)

    def __init__(self, S):
        # 事前計算
        Base = random.randrange(129, (1 << 61) - 1)
        self.Base = Base

        L = len(S)
        powMemo = [0] * (L + 1)
        rhash = [0] * (L + 1)

        powMemo[0] = 1
        for i in range(1, L + 1):
            powMemo[i] = self.calcMod(self.Mul(powMemo[i - 1], Base))

        for i in range(L):
            rhash[i + 1] = self.calcMod(self.Mul(rhash[i], Base) + ord(S[i]))

        self.powMemo = powMemo
        self.rhash = rhash

    def getHash(self, begin, length):
        r = self.calcMod(
            self.rhash[begin + length]
            + self.POSITVIZER
            - self.Mul(self.rhash[begin], self.powMemo[length])
        )

        return r

    def Mul(self, l, r):
        lu = l >> 31
        ld = l & self.MASK31
        ru = r >> 31
        rd = r & self.MASK31
        middle = ld * ru + lu * rd

        return (
            ((lu * ru) << 1) + ld * rd + ((middle & self.MASK30) << 31) + (middle >> 30)
        )

    def calcMod(self, val):
        val = (val & self.MOD) + (val >> 61)
        if self.MOD <= val:
            val -= self.MOD
        return val


N = int(input())
S = input()

RH = RollingHash(S)


def check(n, RH):
    ret = False
    cnt = defaultdict(int)
    for i in range(0, N - n + 1):
        h = RH.getHash(i, n)

        if not cnt[h]:
            cnt[h] = i + 1
        else:
            f = cnt[h]
            if f + n <= i + 1:
                ret = True
                break

    return ret


l = 0  # OK
r = (N // 2) + 1  # NG

while (r - l) != 1:
    mid = (l + r) // 2
    if check(mid, RH):
        l = mid
    else:
        r = mid

print(l)
