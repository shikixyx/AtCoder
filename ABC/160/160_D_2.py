import sys
import itertools
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC


N, X, Y = map(int, input().split())

ans = []

cnt = [0] * (N+1)
for a, b in itertools.combinations(range(1, N + 1), 2):
    d1 = b - a
    d2 = abs(X - a) + abs(Y - b) + 1

    d = min(d1, d2)

    cnt[d] += 1

for i in range(1, N):
    print(cnt[i])
