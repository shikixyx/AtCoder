import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 2部グラフ
# 二部グラフ

N = int(readline())

E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    E[a].append(b)
    E[b].append(a)

DIST = [-1] * (N+1)
STACK = [1]
DIST[1] = 0

'''
距離を求めて、2で割る
木ならこれでOK

while STACK:
    v = STACK.pop()

    for w in E[v]:
        if DIST[w] == -1:
            DIST[w] = DIST[v] + 1
            STACK.append(w)
'''

COLOR = [None] * (N + 1)


def setColor(v, c):
    COLOR[v] = c
    for w in E[v]:
        if COLOR[w] == None:
            setColor(w, -c)


setColor(1, 1)

EVEN = [i for i, x in enumerate(COLOR) if x == 1 and i > 0]
ODD = [i for i, x in enumerate(COLOR) if x == -1 and i > 0]

listN = list(range(1, N + 1))
mod1 = deque(listN[0::3])
mod2 = deque(listN[1::3])
mod0 = deque(listN[2::3])

ANS = [-1] * (N+1)


def assign(target, arr1, arr2=[], arr3=[]):
    source = [arr1, arr2, arr3]
    idx = 0
    for e in target:
        if len(source[idx]) == 0:
            idx += 1

        ANS[e] = source[idx].pop()
    return 0


if len(EVEN) <= len(mod0):
    assign(EVEN, mod0)
    assign(ODD, mod0, mod1, mod2)
elif len(ODD) <= len(mod0):
    assign(ODD, mod0)
    assign(EVEN, mod0, mod1, mod2)
else:
    assign(EVEN, mod1, mod0)
    assign(ODD, mod2, mod0)

ANS = ANS[1:]
print(' '.join(map(str, ANS)))
