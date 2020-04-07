from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def solve(N):
    DIV = [[] for _ in range(N + 1)]
    isPrime = [True] * (N + 1)
    PRIMES = defaultdict(int)

    # 約数の配列
    for i in range(2, N + 1):
        if not isPrime[i]:
            continue

        PRIMES[i] = 0

        for j in range(i + i, N + 1, i):
            DIV[j].append(i)
            isPrime[j] = False

    m = N // 2 if N != 1 else 1
    ANS = [[] for _ in range(m)]

    # 数字を試す
    for i in range(1, N + 1):
        # 素数
        if isPrime[i]:
            ANS[0].append(i)
            continue

        # 合成数
        idx = 0
        for x in DIV[i]:
            idx = max(idx, PRIMES[x])

        idx += 1
        ANS[idx].append(i)

        # update
        for x in DIV[i]:
            PRIMES[x] = idx

    RET = []
    RET.append(m)
    for i in range(m):
        L = len(ANS[i])
        tmp = [L] + ANS[i]
        RET.append(" ".join(map(str, tmp)))

    return RET


ans = []
for _ in range(T):
    N = int(input())
    t = solve(N)
    ans.append("\n".join(map(str, t)))

print("\n".join(map(str, ans)))
exit(0)
