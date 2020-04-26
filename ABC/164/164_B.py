import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, C, D = map(int, input().split())

while True:
    C -= B
    if C <= 0:
        break

    A -= D
    if A <= 0:
        break

if C <= 0:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
