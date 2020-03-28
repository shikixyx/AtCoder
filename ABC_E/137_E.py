import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA
# 1-Nまでの中での負閉路検出までやる必要がある

N, M, P = map(int, readline().split())
ABC = [[int(x) for x in readline().split()] for _ in range(M)]

INF = 10 ** 12
POINT = [INF] * (N + 1)

POINT[1] = 0

for i in range(N*2 + 1):
    update = False
    for j in range(M):
        a, b, c = ABC[j]
        pt = - (c - P)
        if POINT[a] != INF and POINT[a] + pt < POINT[b]:
            POINT[b] = POINT[a] + pt
            update = True

            if i > N-1 and b == N:
                print(-1)
                exit()

    if not update:
        break

# print(POINT)
pt = -POINT[N]

ans = pt if pt > 0 else 0
print(ans)
