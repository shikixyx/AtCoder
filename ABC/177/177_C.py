import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))

S = 0
for a in A:
    S += a
    S %= MOD

ans = 0

for a in A:
    t = (S - a) * a
    t %= MOD
    ans += t
    ans %= MOD

fact = [1]
fact_inv = [1]  # numpyなし
for i in range(10):
    new_fact = fact[-1] * (i + 1) % MOD
    fact.append(new_fact)
    fact_inv.append(pow(new_fact, MOD - 2, MOD))

ans *= fact_inv[2]
ans %= MOD

print(ans)

