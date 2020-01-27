import itertools

N, M = map(int, input().split())
G = [[0] * N for i in range(N)]
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1

if N == 1:
    print(1)
    exit()

for x in itertools.permutations(range(1, N), N-1):
    prev = 0
    for i in range(N-1):
        if G[prev][x[i]] == 0:
            break

        prev = x[i]

        if i == N-2:
            cnt += 1

print(cnt)
