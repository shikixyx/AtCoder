import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
AB = [list(map(int, readline().split())) for _ in range(N)]

LINE = defaultdict(lambda: [0, 0])
for a, b in AB:
    LINE[a][0] += 1
    LINE[b + 1][1] += 1

LINE = list(LINE.items())
LINE.sort()

ans = 0

small = 0
small_able = 0
prevx = -1


if N % 2 == 1:

    mn = 10 ** 10
    mx = 10 ** 10

    flg = False

    for x, p in LINE:
        small_able += p[0]
        small += p[1]

        if small < (N + 1) // 2 and ((N + 1) // 2) <= small_able:
            mn = min(x, mn)

        if (N + 1) // 2 <= small:
            mx = min(mx, x - 1)
            break


else:
    mn_0 = 10 ** 10
    mn_1 = 10 ** 10
    mx_0 = 10 ** 10
    mx_1 = 10 ** 10

    flg_0 = False
    flg_1 = False

    for x, p in LINE:
        small_able += p[0]
        small += p[1]

        if small < N // 2 and (N // 2) <= small_able:
            mn_0 = min(x, mn_0)

        if N // 2 <= small:
            mx_0 = min(mx_0, x - 1)

        if small < (N // 2) + 1 and (N // 2) + 1 <= small_able:
            mn_1 = min(x, mn_1)

        if (N // 2) + 1 <= small:
            mx_1 = min(mx_1, x - 1)
            break

    mn = mn_0 + mn_1
    mx = mx_0 + mx_1


print(mx - mn + 1)
