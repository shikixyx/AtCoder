import math
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())

# AC


def solve():
    DEBUG = False
    N = int(readline())
    A = list(map(int, readline().split()))
    A += [-1]

    INF = 10 ** 6

    cnt = 0
    EVEN = []
    FOUR = []

    # only odd
    odd_cnt = 0
    for i in range(N+1):
        a = A[i]

        if a == -1:
            cnt += odd_cnt * (odd_cnt + 1) // 2
            break

        if a % 2 == 0:
            EVEN.append(i)
            if a % 4 == 0:
                FOUR.append(i)
            cnt += odd_cnt * (odd_cnt + 1) // 2
            odd_cnt = 0
        else:
            odd_cnt += 1

    LE = len(EVEN)
    LF = len(FOUR)
    idx_even = 0
    idx_four = 0
    for i in range(N):
        a = A[i]

        # update even idx
        if EVEN and EVEN[idx_even] <= i and idx_even < LE-1:
            idx_even += 1

        # update four idx
        if FOUR and FOUR[idx_four] <= i and idx_four < LF-1:
            idx_four += 1

        # odd
        # two Even or one Four
        if a % 2 == 1:
            # two Even
            nxt = INF
            if EVEN and idx_even < LE - 1:
                nxt = min(EVEN[idx_even+1], nxt)

            # four
            if FOUR and idx_four < LE and i < FOUR[idx_four]:
                nxt = min(FOUR[idx_four], nxt)

            if nxt == INF:
                continue

            cnt += N - nxt

        # div by four
        elif a % 4 == 0:
            # any will do
            cnt += N - i
        # even
        else:
            # next even
            if EVEN and idx_even < LE and i < EVEN[idx_even]:
                cnt += N - EVEN[idx_even]

    return cnt


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
