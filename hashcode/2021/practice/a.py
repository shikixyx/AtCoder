import sys

sys.path.append("/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/practice")

import itertools
from common.common import *

M, T2, T3, T4, P, I = load("a")

m = 0
ans = []

for O in itertools.permutations(range(5)):
    for T in itertools.permutations([2, 3, 3, 4]):
        Q = []
        lo = len(O)
        i = 0

        for j in range(len(T)):
            lt = T[j]

            if lo >= lt:
                t = []
                lo -= lt
                while lt > 0:
                    t.append(O[i])
                    i += 1
                    lt -= 1

                Q.append(t)
            else:
                break

        score = calc_score(Q, P)
        print(Q, score)

        if score > m:
            m = score
            ans = Q[:]
            # print("update", m, ans)


print(ans, calc_score(ans, P))
make_output(ans, "a")

