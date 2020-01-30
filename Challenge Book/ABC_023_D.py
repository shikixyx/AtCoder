import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

# 二分探索
# 判定問題にするテクニック

N = int(input())
HS = np.array([input().split() for _ in range(N)], dtype=np.int64)
H = HS[:, 0]
S = HS[:, 1]

# 割れるまでの時間
t = np.arange(N, dtype=np.int64)


def test(x):
    T = (x - H) // S
    T.sort()
    return (T >= t).all()


# NG
left = 0
# OK
right = 10 ** 15

while (right - left) != 1:
    mid = (left + right) // 2
    if test(mid):
        right = mid
    else:
        left = mid

print(right)
