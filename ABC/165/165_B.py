import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


import math


X = int(input())
ans = 0
t = 100.0

while t < X:
    t = math.floor(t * 1.01)
    ans += 1

print(ans)
