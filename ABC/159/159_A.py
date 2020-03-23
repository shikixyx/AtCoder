import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())

if N < 2 and M < 2:
    print(0)
    exit()

ans = 0

ans += N * (N - 1) // 2
ans += M * (M - 1) // 2
print(ans)
