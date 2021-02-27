import pickle
import datetime
import random
import math
import time


def load(case):
    with open(
        "/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/practice/input/{}".format(
            case
        ),
        mode="r",
    ) as f:
        M, T2, T3, T4 = map(int, f.readline().split())
        P = []
        I = []
        for _ in range(M):
            C = f.readline().split()
            P.append([int(C[0]), C[1:]])
            I.append(int(C[0]))

    return M, T2, T3, T4, P, I


def calc_score(Q, P):
    ret = 0
    for l in Q:
        s = set()
        people = len(l)
        for i in range(people):
            s |= set(P[l[i]][1])

        ret += len(s) ** 2

    return ret


def make_output(Q, case):
    now = datetime.datetime.now()
    out_file = "{}_{}.txt".format(case, now.strftime("%Y%m%d%H%M"))
    L = len(Q)
    with open(
        "/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/practice/output/{}".format(
            out_file
        ),
        mode="w",
    ) as f:
        f.write(str(L))
        f.write("\n")

        for x in Q:
            x = [len(x)] + x
            f.write(" ".join(map(str, x)))
            f.write("\n")


## 温度設定
## http://gasin.hatenadiary.jp/entry/2019/09/03/162613


def simulated_annealing(initial_state, get_cost, get_neighbors, P):
    """Peforms simulated annealing to find a solution"""
    ## 一回の遷移で動きうるスコア幅の最大値程度
    initial_temp = 1000

    ## 一回の遷移で動きうるスコア幅の最小値程度
    final_temp = 1

    ## 線形でstart_tempからend_tempに減少する
    alpha = 0.9

    ## 時間を指定する
    TIME_LIMIT = 300
    start = time.perf_counter()

    ## 冷却のタイプ
    TYPE = "TIME"
    # TYPE = "ALPHA"

    current_temp = initial_temp

    # Start by initializing the current state with the initial state
    current_state = initial_state
    solution = current_state

    while current_temp > final_temp:
        # neighbor = random.choice(get_neighbors())
        neighbor = get_neighbors(current_state)

        # Check if neighbor is best so far
        cur_cost = get_cost(current_state, P)
        new_cost = get_cost(neighbor, P)
        cost_diff = new_cost - cur_cost

        # if the new solution is better, accept it
        if cost_diff > 0:
            # solution = neighbor[:]
            current_state = neighbor
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            if random.uniform(0, 1) < math.exp(cost_diff / current_temp):
                current_state = neighbor[:]

        # decrement the temperature

        if TYPE == "ALPHA":
            current_temp *= alpha
        elif TYPE == "TIME":
            now = time.perf_counter()
            elapsed = now - start
            t = elapsed / TIME_LIMIT
            if t > TIME_LIMIT:
                break
            current_temp = (initial_temp ** (1 - t)) * (final_temp ** t)

        print(
            "current_temp: {}  cost: {} \r".format(
                current_temp, get_cost(current_state, P)
            ),
            end="",
        )

    print("\n")

    # return solution
    return current_state

