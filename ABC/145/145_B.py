import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()

if N % 2 == 1:
    print('No')
    exit()

mid = N // 2
if S[:mid] == S[mid:]:
    print('Yes')
else:
    print('No')
