import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

# 半分全列挙


N, M = map(int, readline().split())
P = np.array([0] + read().split(), np.int64)

P = P[P <= M]
P2 = (P[:, None] + P[None, :]).ravel()
P2 = P2[P2 <= M]
P2.sort()

# numpyで並列にやらないと間に合わない
I = np.searchsorted(P2, M-P2, side='right') - 1
P4 = P2 + P2[I]

print(max(P4))
