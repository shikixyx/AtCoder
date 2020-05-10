import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X = int(input())

b = 10 ** 3
F5 = defaultdict(int)
for i in range(1, 10 ** 3):
    k = pow(i, 5)
    if X <= k:
        b = min(b, i)
    F5[k] = i

b -= 1
while True:
    x = X - pow(b, 5)
    if F5[x]:
        ans = (F5[x], -b)
        break

    b -= 1

print(ans[0], ans[1])
