import sys

sys.setrecursionlimit(10 ** 7)

# WA

N = int(input())
K = int(input())

ans = 0

if K == 1:
    c = 10
    # 桁ごと
    while N >= c:
        ans += 9
        c *= 10

    # あまり
    ans += int(str(N)[0])

elif K == 2:
    i = 2
    c = 100

    if N < 11:
        print(0)
        exit()

    # 桁毎
    while N >= c:
        ans += 9 * (i - 1) * 9
        i += 1
        c *= 10

    print(ans)

    # あまり
    l = len(str(N))
    d1 = int(str(N)[0])
    d2 = int(str(N)[1])

    # 1桁目 1 - d1-1
    if d1 > 0:
        ans += (d1 - 1) * (l - 1) * 9

    # 1桁目 d1
    # 2桁目 0
    if l > 2:
        ans += (l - 2) * 9

    # 2桁目 1-d2
    ans += d2


elif K == 3:
    i = 3
    c = 1000

    if N < 111:
        print(0)
        exit()

    # 桁毎
    while N >= c:
        ans += 9 * ((i-1) * (i-2) // 2) * 9 * 9
        i += 1
        c *= 10

    # あまり
    l = len(str(N))
    d1 = int(str(N)[0])
    d2 = int(str(N)[1])
    d3 = int(str(N)[2])

    # 1桁目 1 - d1-1
    if d1 > 0:
        ans += (d1 - 1) * ((l - 1) * (l - 2) // 2) * 9 * 9

    # 1桁目 d1
    # 2桁目 0
    if l > 3:
        ans += ((l - 2) * (l-3) // 2) * 9 * 9

    # 2桁目 1 - d2-1
    if d2 >= 1:
        ans += (d2 - 1) * (l - 2) * 9

    # 2桁目 d2
    # 3桁目 0
    if l > 3:
        ans += (l - 2) * 9

    # 3桁目 1-d3
    ans += d3


print(ans)
