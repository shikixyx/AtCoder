import sys
import bisect
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA
# 何がおかしいか、もうわからない。。。


N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()


def test(x):
    cnt = 0

    for a in A:
        if a == 0:
            if 0 <= x:
                t = N - 1
            else:
                t = 0

        elif a > 0:
            m = x / a
            i = bisect.bisect_right(A, m)
            t = i
            if a <= m:
                t -= 1
        elif a < 0:
            m = x / a
            i = bisect.bisect_left(A, m)
            t = N - i
            if m <= a:
                t -= 1

        cnt += t

    cnt //= 2

    return K <= cnt


l = -(10 ** 19)  # NG
r = 10 ** 19  # OK

while l + 1 != r:
    mid = (l + r) // 2

    if test(mid):
        r = mid
    else:
        l = mid

print(r)
