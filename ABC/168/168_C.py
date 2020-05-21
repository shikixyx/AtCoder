import sys
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, H, M = map(int, input().split())

H = H % 12
X = H * 60 + M

AX = X / 720.0 * 360
BX = M / 60.0 * 360

D = abs(AX - BX + (10 ** -10))

ANS = A ** 2 + B ** 2 - 2 * B * A * math.cos(math.radians(D))

print(math.sqrt(ANS))
