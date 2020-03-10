import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, A, B = map(int, input().split())

c = A + B

if A == 0:
    print(0)
    exit()

ans = 0
cnt = N // c
ans += cnt * A
N -= cnt * c

ans += min(N, A)

print(ans)
