import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = list(input())

    cnt = [defaultdict(lambda: deque()) for _ in range(2)]
    for i in range(N):
        s = int(S[i])
        a = A[i]

        cnt[s][a].append(i)

    # 同じものが下にないとダメ
    # この方針はNG
    OK = True
    for i in range(N):
        s = int(S[i])
        a = A[i]

        if s == 1:
            flg = False
            while len(cnt[0][a]) != 0:
                j = cnt[0][a].popleft()
                if i < j:
                    flg = True
                    break

            if not flg:
                OK = False
                break

    ans = 1
    if OK:
        ans = 0

    return ans


ANS = []
for _ in range(T):
    t = solve()
    ANS.append(t)

print("\n".join(map(str, ANS)))
