import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

ANS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)]

for i in range(N - 1):
    ANS += [(i + 3, i + 3), (i + 2, i + 3), (i + 3, i + 2)]

print(len(ANS))

for x, y in ANS:
    print(x, y)
