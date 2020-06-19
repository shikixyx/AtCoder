"""
import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
"""
# AC
# pypy3

N = int(input())
A = list(map(int, input().split()))

BIT = [0] * 22

for a in A:
    for i in range(21):
        BIT[i] += a & 1
        a >>= 1

ANS = 0

while any(BIT):
    k = 1
    c = 0
    for i in range(21):
        if BIT[i]:
            c += k
            BIT[i] -= 1
        k <<= 1

    ANS += c * c


print(ANS)
