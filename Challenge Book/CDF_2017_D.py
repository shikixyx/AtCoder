import sys
sys.setrecursionlimit(10 ** 7)

# 二分探索
# 最小値の最大化
# 最大値の最小化

N, M = map(int, input().split())
X = []
for _ in range(M):
    x = int(input())
    X.append(x)


def test(t):
    n = 0
    for x in X:
        d = x - (n+1)
        # 前の端に辿り着けない場合
        if d > t:
            return False

        # 自分の位置まで来れる場合
        if (n+1) >= x:
            n = x + t
        else:
            n = max(x + (t-d)//2, x + t - d * 2)

    if n >= N:
        return True

    return False


if (N == M):
    print(0)
    exit()


left = 0  # NG
right = 10**12  # OK


while (right - left) != 1:
    mid = (left + right) // 2
    if test(mid):
        right = mid
    else:
        left = mid

print(right)
