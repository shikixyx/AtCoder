import pickle
import datetime
import random
import math
import time
from tqdm import tqdm
from numba import jit


def load(case):
    with open(
        "/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/qualifications/input/{}.txt".format(
            case
        ),
        mode="r",
    ) as f:
        D, I, S, V, F = map(int, f.readline().split())
        PATH = [[] for _ in range(I + 1)]
        STREETS = {}
        LIGHTS = [[] for _ in range(I + 1)]
        for _ in range(S):
            B, E, name, L = f.readline().split()
            B, E, L = int(B), int(E), int(L)
            PATH[B].append({"end": E, "cost": L, "name": name})
            STREETS[name] = {"begin": B, "end": E, "cost": L}
            LIGHTS[E].append(name)

        CARS = []
        for _ in range(V):
            P = f.readline().split()
            CARS.append({"num": int(P[0]), "streets": P[1:]})

    return D, I, S, V, F, PATH, STREETS, LIGHTS, CARS


def make_output(schedule, case):
    now = datetime.datetime.now()
    out_file = "{}_{}.txt".format(case, now.strftime("%Y%m%d%H%M"))
    L = len(schedule.keys())
    with open(
        "/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/qualifications/output/{}".format(
            out_file
        ),
        mode="w",
    ) as f:
        f.write(str(L))

        for intersection, v in schedule.items():
            f.write("\n")
            f.write(str(intersection))
            f.write("\n")
            f.write(str(len(v)))
            for name, interval in v:
                f.write("\n")
                f.write("{} {}".format(name, interval))


# 温度設定
# http://gasin.hatenadiary.jp/entry/2019/09/03/162613
def simulated_annealing(initial_state, get_cost, get_neighbors, P):
    """Peforms simulated annealing to find a solution"""
    # 一回の遷移で動きうるスコア幅の最大値程度
    initial_temp = 1000

    # 一回の遷移で動きうるスコア幅の最小値程度
    final_temp = 1

    # 線形でstart_tempからend_tempに減少する
    alpha = 0.9

    # 時間を指定する
    TIME_LIMIT = 300
    start = time.perf_counter()

    # 冷却のタイプ
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


class Traffic:
    def __init__(self, D, I, S, V, F, PATH, STREETS, LIGHTS, CARS):
        self.D = D
        self.I = I
        self.S = S
        self.V = V
        self.F = F
        self.PATH = PATH
        self.STREETS = STREETS
        self.LIGHTS = LIGHTS
        self.CARS = CARS

        self.score = 0
        self.now = 0

        # 通れるやつの状態と、信号待ちの状態
        self.LIGHT_STATE = [{} for _ in range(I + 1)]
        self.WAIT = [{} for _ in range(I + 1)]
        self.PASS = [{} for _ in range(I + 1)]
        self.QMAX = [{} for _ in range(I + 1)]

        for i in range(I):
            lights = LIGHTS[i]
            for l in lights:
                self.LIGHT_STATE[i][l] = False
                self.WAIT[i][l] = []
                self.PASS[i][l] = 0
                self.QMAX[i][l] = 0

        # 車の状態
        for i in range(V):
            # num,streets
            car = CARS[i]
            streets = car["streets"]
            start_street = streets[0]
            end = STREETS[start_street]["end"]

            # 待ちに追加
            self.WAIT[end][start_street].append(i)

            # 次の状態まで
            self.CARS[i]["now_street_idx"] = 0
            self.CARS[i]["counter"] = 0
            self.CARS[i]["goal"] = False

    def debug_print(self):
        print("now = {}".format(self.now))
        print("LIGHT_STATE")
        print(self.LIGHT_STATE)
        print("CARS")
        print(self.CARS)
        print("WAIT")
        print(self.WAIT)

    def calc_score(self, schedule):
        self.__init__(self.D, self.I, self.S, self.V, self.F, self.PATH,
                      self.STREETS, self.LIGHTS, self.CARS)

        self.update_lights(schedule)
        for _ in range(self.D):
            self.now += 1
            self.update_cars()
            self.update_lights(schedule)

            for i in range(self.I):
                lights = self.LIGHTS[i]
                for l in lights:
                    if self.WAIT[i][l]:
                        self.QMAX[i][l] = max(
                            self.QMAX[i][l], len(self.WAIT[i][l]))

        return self.score

    def simulate(self):
        USE_QMAX = True
        self.update_lights_all()
        for _ in tqdm(range(self.D)):
            self.now += 1
            self.update_cars()

            for i in range(self.I):
                lights = self.LIGHTS[i]
                for l in lights:
                    if self.WAIT[i][l]:
                        self.QMAX[i][l] = max(
                            self.QMAX[i][l], len(self.WAIT[i][l]))

            self.update_lights_all()

        self.now = 0
        self.score = 0

        return self.PASS, self.QMAX

    def update_lights_all(self):
        for intersection in range(self.I):
            lights = self.LIGHTS[intersection]
            for l in lights:
                if self.WAIT[intersection][l]:
                    # 車のID
                    car = self.WAIT[intersection][l].pop()

                    # 今いる道をアプデ
                    now_street_idx = self.CARS[car]["now_street_idx"] + 1
                    self.CARS[car]["now_street_idx"] = now_street_idx

                    now_street = self.CARS[car]["streets"][now_street_idx]

                    # counterを更新
                    self.CARS[car]["counter"] = self.STREETS[now_street]["cost"]

                    self.PASS[intersection][l] += 1

    @jit
    def update_lights(self, schedule):
        # schedule
        # i: street t

        for intersection, streets_and_time in schedule.items():
            # 各交差点毎に
            t = 0
            interval = [0]
            L = len(streets_and_time)
            for street, time in streets_and_time:
                interval.append(t + time)
                t += time

            total = t

            for i in range(1, L + 1):
                name = streets_and_time[i - 1][0]

                # 行ける信号
                if interval[i - 1] <= (self.now % total) < interval[i]:
                    self.LIGHT_STATE[intersection][name] = True

                    # WAITに車いたら出してあげる
                    if self.WAIT[intersection][name]:
                        # 車のID
                        car = self.WAIT[intersection][name].pop()

                        # 今いる道をアプデ
                        now_street_idx = self.CARS[car]["now_street_idx"] + 1
                        self.CARS[car]["now_street_idx"] = now_street_idx

                        now_street = self.CARS[car]["streets"][now_street_idx]

                        # counterを更新
                        self.CARS[car]["counter"] = self.STREETS[now_street]["cost"]

                # 無理な信号
                else:
                    self.LIGHT_STATE[intersection][name] = False

    def test(self, schedule):
        print(self.LIGHTS[0])
        for _ in range(10):
            print("now: {}".format(self.now))
            self.update_lights(schedule)
            print(self.LIGHT_STATE[0])
            self.now += 1

    @jit
    def update_cars(self):
        if self.now > self.D:
            return

        for i in range(self.V):
            if self.CARS[i]["goal"]:
                continue

            # 道路走ってるところ
            if self.CARS[i]["counter"] != 0:
                self.CARS[i]["counter"] -= 1

                # 0になったとき
                if self.CARS[i]["counter"] == 0:
                    # ゴール
                    now_street_idx = self.CARS[i]["now_street_idx"]
                    if now_street_idx == (self.CARS[i]["num"] - 1):
                        self.score += self.F + (self.D - self.now)
                        self.goal = True
                        # print("Goal {} !!".format(i))
                        # print("add {} point".format(self.F + (self.D - self.now)))

                    else:
                        # 　それ以外なら、待ちに追加
                        now_street = self.CARS[i]["streets"][now_street_idx]
                        end = self.STREETS[now_street]["end"]
                        self.WAIT[end][now_street].append(i)
