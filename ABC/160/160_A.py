import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = list(input())

if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')

