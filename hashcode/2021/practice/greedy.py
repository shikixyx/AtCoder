import sys

sys.path.append("/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/practice")

import itertools
from common.common import *

case = sys.argv[1]
M, T2, T3, T4, P, I = load(case)
print(case, M, T2, T3, T4)

i_and_num = [(len(P[i][1]), i) for i in range(M)]
i_and_num.sort(reverse=True)

USED = [False] * M
PIZZA_REST = M

Q = []
for per_team in [4, 3, 2]:
    team_num = 0
    if per_team == 4:
        team_num = T4
    elif per_team == 3:
        team_num = T3
    elif per_team == 2:
        team_num = T2

    for _ in range(team_num):

        if PIZZA_REST < per_team:
            break

        t = []
        for _ in range(per_team):
            num, i = i_and_num.pop()
            t.append(i)

        Q.append(t)
        PIZZA_REST -= per_team



print(calc_score(Q, P))
make_output(Q, case)

