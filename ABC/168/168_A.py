import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
n = N % 10

ans = None
if n == 2 or n == 4 or n == 5 or n == 7 or n == 9:
    ans = "hon"
elif n == 0 or n == 1 or n == 6 or n == 8:
    ans = "pon"
elif n == 3:
    ans = "bon"

print(ans)
