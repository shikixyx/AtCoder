import itertools
import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)


# 素数
# Eratosthenesの篩

Q = int(input())
LR = []
for _ in range(Q):
    l, r = map(int, input().split())
    LR.append((l, r))

M = 10 ** 5 + 1
is_prime = np.ones(M, np.bool)
is_prime2 = np.ones(M, np.bool)
is_prime[1] = 0

for i in range(2, M):
    if i*i > M:
        break

    if is_prime[i]:
        is_prime[i+i::i] = 0

for i in range(3, M, 2):
    n = (i+1)//2
    is_prime2[i] = is_prime[n]

is_near_2017 = np.ones(M, np.bool)
is_near_2017[2::2] = 0
is_near_2017[1] = 0

for i in range(3, M, 2):
    is_near_2017[i] = is_prime[i] & is_prime2[i]

#cnt = list(itertools.accumulate(is_near_2017))
cnt = np.cumsum(is_near_2017)

ans = []
for l, r in LR:
    a = cnt[r] - cnt[l-1]
    ans.append(str(a))

print("\n".join(ans))
