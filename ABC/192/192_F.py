import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = X - max(A)
    for i in range(2, N + 1):
        # i個使う、mod iで考える
        DP = [[0] * i for _ in range(i + 1)]

        for j in range(N):
            # j個目を使う
            a = A[j]

            for k in range(i)[::-1]:
                # 今k個使っている時

                ## 0個使っている時は全部いれる
                if k == 0:
                    l = a % i
                    DP[k + 1][l] = max(DP[k + 1][l], a)
                    continue

                ## 1個以上入ってる時
                for m in range(i):
                    # mod mの値は

                    ## 0ならこれは存在してない
                    if DP[k][m] == 0:
                        continue

                    nxt = DP[k][m] + a
                    l = nxt % i
                    DP[k + 1][l] = max(DP[k + 1][l], nxt)

            # print(DP)

        u = X % i

        # print("{}個使う".format(i))
        # print(DP[i])
        # print(u, DP[i][u])

        if DP[i][u] == 0:
            continue
        else:
            t = (X - DP[i][u]) // i
            ans = min(ans, t)

    print(ans)

    return


if __name__ == "__main__":
    main()
