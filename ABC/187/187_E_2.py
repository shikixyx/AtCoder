import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]

    Q = int(input())
    TEX = [list(map(int, input().split())) for _ in range(Q)]

    E = [[] for _ in range(N + 1)]
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)

    v_to_i = [0] * (N + 1)

    c = 1
    stack = [(1, -1)]
    while stack:
        v, parent = stack.pop()
        # 記録
        v_to_i[v] = c
        c += 1

        # 次の点
        for u in E[v]:
            if u == parent:
                continue

            stack.append((u, v))

    ADD = [[] for _ in range(N + 1)]

    for t, e, x in TEX:
        a, b = AB[e - 1]

        if t == 1:
            # a から bを通らず
            if v_to_i[a] < v_to_i[b]:
                # aの方が根に近い
                ADD[1].append(x)
                ADD[b].append(-x)
            else:
                # bの方が近い
                ADD[a].append(x)
        elif t == 2:
            # b から aを通らず
            if v_to_i[a] < v_to_i[b]:
                # aの方が根に近い
                ADD[b].append(x)
            else:
                # bの方が近い
                ADD[1].append(x)
                ADD[a].append(-x)

    ans = [0] * (N + 1)

    stack = [(1, -1, 0)]
    while stack:
        v, parent, plus = stack.pop()

        if len(ADD[v]) > 0:
            plus += sum(ADD[v])

        ans[v] += plus

        for u in E[v]:
            if u == parent:
                continue
            stack.append((u, v, plus))

    print("\n".join(map(str, ans[1:])))

    return


if __name__ == "__main__":
    main()
