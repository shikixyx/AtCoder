import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

buka = [0] * N

for i in range(N - 1):
    buka[A[i]-1] += 1

print('\n'.join(map(str, buka)))
