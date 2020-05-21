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

print(CNT)


ANS = 0

ng = 0

for i in range(N):
    a, b = AB[i]
    d = GCD[i]

    a //= d
    b //= d

    x = CNT[(-b, a)] + CNT[(b, -a)]

    t = pow(2, x, MOD) - 1
    t *= pow(2, N - 1 - i - x, MOD)
    t %= MOD
    ng += t
    ng %= MOD

    CNT[(a, b)] -= 1

print(ng)
al = pow(2, N, MOD) - 1
print(al - ng)
