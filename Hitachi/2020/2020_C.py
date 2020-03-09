import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 距離3のペア求めようとしてた
# これはNが10^5とかだと絶対無理
# WA

N = int(readline())

E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    E[a].append(b)
    E[b].append(a)

#print("E===", E)

Q = []

DIS3 = [[] for _ in range(N+1)]
for i in range(1, N+1):
    nxt = [(x, i) for x in E[i]]

    Q = nxt
    for j in range(2):
        newQ = []

        while Q:
            a, prev = Q.pop()

            for v in E[a]:
                if v == prev:
                    continue
                newQ.append((v, a))

        if len(newQ) == 0:
            Q = []
            break
        Q = newQ

    DIS3[i] = Q

# print(DIS3)
print(0)
exit()
