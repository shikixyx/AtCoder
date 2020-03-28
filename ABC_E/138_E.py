import bisect
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 15min

S = list(input())
T = list(input())

LS = len(S)
LT = len(T)

POS = [[] for _ in range(26)]

for i in range(LS):
    n = ord(S[i]) - 97
    POS[n].append(i)


cnt = 0
prev = -1
for i in range(LT):
    n = ord(T[i]) - 97

    if not POS[n]:
        print(-1)
        exit()

    ps = POS[n]
    p = bisect.bisect_right(ps, prev)

    if p == len(ps):
        cnt += 1
        p = bisect.bisect_right(ps, -1)

    prev = ps[p]


ans = cnt * LS + prev + 1
print(ans)
