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

        cnt = 0
        now_D = D
        for md, b in NEW:
            if now_D == 0:
                break

            # 小さいやつはだめ
            if b < a:
                continue

            # 同じ
            if b == a:
                now_D -= 1
                continue

            # 何きれぶんか
            b_by_a = b // a

            # これでOKの場合
            if now_D == b_by_a:
                cnt += b_by_a

                # きれいに切れる場合は1回少ない
                if md == 0:
                    cnt -= 1

                now_D = 0
                continue

            # 何きれ使うか
            cut = min(now_D, b // a)

            # 残り分使う
            if cut == now_D:
                cnt += cut
                now_D = 0
                continue
            else:
                cnt += b_by_a
                if md == 0:
                    cnt -= 1
                now_D -= b_by_a

        if now_D == 0:
            ans = min(ans, cnt)

    return ans


ans = []
for i in range(1, T + 1):
    r = solve()
    txt = "Case #{}: {}".format(i, r)
    ans.append(txt)

print("\n".join(ans))
