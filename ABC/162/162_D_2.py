import itertools
import bisect
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
S = list(input())

R = []
G = []
B = []
for i in range(N):
    s = S[i]
    if s == 'R':
        R.append(i)
    elif s == 'G':
        G.append(i)
    elif s == 'B':
        B.append(i)

cnt = 0
for A, B, C in itertools.permutations([R, G, B]):
    LA = len(A)
    LB = len(B)
    LC = len(C)

    idx_b = 0
    idx_c = 0

    for a in A:
        while B[idx_b] <= a and idx_b < LB-1:
            idx_b += 1

        if B[idx_b] <= a:
            break

        for i in range(idx_b, LB):
            b = B[idx_b]

print(cnt)
