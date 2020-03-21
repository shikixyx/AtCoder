import numpy as np
import random


def isValid(N, grids):
    q0 = cntQuality(N, grids, 0, 0)

    for i in range(N):
        q = cntQuality(N, grids, i, 0)
        if q0 != q:
            return False

    for i in range(N):
        q = cntQuality(N, grids, i, 1)
        if q0 != q:
            return False
    return True


def cntQuality(N, grids, num, axis):
    q = 0

    if axis == 0:
        g = grids[num, :]
    else:
        g = grids[:, num]

    last = -1

    for i in range(N):
        d = g[i]
        if last != d and d != 0:
            q += 1
            last = d

    return q


def tryDomino(N, iter):
    max_num = (N*N) // 2

    for i in range(iter):
        if i % (10**4) == 0:
            print(i)
        grids = np.zeros((N, N))
        num = random.randrange(1, max_num+1, 1)

        cnt = 10 ** 3
        while(num > 0 and cnt > 0):
            position_x = random.randrange(N)
            position_y = random.randrange(N)
            direct = random.randrange(4)

            # 0 +1
            # 1 -1
            # 2    +1
            # 3    -1
            if direct == 0:
                position_x_2 = position_x + 1
                position_y_2 = position_y
            elif direct == 1:
                position_x_2 = position_x - 1
                position_y_2 = position_y
            elif direct == 2:
                position_x_2 = position_x
                position_y_2 = position_y + 1
            elif direct == 3:
                position_x_2 = position_x
                position_y_2 = position_y - 1

            if not(0 <= position_x <= N-1 and 0 <= position_x_2 <= N-1
                   and 0 <= position_y <= N-1 and 0 <= position_y_2 <= N-1):
                cnt -= 1
                continue

            p1 = grids[position_x][position_y]
            p2 = grids[position_x_2][position_y_2]

            if(p1 == 0 and p2 == 0):
                grids[position_x][position_y] = num
                grids[position_x_2][position_y_2] = num
                num -= 1
                cnt = 10 ** 3
            else:
                cnt -= 1
                continue

        if isValid(N, grids):
            return grids

    return False


grids = tryDomino(7, 10 ** 7)
print(grids)
