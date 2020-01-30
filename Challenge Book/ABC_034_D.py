import sys
sys.setrecursionlimit(10 ** 7)

# 二分探索
# 平均値最大化

N, K = map(int, input().split())
W = []
for _ in range(N):
    w, p = map(int, input().split())
    W.append([w, p])


def test(p):
    l = [x[0] * (x[1] - p) for x in W]
    l.sort(reverse=True)
    r = 0
    for i in range(K):
        r += l[i]

    return r >= 0


left = 0.  # OK
right = 100.  # NG

if test(100):
    print(100)
    exit()

for _ in range(10**3):
    mid = (left + right) / 2
    if test(mid):
        left = mid
    else:
        right = mid

print(left)
