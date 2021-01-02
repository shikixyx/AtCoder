import sys
import operator


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]

    Q = int(input())
    TEX = [list(map(int, input().split())) for _ in range(Q)]

    E = [[] for _ in range(N + 1)]
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)

    v_to_i = {}

    def dfs(v, c, parent):
        # 記録
        v_to_i[v] = c
        c += 1

        # 次の点
        for u in E[v]:
            if u == parent:
                continue

            c = dfs(u, c, v)

        return c

    dfs(1, 1, -1)
    i_to_v = {i: v for v, i in v_to_i.items()}
    initial = [0] + list(i_to_v.values())

    # 新しく辺を作る
    E2 = [[] for _ in range(N + 1)]
    for v in range(1, N + 1):
        i = v_to_i[v]
        e = [v_to_i[u] for u in E[v]]
        E2[i] += e

    ADD = [[] for _ in range(N + 1)]

    for T, e, x in TEX:
        a, b = AB[e - 1]
        p, q = v_to_i[a], v_to_i[b]

        if T == 1:
            s = p
            t = q
        else:
            s = q
            t = p

        EG = E2[s]
        flg = False
        nxt = 10 ** 9
        for y in EG:
            if y > t:
                flg = True
                nxt = min(nxt, y)

        print("QUERY:", T, e, x, s, t)
        print("右の子", flg, nxt)

        # sがtより大きい
        # 1-p-1
        # 右の子-
        if s > t:
            ADD[1].append(x)
            ADD[p].append(-x)

            if flg:
                ADD[nxt].append(x)

        # tの方が大きい
        # sの右の子まで
        else:
            print("hoge", flg)
            ADD[s].append(x)

            if flg:
                ADD[nxt].append(x)
            elif s < N:
                ADD[s + 1].append(-x)

        print(ADD)

    plus = 0
    for i in range(1, N + 1):
        if len(ADD[i]) > 0:
            plus += sum(ADD[i])

        initial[i] += plus

    print(v_to_i)
    # print(ADD)

    ans = []
    for i in range(1, N + 1):
        ans.append(initial[v_to_i[i]])

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
