import itertools
import bisect
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
S = list(input())

STR = [[] for _ in range(3)]
RGB = {'R': 0, 'G': 1, 'B': 2}
for i in range(N):
    s = S[i]
    STR[RGB[s]].append(i)

if not STR[0] or not STR[1] or not STR[2]:
    print(0)
    exit()

cnt = 0
for x, y in itertools.combinations(range(3), 2):
    for a, b in itertools.product(STR[x], STR[y]):
        if b < a:
            a, b = b, a

        c = b + (b - a)

        if N - 1 < c:
            continue

        t = RGB[S[c]]

        if t != x and t != y:
            cnt += 1

ans = len(STR[0]) * len(STR[1]) * len(STR[2]) - cnt
print(ans)
