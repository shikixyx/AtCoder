import math
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    DEBUG = False
    N = int(readline())
    A = list(map(int, readline().split()))
    A += [-1]

    cnt = 0
    EVEN = []
    divByFour = []

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
                divByFour.append(i)
            cnt += odd_cnt * (odd_cnt + 1) // 2
            odd_cnt = 0
        else:
            odd_cnt += 1

    # div By Four

    # has more than 2 even
    LE = len(EVEN)
    for i in range(LE):
        idx, divByFour = EVEN[i]

        # a % 4 == 0
        # always ok
        if divByFour:
            cnt += N - idx
            continue
        else:
            if i == (LE - 1):
                continue

            n_idx, _ = EVEN[i + 1]
            cnt += N - n_idx

    return cnt


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
