import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7

T = int(input())


def solve():
    N, K, W = map(int, input().split())
    L = list(map(int, input().split()))
    AL, BL, CL, DL = map(int, input().split())
    H = list(map(int, input().split()))
    AH, BH, CH, DH = list(map(int, input().split()))

    for i in range(K, N):
        l = (L[-2] * AL + L[-1] * BL + CL) % DL + 1
        h = (H[-2] * AH + H[-1] * BH + CH) % DH + 1
        L.append(l)
        H.append(h)

    rtn = 1
    prev = (W * 2 + H[0] * 2) % MOD
    rtn *= prev
    rtn %= MOD

    P = []
    P.append(prev)

    for i in range(1, N):
        left_x_r = L[i - 1] + W
        right_x_l = L[i]

        now = prev
        now += W * 2
        now %= MOD
        now += H[i] * 2
        now %= MOD

        # 超えている
        if left_x_r < right_x_l:
            pass
        # 超えていない
        else:
            mh = min(H[i], H[i - 1])
            now -= (W - (L[i] - L[i - 1])) * 2
            now %= MOD
            now -= mh * 2
            now %= MOD

        rtn *= now
        rtn %= MOD
        prev = now

        P.append(now)

    print(P)
    return rtn


ans = []
for i in range(1, T + 1):
    t = solve()
    txt = "Case #{}: {}".format(i, t)
    ans.append(txt)

print("\n".join(ans))

