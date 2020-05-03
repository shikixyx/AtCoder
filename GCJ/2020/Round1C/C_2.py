import sys
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    N, D = map(int, readline().split())
    A = list(map(int, readline().split()))
    rest = 365 * (10 ** 9) - sum(A)
    A.append(rest)

    ans = D - 1

    ok = False
    for a in A:
        NEW = [(b % a, b) for b in A]
        NEW.sort()

        LDP = 100
        DP = list(range(LDP))

        L = len(NEW)

        for i in range(L):
            md, b = NEW[i]

            if b < a:
                continue

            if a == b:
                for j in range(LDP - 1):
                    DP[j] = max(DP[j] - 1, 0)
                continue

            if md == 0:
                b_by_a = b // a
                for j in range(1, LDP - 1):
                    if LDP - 1 < j + b_by_a:
                        continue
                    DP[j + b_by_a] = min(DP[j] + b_by_a - 1, DP[j + b_by_a])
                    DP[j + b_by_a] = max(0, DP[j + b_by_a])

        ans = min(ans, DP[D])

    return ans


ans = []
for i in range(1, T + 1):
    r = solve()
    txt = "Case #{}: {}".format(i, r)
    ans.append(txt)

print("\n".join(ans))
