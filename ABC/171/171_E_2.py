import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

T = 0
for a in A:
    T ^= a

ANS = []
for a in A:
    ANS.append(T ^ a)

print(" ".join(map(str, ANS)))

