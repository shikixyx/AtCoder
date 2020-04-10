import operator
import itertools
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

NAME = ["ZERO", "ONE", "a", "A"]
OPNAME = ['AND', 'OR', 'XOR']

ZERO = [0, 0]
ONE = [1, 1]
a = [0, 1]
A = [1, 0]

CHOICE = [ZERO, ONE, a, A]


cnt = [[0] * 4 for _ in range(3)]

calcRes = [[[None] * 4 for _ in range(4)] for _ in range(3)]


def updateCnt(l, r, op):
    print(NAME[l], op, NAME[r])
    L = CHOICE[l]
    R = CHOICE[r]

    if op == 0:
        o = operator.and_
    elif op == 1:
        o = operator.or_
    elif op == 2:
        o = operator.xor

    g0 = o(L[0], R[0])
    g1 = o(L[1], R[1])

    ret = None
    if g0 == 0 and g1 == 0:
        ret = '0'
        cnt[op][0] += 1
    elif g0 == 1 and g1 == 1:
        ret = '1'
        cnt[op][1] += 1
    elif g0 == 0 and g1 == 1:
        ret = 'a'
        cnt[op][2] += 1
    elif g0 == 1 and g1 == 0:
        ret = 'A'
        cnt[op][3] += 1

    calcRes[op][l][r] = ret

    print(ret)

    return ret


for i, j in itertools.product(range(4), repeat=2):
    for op in range(3):
        updateCnt(i, j, op)

print("== RESULT ==")

for i in range(3):
    cn = cnt[i]
    print("OP == ", i)
    print("0: ", cn[0])
    print("1: ", cn[1])
    print("a: ", cn[2])
    print("A: ", cn[3])

for k in range(3):
    res = calcRes[k]
    for i, j in itertools.product(range(4), repeat=2):
        print(i, j, OPNAME[k], res[i][j])
