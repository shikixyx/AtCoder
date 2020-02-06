import sys
import math
sys.setrecursionlimit(10 ** 7)

N = int(input())
CITY = [[int(x) for x in input().split()] for _ in range(N)]

l = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        ci = CITY[i]
        cj = CITY[j]
        d = math.sqrt((ci[0] - cj[0]) ** 2 + (ci[1] - cj[1]) ** 2)
        l += math.factorial(N - 1) * d

print(l / math.factorial(N))
