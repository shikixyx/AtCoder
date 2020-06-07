import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
AB = [list(map(int, readline().split())) for _ in range(N)]

LINE = []
for a, b in AB:
    LINE.append((a, 0))
    LINE.append((b + 1, 1))

LINE.sort()

ans = 0

small = 0
small_able = 0
prevx = -1


if N % 2 == 1:

    mn = 10 ** 10
    mx = 0

    flg = False

    for x, p in LINE:
        if p == 0:
            small_able += 1
        elif p == 1:
            small += 1

        if (small_able - small) >= ((N + 1) // 2):
            flg = True
            mn = min(mn, x)

        if flg and not (small_able - small) >= ((N + 1) // 2):
            mx = max(mx, x - 1)
            flg = False

else:
    mn_0 = 10 ** 10
    mn_1 = 10 ** 10
    mx_0 = 0
    mx_1 = 0

    flg_0 = False
    flg_1 = False

    for x, p in LINE:
        if p == 0:
            small_able += 1
        elif p == 1:
            small += 1

        # N // 2
        if (small_able - small) >= ((N) // 2):
            flg_0 = True
            mn_0 = min(mn_0, x)

        if flg_0 and not (small_able - small) >= ((N) // 2):
            mx_0 = max(mx_0, x - 1)
            flg_0 = False

        # N // 2 + 1
        if (small_able - small) >= ((N // 2) + 1):
            flg_1 = True
            mn_1 = min(mn_1, x)

        if flg_1 and not (small_able - small) >= ((N // 2) + 1):
            mx_1 = max(mx_1, x - 1)
            flg_1 = False

    mn = mn_0 + mn_1
    mx = mx_0 + mx_1

    print(mn, mx)


print(mx - mn + 1)
