import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = list(input())

ok = False
for i in range(3):
    if N[i] == '7':
        ok = True

if ok:
    print('Yes')
else:
    print('No')
