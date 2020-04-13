import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

MOD = 10**9 + 7
fact = [1]
fact_inv = [1]  # numpyなし
for i in range(10**5 + 10):
    new_fact = fact[-1]*(i+1) % MOD
    fact.append(new_fact)
    fact_inv.append(pow(new_fact, MOD-2, MOD))


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] % mod


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
K1 = K-1
mx = N-K
px = K-1

for i in range(K-1, N):
    cnb = mod_comb_k(i, K1, MOD)
    #print("cnb", cnb, "px", A[px], "mx", A[mx], "ans", ans)
    ans += A[px] * cnb
    ans %= MOD
    ans -= A[mx] * cnb
    ans %= MOD
    px += 1
    mx -= 1

print(ans)


'''
px = K - 1
mx = N - K
cnb = 0
k2 = K - 2
'''

'''
for i in range(1, N):
    if px > N-1:
        break

    cnb += mod_comb_k(i, k2, MOD)

    print("cnb", cnb, "px", A[px], "mx", A[mx], "ans", ans)
    ans += A[px]
    #ans %= MOD
    ans -= A[mx]
    #ans %= MOD

    px += 1
    mx -= 1
'''

# print(ans)
