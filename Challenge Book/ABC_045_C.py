import sys
import copy
from collections import deque

sys.setrecursionlimit(1000000000)

def dfs(xs,q):
    if len(xs) == 0:
        return sum(int(i) for i in q)

    x = xs.popleft()

    if len(q) == 0:
        q.append(x)
        return dfs(xs,q)


    a1 = copy.copy(xs)
    a2 = copy.copy(xs)

    q1 = copy.copy(q)
    q2 = copy.copy(q)

    q1.append(x)

    y  = q2.pop()
    yx = y + x
    q2.append(yx)

    return dfs(a1,q1) + dfs(a2,q2)


s  = str(input())
xs = deque(list(s))

print(dfs(xs,deque([])))