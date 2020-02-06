import sys
sys.setrecursionlimit(10 ** 7)

X, Y = map(int, input().split())

cnt_d1 = 0
cnt_d2 = 0

diff = Y - X
if diff == 0:
    if X % 3 != 0:
        print(0)
        exit()
    cnt_d1 = X // 3
    cnt_d2 = cnt_d1
elif diff > 0:
    Y -= 2 * diff
    X -= 1 * diff
    if X < 0 or X % 3 != 0:
        print(0)
        exit()

    cnt_d1 = X // 3
    cnt_d2 = diff + X // 3
else:
    diff = - diff
    X -= 2 * diff
    Y -= 1 * diff
    if X < 0 or X % 3 != 0:
        print(0)
        exit()

    cnt_d1 = diff + X // 3
    cnt_d2 = X // 3

MOD = 10**9 + 7
fact = [1]
fact_inv = [1]
for i in range(cnt_d1+cnt_d2 + 10):
    new_fact = fact[-1]*(i+1) % MOD
    fact.append(new_fact)
    fact_inv.append(pow(new_fact, MOD-2, MOD))


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] % mod


print(mod_comb_k(cnt_d1+cnt_d2, cnt_d1, MOD))

'''
dp = np.array([[0] * (Y + 1) for _ in range(X + 1)], dtype=np.int64)
#dp = [np.zeros(Y+1, np.int64) for _ in range(X+1)]
print(dp)

for i in range(X):
    if i > 0:
        dp[i] = dp[i]
'''
