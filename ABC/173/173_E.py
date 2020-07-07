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
    # ZERO
    if LP + LN < K:
        return 0

    ret = -float("inf")

    # positive
    pos.sort(reverse=True)
    neg.sort()

    acc_pos = itertools.accumulate(pos, operator.mul)
    acc_neg = itertools.accumulate(neg, operator.mul)

    for cnt_neg in range(0, K, 2):
        cnt_pos = K - cnt_neg
        if LP < cnt_pos:
            continue

        ret = 

    return


# positive
# pos が K個以上
#

