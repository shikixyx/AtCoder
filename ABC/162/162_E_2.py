import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())

# AC
# powのMODを忘れてた


# nの約数列挙
def divisor(n):
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if i**2 == n:
                continue
            ans.append(n // i)
    return ans  # sortされていない


MOD = 10 ** 9 + 7

ans = 0
num = 0
CNT = [0] * (K+1)
for i in range(K, 1, -1):
    n = K // i
    c = pow(n, N, MOD)

    c -= CNT[i]

    num += c

    f = divisor(i)
    for n in f:
        CNT[n] += c

    ans += c * i
    ans %= MOD


al = pow(K, N, MOD)
ans += al - num
ans %= MOD

print(ans)
