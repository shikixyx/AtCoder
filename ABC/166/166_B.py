import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())
T = set()

for _ in range(K):
    d = int(input())
    A = set(map(int, input().split()))
    T |= A

print(N - len(T))
