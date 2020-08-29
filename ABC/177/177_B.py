import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = list(input())
T = list(input())

LS = len(S)
LT = len(T)

ans = LT
for i in range(LS - LT + 1):
    t = 0
    for j in range(LT):
        if S[i + j] != T[j]:
            t += 1

    ans = min(ans, t)

print(ans)
