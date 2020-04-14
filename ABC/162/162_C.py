import math
import itertools
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

K = int(input())

ans = 0
for x, y, z in itertools.product(range(1, K + 1), repeat=3):
    a = math.gcd(x, y)
    b = math.gcd(a, z)
    ans += b

print(ans)
