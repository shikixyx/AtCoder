import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H1, M1, H2, M2, K = map(int, input().split())

S = H1 * 60 + M1
E = H2 * 60 + M2

print(E - K - S)
