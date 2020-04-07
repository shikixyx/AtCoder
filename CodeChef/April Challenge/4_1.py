import sys
import math
import fractions
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def solve(N):
    CNT = [-1] * (N + 1)
    CNT[1] = 0
    m = N // 2 if N != 1 else 1
    ANS = [[] for _ in range(m)]
    ANS[0].append(1)

    for i in range(2, N + 1):
        if CNT[i] != -1:
            continue
        CNT[i] = 0
        ANS[0].append(i)

        nxt = i + i
        c = 0

        if i == 2:
            while nxt <= N:
                c += 1
                ANS[c].append(nxt)
                CNT[nxt] = c
                nxt += i
            continue

        while nxt <= N:
            if CNT[nxt] != -1:
                nxt += i
                continue
            for _ in range(N):
                c += 1
                ok = True
                for x in ANS[c]:
                    gcd = fractions.gcd(x, nxt)
                    if gcd != 1:
                        ok = False
                        break

                if ok:
                    ANS[c].append(nxt)
                    CNT[nxt] = c
                    break
            nxt += i

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
