import sys
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, H, M = map(int, input().split())

AX = 30.0 * H + M / 2.0
BX = M * 6.0

D = AX - BX

ANS = A ** 2 + B ** 2 - 2 * B * A * math.cos(math.radians(D))

print(math.sqrt(ANS))
