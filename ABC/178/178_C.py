import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

MOD = 10 ** 9 + 7

ALL = pow(10, N, MOD)
ONE = pow(9, N, MOD)
TWO = pow(8, N, MOD)

ans = ALL - ONE - ONE + TWO
ans %= MOD

print(ans)

