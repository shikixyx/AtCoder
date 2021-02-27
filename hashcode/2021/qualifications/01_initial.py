import sys

sys.path.append("/Users/hiroaki/Documents/34_AtCoder/hashcode/2021/qualifications")

import itertools
from common.common import *

case = "a"
if len(sys.argv) >= 2:
    case = sys.argv[1]

D, I, S, V, F, PATH, STREETS, LIGHTS, CARS = load(case)

T = Traffic(D, I, S, V, F, PATH, STREETS, LIGHTS, CARS)

schedule = {}
for i in range(I):
    lights = LIGHTS[i]
    schedule[i] = []
    for l in lights:
        schedule[i].append([l, 1])

# print(schedule)
# T.test(schedule)
# exit()

score = T.calc_score(schedule)
print(score)

make_output(schedule, case)

