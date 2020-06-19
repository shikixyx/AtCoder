import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

K = int(input())

REP = [1] * 10
CNT = 1
i = 0

while CNT < K:
    CNT //= REP[i]
    REP[i] += 1
    CNT *= REP[i]

    # 最後の数字なら0に
    i = 0 if i == 9 else i + 1

S = []
STR = list("codeforces")
for i in range(10):
    S += STR[i] * REP[i]

print("".join(S))
