import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    UVC = [list(map(int, input().split())) for _ in range(M)]

    cnt_path = defaultdict(int)
    labels = defaultdict(list)

    for u, v, c in UVC:
        if u > v:
            u, v = v, u

        cnt_path[(u, v)] += 1
        labels[(u, v)].append(c)

    cnt_path = list(cnt_path.items())
    cnt_path.sort(key=lambda x: x[1])

    ans = [0] * (N + 1)
    USED = [False] * (N + 1)
    for path in cnt_path:
        u, v = path[0]

        # どちらも使用ずみ
        if USED[u] and USED[v]:
            continue

        cs = labels[(u, v)]

        # 双方使われていない
        if not USED[u] and not USED[v]:
            cu = cs[0]
            ans[u] = cu

            cv = -1
            if len(cs) == 1:
                cv = cu + 1
                if cv > N:
                    cv = 1
            else:
                cv = cs[1]

            ans[v] = cv

        if not USED[u]:
            cv = ans[v]

            cu = -1
            if cv in cs:
                cu = cv + 1
                if cu > N:
                    cu = 1
            else:
                cu = cs[0]

            ans[u] = cu

        if not USED[v]:
            cu = ans[u]

            cv = -1
            if cu in cs:
                cv = cu + 1
                if cv > N:
                    cv = 1
            else:
                cv = cs[0]

            ans[v] = cv

        USED[u] = True
        USED[v] = True

    print("\n".join(map(str, ans[1:])))

    return


if __name__ == "__main__":
    main()
