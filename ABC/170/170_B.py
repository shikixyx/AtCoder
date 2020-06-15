import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X, Y = map(int, input().split())

ans = -1
for i in range(X + 1):
    if i * 2 + (X - i) * 4 == Y:
        ans = i

if ans == -1:
    print("No")
else:
    print("Yes")
