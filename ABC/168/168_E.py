import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 1000000007

N = int(readline())
AB = [list(map(int, readline().split())) for _ in range(N)]

CNT = defaultdict(int)
GCD = []

for i in range(N):
    a, b = AB[i]
    d = math.gcd(a, b)
    GCD.append(d)
    a //= d
    b //= d

    CNT[(a, b)] += 1


ANS = pow(2, N, MOD) - 1

C = defaultdict(bool)
for i in range(N):
    a, b = AB[i]
    d = GCD[i]

    a //= d
    b //= d

    y = CNT[(a, b)]
    x = 0

    if C[(a, b)]:
        continue

    if not C[(b, -a)]:
        x += CNT[(b, -a)]

    if not C[(-b, a)]:
        x += CNT[(-b, a)]

    t = (pow(2, y, MOD) - 1) * (pow(2, x, MOD) - 1)
    t %= MOD
    t *= pow(2, N - x - y, MOD)
    t %= MOD

    ANS -= t
    ANS %= MOD
    C[(a, b)] = True


print(ANS)
