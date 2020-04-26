import sys
import copy
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

INF = 10 ** 12
N, M, S = map(int, input().split())
PATH = [[] for _ in range(N + 1)]

for _ in range(M):
    U, V, A, B = map(int, input().split())
    PATH[U].append([V, A, B])
    PATH[V].append([U, A, B])

CHANGE = [None] * (N + 1)

for i in range(N):
    C, D = map(int, input().split())
    CHANGE[i + 1] = (C, D)


def dfs(state, sts, parent):

    u, mn, visited, ginka = state

    for v, a, b in PATH[u]:
        if v == parent:
            continue

        ginka -= a
        mn += b

        if ginka < 0:
            need = -ginka

            change_t_c = (INF, 0)
            vs = list(set(visited))
            for w in vs:
                c, d = CHANGE[w]

                get = -(-need // c)
                t = get * d

                change_t_c = min((t, -get), change_t_c)

            t, get = change_t_c[0], -change_t_c[1]
            mn += t
            ginka += get

        nv = copy.copy(visited)
        nv.append(v)
        new_state = (v, mn, nv, ginka)
        sts[v] = new_state
        print(sts)

        dfs(new_state, sts, u)

    return


state = [1, 0, [1], S]
ANS = [INF] * (N + 1)
ANS[1] = 0
USED = [False] * (N + 1)
USED[1] = True

for i in range(N - 1):
    sts = [None] * (N+1)
    dfs(state, sts, -1)

    print(sts)

    time = [INF] * (N + 1)
    for i in range(N+1):
        if i == 0 or i == 1:
            continue

        if USED[i]:
            continue
        time[i] = sts[i][1]

    print(time)

    m = min(time)
    idx = time.index(m)
    ANS[idx] = m
    USED[idx] = True
    state = sts[idx]

print("\n".join(map(str, ANS[2:])))
