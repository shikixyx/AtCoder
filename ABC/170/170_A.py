import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A = list(map(int, input().split()))

print(A.index(0) + 1)
