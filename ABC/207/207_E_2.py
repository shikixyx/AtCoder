import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    mod_index = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

    acc = list(itertools.accumulate(A))

    for i in range(1, N + 1):
        for div in range(1, i + 1):
            mod_index[div][acc[i] % div].append(i)

    cnt = [[0] * 3010 for _ in range(3010)]
    cnt[1][1] = 1
    for i in range(1, N + 1):
        ## 今i個目をみてる
        for num in range(1, i + 1):
            ## num番目の数列がここで終わった
            if cnt[i][num] == 0:
                continue

            nxt = num + 1
            mod = acc[i] % nxt
            for x in mod_index[div][mod][::-1]:
                if x <= i:
                    break

                cnt[x][nxt] += cnt[i][num] % MOD

    print(sum(cnt[N + 1]))

    return


if __name__ == "__main__":
    main()
