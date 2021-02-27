import sys

sys.path.append("/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/practice")

import random
from common.common import *
import copy

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


def get_neighbors(Q):
    L = len(Q)
    i, j = random.sample(range(L), k=2)

    i_k = random.randrange(0, len(Q[i]))
    j_k = random.randrange(0, len(Q[j]))

    # print(i, j)
    # print(Q[i], Q[j])

    neighbors = copy.deepcopy(Q)
    neighbors[i][i_k], neighbors[j][j_k] = neighbors[j][j_k], neighbors[i][i_k]

    return neighbors


print(calc_score(Q, P))


ans = simulated_annealing(Q, calc_score, get_neighbors, P)


print(calc_score(ans, P))

