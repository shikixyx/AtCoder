import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

K = int(input())
A, B = map(int, input().split())

ok = False
for i in range(A, B + 1):
    if i % K == 0:
        ok = True


if ok:
    print("OK")
else:
    print("NG")

