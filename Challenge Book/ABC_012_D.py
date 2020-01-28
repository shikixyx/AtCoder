import sys
sys.setrecursionlimit(10 ** 7)

# ワーシャル–フロイド法
# Warshall–Floyd Algorithm
# 全点経路探索

N, M = map(int, input().split())
INF = 10**10
d = [[INF] * N for _ in range(N)]


for _ in range(M):
    a, b, t = map(int, input().split())
    d[a-1][b-1] = t
    d[b-1][a-1] = t

for i in range(N):
    d[i][i] = 0

# ループ順大事
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

m = min(d, key=lambda x: max(x))
print(max(m))
