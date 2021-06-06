import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def judge(mid, arr, N, K, m):
    # print("mid == {}, m == {}".format(mid, m))

    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= mid:
                new_arr[i][j] = 1

    cumsum = [[0] * N for _ in range(N)]
    for i in range(N):
        t = 0
        for j in range(N):
            t += new_arr[i][j]
            cumsum[i][j] = t

    # print(new_arr)
    # print(cumsum)

    for j in range(N - K + 1):
        cnt = 0
        first = True

        for i in range(N - K + 1):
            ## 開始位置が(i,j)

            if first:
                ## 最初は全部たす
                for k in range(i, i + K):
                    cnt += cumsum[k][j + K - 1]

                    if j != 0:
                        cnt -= cumsum[k][j - 1]

                first = False
            else:
                ## 前の行を引いて、最後を足す
                t = cumsum[i - 1][j + K - 1]
                if j != 0:
                    t -= cumsum[i - 1][j - 1]

                cnt -= t

                cnt += cumsum[i + K - 1][j + K - 1]
                if j != 0:
                    cnt -= cumsum[i + K - 1][j - 1]

            # print("i,j = {} {} ,cnt = {}".format(i, j, cnt))

            if cnt >= m:
                return True

    return False


def main():
    N, K = map(int, input().split())
    AA = [list(map(int, input().split())) for _ in range(N)]

    left = -1
    right = pow(10, 9) + 10

    m = K * K - ((K * K) // 2 + 1) + 1

    while (right - left) != 1:
        mid = (right + left) // 2

        flg = judge(mid, AA, N, K, m)
        # print(flg)

        if flg:
            right = mid
        else:
            left = mid

    print(right)

    return


if __name__ == "__main__":
    main()
