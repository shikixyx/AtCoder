import sys
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())

ans = 0
for n in range(N + 1):
    # 無理
    if n <= K:
        continue

    if K == 0:
        ans += N
        continue

    # 倍数分
    ans += (N // n) * (n - K)
    # あまり分
    if K <= (N % n):
        ans += (N % n) - K + 1


print(ans)
