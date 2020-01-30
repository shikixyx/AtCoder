import sys
sys.setrecursionlimit(10 ** 7)

# 反転 (ライツアウト)
# 2回やったら元に戻る

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

if A[0] > X:
    x = X
    ans += A[0] - X
else:
    x = A[0]

for i in range(1, N):
    a = A[i]
    b = max(a - X + x, 0)
    ans += b
    x = A[i] - b

print(ans)
