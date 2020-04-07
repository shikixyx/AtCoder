from collections import Counter
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# SCORE:38051

T = int(readline())


def solve_1(N, M, K, C):
    CHOICE_IDX = []
    for c in range(1, M + 1):
        lst = [[i for i, x in enumerate(C[i]) if x == c] for i in range(N)]
        CHOICE_IDX.append(lst)

    ANS = []
    SCORE = [0] * K
    for i in range(N):
        min_idx = SCORE.index(min(SCORE))
        c = C[i][min_idx]
        ANS.append(c)

        for j in CHOICE_IDX[c-1][i]:
            SCORE[j] += 1
    return " ".join(map(str, ANS))


def solve():
    N, M, K = map(int, readline().split())
    C = [[int(x) for x in readline().split()] for _ in range(N)]

    ANS = solve_1(N, M, K, C)

    return " ".join(map(str, ANS))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
