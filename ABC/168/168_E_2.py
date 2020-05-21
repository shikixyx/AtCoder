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


ANS = pow(2, N, MOD) - 1

print(ANS)

for i in range(N):
    a, b = AB[i]
    d = GCD[i]

    a //= d
    b //= d

    x = CNT[(-b, a)] + CNT[(b, -a)]

    if x == 0:
        continue

    t = pow(2, x, MOD) - 1
    t %= MOD
    t *= pow(2, N - i - x - 1, MOD)
    t %= MOD

    print(ANS, t, a, b, i)

    ANS -= t
    ANS %= MOD
    CNT[(a, b)] -= 1


print(ANS)
