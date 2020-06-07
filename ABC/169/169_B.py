import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit(0)

ans = 1
for a in A:
    ans *= a
    if ans > pow(10, 18):
        print(-1)
        exit(0)

print(ans)
