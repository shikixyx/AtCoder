import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
m = S / (4 * M)
cnt = 0
for a in A:
    if a < m:
        continue
    cnt += 1

if cnt >= M:
    print('Yes')
else:
    print('No')
