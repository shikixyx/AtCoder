W = int(input())
N, K = map(int, input().split())

A = [0] * N
B = [0] * N
DP = [[[0] * (W+1) for i in range(K+1)] for j in range(N+1)]

for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

for n in range(N):
    for k in range(K+1):
        for w in range(W+1):
            if w >= A[n] and k >= 1:
                DP[n+1][k][w] = max(DP[n][k-1][w-A[n]] + B[n], DP[n][k][w])
            else:
                DP[n+1][k][w] = DP[n][k][w]

print(DP[N][K][W])
