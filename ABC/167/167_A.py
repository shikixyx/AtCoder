import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = list(input())
T = list(input())

LS = len(S)
LT = len(T)

if LS == (LT - 1) and S == T[:-1]:
    print("Yes")
else:
    print("No")
