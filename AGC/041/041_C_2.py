import sys
import numpy as np
import random
import copy
import datetime
from line_profiler import LineProfiler
import cProfile
import pstats

sys.setrecursionlimit(10 ** 7)


def isValid(N, grids, q=None):
    q0 = cntQuality(N, grids, 0, 0) if q == None else q

    for i in range(N):
        q = cntQuality(N, grids, i, 0)
        if q0 != q:
            return False

    for i in range(N):
        q = cntQuality(N, grids, i, 1)
        if q0 != q:
            return False
    return True


def hasOver(N, grids, q0):
    for i in range(N):
        q = cntQuality(N, grids, i, 0)
        if q > q0:
            return True

    for i in range(N):
        q = cntQuality(N, grids, i, 1)
        if q > q0:
            return True
    return False


def cntQuality(N, grids, num, axis):
    q = 0

    if axis == 0:
        g = grids[num, :]
    else:
        g = grids[:, num]

    last = -1

    for i in range(N):
        d = g[i]

        if last == d or d == 0:
            continue

        q += 1
        last = d

    return q


def dfs(N, grids, pos, num, q):
    x = pos // N
    y = pos % N

    '''
    if hasOver(N, grids, q):
        return False
    '''

    if y == 0 and x != 0:
        qx = cntQuality(N, grids, x-1, 0)
        if qx != q:
            return False

    # end grids
    if x == N and y == 0:
        # valid
        for i in range(N):
            qy = cntQuality(N, grids, i, 1)
            if qy != q:
                return False
        return grids

    # end grids
    if x == N-1 and y == N-1:
        # valid
        if isValid(N, grids, q):
            return grids
        else:
            return False

    # not yet
    pos += 1

    # horizontal
    if x < N-1 and grids[x][y] == 0 and grids[x+1][y] == 0:
        h_num = num + 1
        # h_grids = copy.copy(grids)
        grids[x][y] = h_num
        grids[x+1][y] = h_num
        g = dfs(N, grids, pos, h_num, q)
        if g is not False:
            return g
        grids[x][y] = 0
        grids[x+1][y] = 0

    # vertical
    if y < N-1 and grids[x][y] == 0 and grids[x][y+1] == 0:
        v_num = num + 1
        # v_grids = copy.copy(grids)
        grids[x][y] = v_num
        grids[x][y+1] = v_num
        g = dfs(N, grids, pos, v_num, q)
        if g is not False:
            return g
        grids[x][y] = 0
        grids[x][y+1] = 0

    # dont put domino
    g = dfs(N, grids, pos, num, q)
    if g is not False:
        return g

    return False


start = datetime.datetime.now()
print("start", start)


N = 7
q = 3
grids = np.zeros((N, N))
g = dfs(N, grids, 0, 0, q)

'''


prof = LineProfiler()
prof.add_function(dfs)
prof.enable()
g = dfs(N, grids, 0, 0, q)
prof.disable()
prof.print_stats()
prof.dump_stats("dfs_line_prf.profile")
'''

'''
pr = cProfile.Profile()
pr.enable()
g = dfs(N, grids, 0, 0, q)
pr.disable()
pr.print_stats()
pr.dump_stats('dfs.profile')
'''
end = datetime.datetime.now()
print("end", end)


print(g)
