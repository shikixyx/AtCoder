import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if W >= V:
    print("NO")
    exit()

D = abs(B - A)
X = V - W

if D <= X * T:
    print("YES")
else:
    print("NO")
