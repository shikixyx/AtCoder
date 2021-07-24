import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    count = defaultdict(int)

    t = 0
    ## init
    for j in range(K):
        if count[C[j]] == 0:
            t += 1
        count[C[j]] += 1

    ans = t

    prev = ans
    idx = 0
    for i in range(K, N):
        tmp = prev

        ## iを入れる
        if count[C[i]] == 0:
            tmp += 1

        count[C[i]] += 1

        ## idx をとる
        if count[C[idx]] == 1:
            tmp -= 1

        count[C[idx]] -= 1

        idx += 1
        ans = max(tmp, ans)
        prev = tmp

    print(ans)

    return


if __name__ == "__main__":
    main()
