import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

D, T, S = map(int, input().split())

if T * S < D:
    print("No")
else:
    print("Yes")
