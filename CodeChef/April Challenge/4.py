import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def solve(N):
    CNT = [-1] * (N + 1)
    CNT[1] = 0

    for i in range(2, N + 1):
        if CNT[i] != -1:
            continue
        CNT[i] = 0
        idx = i + i
        c = 1
        while idx <= N:
            if i == 2:
                CNT[idx] = c
                c += 1
            elif CNT[idx] == -1:
                while idx % (c+1) == 0:
                    c += 1
                CNT[idx] = c
                c += 1
            idx += i

    print(CNT)

    m = N // 2 if N != 1 else 1
    ANS = [[] for _ in range(m)]
    for i in range(1, N + 1):
        idx = CNT[i]
        ANS[idx].append(i)

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
