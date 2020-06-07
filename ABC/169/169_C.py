import sys
from decimal import *
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B = input().split()

if A == "0":
    print(0)
    exit()

getcontext().prec = 10 ** 10

ANS = Decimal(A) * Decimal(B)
print((math.floor(ANS)))
