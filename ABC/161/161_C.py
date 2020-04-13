import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())

a = N % K
b = (-N) % K

ans = min(a, b)

print(ans)
