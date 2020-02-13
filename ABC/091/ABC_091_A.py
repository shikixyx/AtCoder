import sys
sys.setrecursionlimit(10 ** 7)

A, B, C = map(int, input().split())

if (A + B) >= C:
    print('Yes')
else:
    print('No')
