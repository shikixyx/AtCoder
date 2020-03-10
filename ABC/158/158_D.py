import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = deque(input())

Q = int(input())
TURN = False

for _ in range(Q):
    q = input()
    if q[0] == '1':
        TURN = not TURN
        continue

    _, f, c = q.split()

    FIRST = True if f == '1' else False

    if (FIRST and (not TURN)) or ((not FIRST) and TURN):
        S.appendleft(c)
    else:
        S.append(c)


if TURN:
    S.reverse()

print(''.join(S))
