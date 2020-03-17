import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W = map(int, input().split())

al = H * W

if H == 1 or W == 1:
    ans = 1
elif al % 2 == 0:
    ans = al // 2
else:
    ans = (al + 1) // 2

print(ans)
