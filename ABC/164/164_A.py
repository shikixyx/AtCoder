import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S, W = map(int, input().split())

if W >= S:
    ans = "unsafe"
else:
    ans = 'safe'

print(ans)
