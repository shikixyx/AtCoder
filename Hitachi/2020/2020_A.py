import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = input()

if S == 'hi' or S == 'hihi' or S == 'hihihi' or S == 'hihihihi' or S == 'hihihihihi':
    print('Yes')
else:
    print('No')
