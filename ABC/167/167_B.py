import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, C, K = map(int, input().split())

cnt = 0
cntA = min(A, K)

K -= cntA
if K == 0:
    print(cntA)
    exit()

cntB = min(B, K)
K -= cntB

if K == 0:
    print(cntA)
    exit()

cntC = min(C, K)
K -= cntC

print(cntA - cntC)
exit()
