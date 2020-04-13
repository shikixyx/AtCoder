import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X, Y, Z = map(int, input().split())
X, Y = Y, X
X, Z = Z, X

print(X, Y, Z)
