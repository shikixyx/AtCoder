import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = list(input())

L = len(T)
for i in range(L):
    s = T[i]
    if s == "?":
        T[i] = "D"

print("".join(T))
