import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

K = int(input())
S = list(input())

L = len(S)

if L <= K:
    pass
else:
    S = S[:K]
    S.append("...")

print("".join(S))
