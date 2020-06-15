import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
POND = [list(input()) for _ in range(H)]




