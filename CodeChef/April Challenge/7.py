import itertools
import operator
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC

T = int(readline())

# 逆元求めるよう
MOD = 998244353


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# 結果求めるよう
ZERO = [0, 0]
ONE = [1, 1]
a = [0, 1]
A = [1, 0]

CHOICE = [ZERO, ONE, a, A]
calcRes = [[[None] * 4 for _ in range(4)] for _ in range(3)]


def updateCnt(l, r, op):
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
        ret = 0
    elif g0 == 1 and g1 == 1:
        ret = 1
    elif g0 == 0 and g1 == 1:
        ret = 2
    elif g0 == 1 and g1 == 0:
        ret = 3

    calcRes[op][l][r] = ret
    return


for i, j in itertools.product(range(4), repeat=2):
    for op in range(3):
        updateCnt(i, j, op)


def expr(lst, pos):
    parseDbg = False
    print("INPUT", lst[pos], pos) if parseDbg else None
    # expr := term
    if lst[pos] == '#':
        cnt = [1] * 4
        return pos+1, cnt

    # expr := (expr OP expr)

    # left par
    pos += 1

    # left expr
    print("LEFT START", pos) if parseDbg else None
    pos, left_cnt = expr(lst, pos)
    print("LEFT END", pos) if parseDbg else None

    # op
    op = lst[pos]
    opcode = None
    if op == '&':
        opcode = 0
    elif op == '|':
        opcode = 1
    elif op == '^':
        opcode = 2

    print("op", op, opcode, pos) if parseDbg else None
    # print(opcode)

    pos += 1

    # right expr
    print("RIGHT START", pos) if parseDbg else None
    pos, right_cnt = expr(lst, pos)
    print("RIGHT END", pos) if parseDbg else None

    # right par
    pos += 1

    cnt = [0] * 4
    for i, j in itertools.product(range(4), repeat=2):
        update = calcRes[opcode][i][j]
        cnt[update] += left_cnt[i] * right_cnt[j] % MOD
        cnt[update] %= MOD

    return pos, cnt


def solve():
    S = list(input())
    _, r = expr(S, 0)

    total = sum(r) % MOD
    total_inv = modinv(total, MOD)
    ANS = [x * total_inv % MOD for x in r]

    return ' '.join(map(str, ANS))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
