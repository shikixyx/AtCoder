import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

cnt = 0
for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        cnt += i

print(cnt)
