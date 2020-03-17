import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 構築問題


N, K = map(int, input().split())

up = (N - 1) * (N - 2) // 2

if up < K:
    print(-1)
    exit()

res = []

for i in range(2, N+1):
    res.append((1, i))

K = up - K

for i in range(2, N):
    for j in range(i+1, N + 1):
        if K == 0:
            break
        res.append((i, j))
        K -= 1

    if K == 0:
        break

print(len(res))

for u, v in res:
    print(u, v)
