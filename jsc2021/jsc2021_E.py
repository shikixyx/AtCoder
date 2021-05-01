import sys
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M, Q = map(int, input().split())
    TXY = [list(map(int, input().split())) for _ in range(Q)]

    SUM = 0
    A = [0] * N
    B = [0] * M
    AB = [A, B]

    sorted_A = [0] * N
    sorted_B = [0] * M

    cum_A = [0] * N
    cum_B = [0] * M

    for t, x, y in TXY:
        ## 変更前と後
        bef, aft = AB[t - 1][x - 1], y

        ## 値を更新
        AB[t - 1][x - 1] = y

        ## 和を更新
        ## 同じ
        if bef == aft:
            continue

        ## 大きく
        if bef < aft:
            ## Aに更新→Bをみる
            if t == 1:
                n = bisect.bisect_right(sorted_B, bef)
            else:
                bisect.bisect_right(sorted_A, bef)

            SUM += n * (aft - bef)

        ## 小さく
        else:
            if t == 1:
                cum = cum_B
                sor = sorted_B
            else:
                cum = cum_A
                sor = sorted_A

            num_smller_than_bef = bisect.bisect_left(sor, bef)
            num_smaller_than_aft = bisect.bisect_left(sor, aft)
            rest = num_smller_than_bef - num_smaller_than_aft

            ## befより小さいのがあった時
            if num_smller_than_bef != 0:

                ## 一度引く
                SUM -= bef * num_smller_than_bef

                ## 足す
                SUM += num_smaller_than_aft * aft
                SUM += cum[num_smller_than_bef - 1]

                if rest != 0:
                    SUM += aft * rest
                    SUM -= cum[num_smller_than_bef - 1]

        ## 列を更新
        


        ## 区間和を更新

    return


if __name__ == "__main__":
    main()
