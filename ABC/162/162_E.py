import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# powのMODを忘れてた。。。

N, K = map(int, input().split())

MOD = 10 ** 9 + 7

ans = 0
num = 0
CNT = [0] * (K+1)
for i in range(K, 1, -1):
    n = K // i
    c = pow(n, N, MOD)

    ni = i + i
    while ni <= K:
        c -= CNT[ni]
        ni += i

    ans += c * i
    ans %= MOD
    num += c
    CNT[i] = c

rest = pow(K, N, MOD)
ans += rest - num
ans %= MOD

print(ans)
