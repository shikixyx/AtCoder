import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = list(input())
T = list(input())
L = len(S)

ans = 0
for i in range(L):
    if S[i] == T[i]:
        continue
    ans += 1

print(ans)
