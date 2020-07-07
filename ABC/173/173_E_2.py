import sys
import itertools
import operator

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())
A = list(map(int, input().split()))

pos = [a for a in A if a > 0]
neg = [a for a in A if a < 0]
LP = len(pos)
LN = len(neg)
zer = N - LP - LN

MOD = 10 ** 9 + 7


def solve():
    global N, K, pos, neg, LP, LN, zer, MOD
    # ZERO
    if LP + LN < K:
        return 0

    # 全部使い切るとき
    if LP + LN == K and LP != 0:
        ans = 1
        for n in pos:
            ans *= n
            ans %= MOD
        for n in neg:
            ans *= n
            ans %= MOD

        return ans

    # negative にしかならない
    # 正がなくて、負の数を奇数回使う
    if LP == 0 and K % 2 == 1:
        if zer > 0:
            return 0
        else:
            neg.sort(reverse=True)
            ans = 1
            for n in neg:
                if K == 0:
                    break
                ans *= n
                ans %= MOD
                K -= 1

            return ans

    # positiveにできるなら
    # 2個ずつ比較
    pos.sort()
    neg.sort(reverse=True)

    ans = 1

    while K > 0 and len(neg) >= 2 and len(pos) >= 2:
        # 2個を比べる
        p = pos[-1] * pos[-2]
        n = neg[-1] * neg[-2]

        if n >= p:
            neg.pop()
            neg.pop()

            ans *= n
            ans %= MOD
            K -= 2
        else:
            ans *= pos[-1]
            ans %= MOD
            pos.pop()

            K -= 1

    # あとK個使う必要がある
    if K > 0:
        # negが1個以下
        if len(neg) <= 1:
            # posから取る
            for p in pos:
                ans *= p
                ans %= MOD
                K -= 1
                if K == 0:
                    break
        # posが1個以下
        else:
            while K >= 2:
                ans *= neg[-1]
                ans %= MOD
                ans *= neg[-2]
                ans %= MOD
                K -= 2
                neg.pop()
                neg.pop()

            if K == 1:
                ans *= pos[-1]
                ans %= MOD

    return ans


print(solve())

