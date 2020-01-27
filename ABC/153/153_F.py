import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

N, D, A = map(int, input().split())
E = []
for _ in range(N):
    x, h = map(int, input().split())
    E.append((x, h))
    E.append((x+2*D, 0))

E = sorted(E, key=lambda x: (x[0], -x[1]))

for i in range(len(E)-1, -1, -1):
    x, h = E[i]
    if h != 0:
        xmax = x
        break

bomb = defaultdict(int)
damage = 0
ans = 0
for i in range(len(E)):
    x, h = E[i]

    if x > xmax:
        break

    # x+2D: damageをマイナス
    if h == 0:
        damage -= bomb[x]
        continue

    h -= damage

    if h <= 0:
        continue

    x = x + 2 * D
    cnt = -1 * (-h // A)
    damage += cnt * A
    bomb[x] = cnt * A
    ans += cnt

print(ans)
