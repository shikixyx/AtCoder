import sys
import bisect
sys.setrecursionlimit(10 ** 7)

# Not AC
# Code On Contest

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
cnt_a_minus = bisect.bisect_left(A, 0)
cnt_a_plus = bisect.bisect_right(A, 0)
cnt_a_zero = plus - minus

cnt_p_negative = cnt_a_minus * cnt_a_plus
cnt_p_positive = (cnt_a_plus * (cnt_a_plus - 1) // 2) + \
    (cnt_a_minus * (cnt_a_minus - 1) // 2)
cnt_p_zeros = (N * N - 1) // 2 - (positive + negative)

if cnt_p_negative < K and K <= (cnt_p_negative + cnt_p_zeros):
    print(0)
    exit()
elif K <= cnt_p_negative:
    minus = A[:minus]
    plus = A[plus:]
    A0.sort(reverse=True)
    A0 = [-x for x in A0]

    def test(val):
        cnt = 0
        return cnt

elif negative < K and K <= (negative + zeros):
    A0 = A[:minus]


if K <= negative:
    A0 = A[:minus]
    A1 = A[plus:]
    A1.sort()

    left = -(10 ** 18)
    right = 0

    print(A0)
    print(A1)

    def test(val):
        cnt = 0
        lg = len(A0)
        for a0 in A0:
            p = val // a0
            cnt += lg - bisect.bisect_left(A1, p)
        return cnt

    while (right - left) > 1:
        mid = (left + right) // 2
        res = test(mid)
        print("mid,cnt", mid, res)
        if res >= K:
            right = mid
        else:
            left = mid

    print(left)
    exit()


elif negative < K and K <= (negative + zeros):
    print(0)
    exit()
else:
    A0 = A[:minus]
    A1 = A[plus:]

    A0.sort(reverse=True)

    K -= zeros + negative

    def test(val):
        cnt = 0
        lg = len(A0)
        if lg > 1:
            for i in ren(lg - 1):
                l = i+1
                r = len(lg) - 1

                a0 = A0[i]
                if val < a0 * A0[l]:
                    continue

                while (r - l) > 1:
                    m = (l + r) // 2
                    if val < a0 * A0[m]:
                        r = m
                    else:
                        l = m

                cnt += l

        lg = len(A1)
        if lg > 1:
            for i in ren(lg - 1):
                l = i+1
                r = len(lg) - 1

                a0 = A0[i]
                if val < a0 * A0[l]:
                    continue

                while (r - l) > 1:
                    m = (l + r) // 2
                    if val < a0 * A0[m]:
                        r = m
                    else:
                        l = m

                cnt += l
        return cnt

    left = 0
    right = 10 ** 18

    while (right - left) > 1:
        mid = (left + right) // 2
        res = test(mid)
        if res >= K:
            right = mid
        else:
            left = mid

    print(left)
    exit()
