import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    U = int(readline())

    QM = []
    DIGITS = set()
    INITIAL = set()

    SAME_LEN = []

    for _ in range(10 ** 4):
        Q, M = readline().split()
        LQ = len(Q)
        LM = len(M)

        Q = int(Q)

        if Q == -1:
            Q = pow(10, LQ) - 1

        M = M.decode(encoding="utf-8")
        DIGITS |= set(M)
        INITIAL |= set(M[0])
        QM.append((Q, M))

        if LQ == LM:
            q = int(str(Q)[0])
            m = M[0]
            SAME_LEN.append((q, m))

    zero = list(DIGITS - INITIAL)[0]

    str_max = {a: 10 for a in list(INITIAL)}
    for q, m in SAME_LEN:
        str_max[m] = min(q, str_max[m])

    for x in itertools.permutations(list(INITIAL)):
        dct = {a: i + 1 for i, a in enumerate(x)}
        dct[zero] = 0

        str_ok = True
        for m in list(INITIAL):
            if str_max[m] < dct[m]:
                str_ok = False
                break

        if not str_ok:
            continue

        ok = True
        for Q, M in QM:
            val = 0
            for m in M:
                val *= 10
                val += dct[m]

            if val <= Q:
                continue
            else:
                ok = False
                break

        if ok:
            break

    ANS = [None] * 10
    for k, x in dct.items():
        ANS[x] = k

    return ANS


ans = []
for i in range(1, T + 1):
    a = solve()
    txt = "Case #{}: {}".format(i, "".join(map(str, a)))
    ans.append(txt)

print("\n".join(ans))
