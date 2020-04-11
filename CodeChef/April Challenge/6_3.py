import sys
import math
import random
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# SCORE:36803
# 焼きなまし
# あまり効果なし

T = int(readline())


def addScore(SCORE, arr, isPlus=True):
    for x in arr:
        if isPlus:
            SCORE[x] += 1
        else:
            SCORE[x] -= 1
    return SCORE


def solve_1(N, M, K, C, GRP):
    dbg = True
    CHOICE_IDX = []
    CHOICE_CNT = []

    for i in range(N):
        choose = [[] for _ in range(M)]
        cnt = [0] * M
        for k, c in enumerate(C[i]):
            choose[c - 1].append(k)
            cnt[c - 1] += 1

        CHOICE_IDX.append(choose)
        CHOICE_CNT.append(cnt)

    ANS = []
    SCORE = [0] * K
    for i in range(N):
        min_idx = SCORE.index(min(SCORE))
        c = C[i][min_idx]
        ANS.append(c)

        addScore(SCORE, CHOICE_IDX[i][c - 1])

    if GRP == 1 or GRP == 2:
        T = pow(10, 30)
        cool = 0.99
        idx = 0
        random.seed()

        while 1. < T:
            T *= cool
            idx += 1

            if idx % 1000 == 0:
                random.seed()

            i = random.randint(0, N - 1)
            now_c = ANS[i] - 1

            new_c = None
            if GRP == 1:
                new_c = 1 - now_c
            else:
                new_c = CHOICE_CNT[i].index(max(CHOICE_CNT[i]))
                if new_c == now_c:
                    continue

            now_score = min(SCORE)
            addScore(SCORE, CHOICE_IDX[i][now_c], False)
            addScore(SCORE, CHOICE_IDX[i][new_c])
            new_score = min(SCORE)

            delta = new_score - now_score
            p = pow(math.e, -abs(delta) / T)

            if 0 < delta or random.random() < p:
                ANS[i] = new_c + 1
            else:
                addScore(SCORE, CHOICE_IDX[i][now_c])
                addScore(SCORE, CHOICE_IDX[i][new_c], False)

    else:
        for i in range(N):
            now = min(SCORE)
            now_c = ANS[i] - 1
            mode = CHOICE_CNT[i].index(max(CHOICE_CNT[i]))
            if mode == now_c:
                continue

            addScore(SCORE, CHOICE_IDX[i][now_c], False)
            addScore(SCORE, CHOICE_IDX[i][mode])

            upd = min(SCORE)

            if now < upd:
                ANS[i] = mode + 1
                compile
            else:
                addScore(SCORE, CHOICE_IDX[i][now_c])
                addScore(SCORE, CHOICE_IDX[i][mode], False)

    return ANS


def solve():
    N, M, K = map(int, readline().split())
    C = [[int(x) for x in readline().split()] for _ in range(N)]

    '''
    group 1: N=100, M=2, K=1,000, Wmin=1, Wmax=1
    group 2: N=100, M=4, K=1,000, Wmin=45, Wmax=55
    group 3: N=200, M=2, K=5,000, Wmin=1, Wmax=5
    group 4: N=300, M=4, K=3,000, Wmin=1, Wmax=100
    group 5: N=500, M=9, K=2,000, Wmin=20, Wmax=80

    group 1: W=38
    group 2: W=100
    group 3: W=19
    group 4: W=29
    group 5: W=36
    '''

    GRP = 0
    if N == 100 and M == 2:
        GRP = 1
    elif N == 100 and M == 4:
        GRP = 2
    elif N == 200 and M == 2:
        GRP = 3
    elif N == 300 and M == 4:
        GRP = 4
    elif N == 500 and M == 9:
        GRP = 5

    ANS = solve_1(N, M, K, C, GRP)

    return " ".join(map(str, ANS))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
