import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = input()

if S == 'AAA' or S == 'BBB':
    print('No')
else:
    print('Yes')
