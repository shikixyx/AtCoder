import math

N = int(input())
A = list(map(int, input().split()))
A.sort()

# n以下の素数列挙(O(n log(n))
def primes(n):
    ans = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ans.append(i)
    return ans


def fctr1(n):
    f = []
    c = 0
    r = int(n ** 0.5)
    for i in range(2, r + 2):
        while n % i == 0:
            c += 1
            n = n // i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


c = 0
for a in A:
    if a == 1:
        c += 1
    else:
        break


P = primes(A[-1])
L = len(P)

# MAX以下の素数の数より多い
if (N - c) <= L:
    USED = [False] * (10 ** 6 + 10)
    ok = True
    for a in A:
        if a == 1:
            continue

        f = fctr1(a)
        for x, c in f:
            if not USED[x]:
                USED[x] = True
            else:
                ok = False
                break

    if ok:
        print("pairwise coprime")
        exit()

t = A[0]
for a in A:
    t = math.gcd(a, t)
    if t == 1:
        break

if t == 1:
    print("setwise coprime")
else:
    print("not coprime")

