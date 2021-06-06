import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    AA = [list(map(int, input().split())) for _ in range(N)]

    NUMS = []

    for j in range(N - K + 1):
        T = []
        for i in range(N - K + 1):
            ## 開始位置が (i,j)

            ## 最初
            if not T:
                for k in range(i, i + K):
                    T += AA[k][j : j + K]

            else:
                # それ以外
                T = T[K:]
                T += AA[i + K - 1][j : j + K]

            NUMS.append(T[:])

    left = 0
    right = pow(10, 9) + 10

    m = 0
    if K % 2 == 1:
        m = (K * K) // 2 + 1
    else:
        m = (K * K) // 2

    while (right - left) != 1:
        mid = (right + left) // 2

        flg = False
        for nn in NUMS:
            t = [1 for n in nn if n <= mid]
            if t and sum(t) >= m:
                flg = True
                break

        if flg:
            right = mid
        else:
            left = mid

    print(right)

    return


if __name__ == "__main__":
    main()
