import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

ma = max(A)
cnt = 0
ans = 1

for k in range(2, ma + 1):
    c = 0
    for a in A:
        if k <= a and a % k == 0:
            c += 1

    if cnt < c:
        ans = k
        cnt = c

print(ans)
