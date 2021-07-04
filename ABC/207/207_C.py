import sys
import itertools

sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    TLR = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x, y in itertools.combinations(range(N), 2):
        t1, l1, r1 = TLR[x]
        t2, l2, r2 = TLR[y]

        ## 右側
        if r1 < l2:
            continue

        if r1 == l2 and (t1 in [2, 4] or t2 in [3, 4]):
            continue

        ## 左側
        if r2 < l1:
            continue

        if r2 == l1 and (t1 in [3, 4] or t2 in [2, 4]):
            continue

        ans += 1

    print(ans)

    return


if __name__ == "__main__":
    main()
