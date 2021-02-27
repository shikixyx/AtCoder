from hashlib import new
from common.common import *
import itertools
import sys
import random

sys.path.append(
    "/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/qualifications")


case = "a"
if len(sys.argv) >= 2:
    case = sys.argv[1]

D, I, S, V, F, PATH, STREETS, LIGHTS, CARS = load(case)

T = Traffic(D, I, S, V, F, PATH, STREETS, LIGHTS, CARS)

PASS, QMAX = T.simulate()

"""
schedule = {}
for i in range(I):
    lights = PASS[i].keys()
    t = []
    for l in lights:
        t = PASS[i][l]
        if t == 0:
            continue

        if not i in schedule:
            schedule[i] = []

        schedule[i].append([l, min(t, D)])
"""

schedule = {}
for i in range(I):
    lights = PASS[i].keys()
    t = []
    for l in lights:
        t = PASS[i][l]
        if t == 0:
            continue

        if not i in schedule:
            schedule[i] = []

        if QMAX[i][l]:
            t = random.randint(1, QMAX[i][l])
        else:
            t = 1
        schedule[i].append([l, min(t, D)])

    if i in schedule:
        random.shuffle(schedule[i])

# print(schedule)

# print(schedule)
# T.test(schedule)
# exit()

now_score = T.calc_score(schedule)
print(now_score)

for iter in range(5):
    i = random.randint(0, I-1)
    if not i in schedule or not schedule[i]:
        continue

    current = schedule[i][:]
    random.shuffle(schedule[i])

    new_score = T.calc_score(schedule)
    if new_score > now_score:
        print("iter: {}  score: {}\r".format(iter, new_score), end="")
    else:
        schedule[i] = current

score = T.calc_score(schedule)
print("\n")
print(score)


make_output(schedule, case)
