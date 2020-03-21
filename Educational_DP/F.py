import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve():

    S = input()
    T = input()

    LS = len(S)
    LT = len(T)

    dp = [[0] * (LT + 1) for _ in range(LS + 1)]
    pre = [[None] * (LT + 1) for _ in range(LS + 1)]
    for i in range(LS):
        for j in range(LT):
            now = 0
            if S[i] == T[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                pre[i+1][j+1] = 1
            else:
                if dp[i + 1][j] < dp[i][j + 1]:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                    pre[i+1][j+1] = 2
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                    pre[i+1][j+1] = 3

    # print(dp)

    # for p in pre:
        # print(p)

    si = LS
    ti = LT
    ans = []

    while not ((si == 0) and (ti == 0)):
        frm = pre[si][ti]
        if frm == 1:
            si -= 1
            ti -= 1
            ans.append(S[si])
        elif frm == 2:
            si -= 1
        elif frm == 3:
            ti -= 1
        elif frm == None:
            break

    return ans[::-1]


ans = solve()
print("".join(ans))
