import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

# 座標圧縮
# 座圧

N, M = map(int, input().split())
PY = [[int(x) for x in input().split()] for _ in range(M)]

PREFECTURE = defaultdict(list)
for p, y in PY:
    PREFECTURE[p].append(y)

for i in PREFECTURE.keys():
    ys = sorted(PREFECTURE[i])
    y_to_i = {y: i+1 for i, y in enumerate(ys)}
    PREFECTURE[i] = y_to_i

for p, y in PY:
    print('{:06}{:06}'.format(p, PREFECTURE[p][y]))
